#https://huggingface.co/learn/audio-course/ru/chapter5/fine-tuning
#%%
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from torch.utils.data import Dataset as t_Dataset

from transformers import (Seq2SeqTrainer,
                          Seq2SeqTrainingArguments,
                          WhisperForConditionalGeneration,
                          WhisperProcessor)

from transformers.models.whisper.english_normalizer import BasicTextNormalizer
from transformers.models.whisper.tokenization_whisper import TO_LANGUAGE_CODE
from typing import Any, Dict, List, Union
from validate_my_model_stt import get_dataset
import evaluate
import torch
import torchaudio
metric = evaluate.load("wer")

def get_dt(): return f'{datetime.now():%H:%M:%S}'
def log(msg:str):
    print(f'{get_dt()} - {msg}')

language = 'russian'
assert language in TO_LANGUAGE_CODE, f'not correct language {language}'

log(f'load processor')
processor = WhisperProcessor.from_pretrained("openai/whisper-small", language=language, task="transcribe")

@dataclass
class DataCollatorSpeechSeq2SeqWithPadding:
    processor: Any

    def __call__(
        self, features: List[Dict[str, Union[List[int], torch.Tensor]]]
    ) -> Dict[str, torch.Tensor]:
        # split inputs and labels since they have to be of different lengths and need different padding methods
        # first treat the audio inputs by simply returning torch tensors
        input_features = [
            {"input_features": feature["input_features"][0]} for feature in features
        ]
        batch = self.processor.feature_extractor.pad(input_features, return_tensors="pt")

        # get the tokenized label sequences
        label_features = [{"input_ids": feature["labels"]} for feature in features]
        # pad the labels to max length
        labels_batch = self.processor.tokenizer.pad(label_features, return_tensors="pt")

        # replace padding with -100 to ignore loss correctly
        labels = labels_batch["input_ids"].masked_fill(
            labels_batch.attention_mask.ne(1), -100
        )

        # if bos token is appended in previous tokenization step,
        # cut bos token here as it's append later anyways
        if (labels[:, 0] == self.processor.tokenizer.bos_token_id).all().cpu().item():
            labels = labels[:, 1:]

        batch["labels"] = labels

        return batch

class ListDataset(t_Dataset):
    def __init__(self, data:list): self.data = data
    def __len__(self): return len(self.data)
    def __getitem__(self, idx): return self.data[idx]


normalizer = BasicTextNormalizer()


def compute_metrics(pred):
    pred_ids = pred.predictions
    label_ids = pred.label_ids

    # replace -100 with the pad_token_id
    label_ids[label_ids == -100] = processor.tokenizer.pad_token_id

    # we do not want to group tokens when computing the metrics
    pred_str = processor.batch_decode(pred_ids, skip_special_tokens=True)
    label_str = processor.batch_decode(label_ids, skip_special_tokens=True)

    # compute orthographic wer
    wer_ortho = 100 * metric.compute(predictions=pred_str, references=label_str)

    # compute normalised WER
    pred_str_norm = [normalizer(pred) for pred in pred_str]
    label_str_norm = [normalizer(label) for label in label_str]
    # filtering step to only evaluate the samples that correspond to non-zero references:
    pred_str_norm = [
        pred_str_norm[i] for i in range(len(pred_str_norm)) if len(label_str_norm[i]) > 0
    ]
    label_str_norm = [
        label_str_norm[i]
        for i in range(len(label_str_norm))
        if len(label_str_norm[i]) > 0
    ]

    wer = 100 * metric.compute(predictions=pred_str_norm, references=label_str_norm)

    return {"wer_ortho": wer_ortho, "wer": wer}

def get_model():
    print(f'load model')
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

    # disable cache during training since it's incompatible with gradient checkpointing
    model.config.use_cache = False

    # set language and task for generation and re-enable cache
    model.generate = partial(
        model.generate, language=language, task="transcribe", use_cache=True
    )
    return model
model = get_model()
#%%
type(model.model)
#%%
model.forward?
#%%
import numpy as np
print(
    #f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)
#%%
for p in model.parameters():
    print(p.shape)
#%%

def get_training_args():
    training_args = Seq2SeqTrainingArguments(
        output_dir="./whisper-small-dv_1",  # name on the HF Hub
        per_device_train_batch_size=16,
        gradient_accumulation_steps=1,  # increase by 2x for every 2x decrease in batch size
        learning_rate=1e-5,
        lr_scheduler_type="constant_with_warmup",
        warmup_steps=50,
        max_steps=500,  # increase to 4000 if you have your own GPU or a Colab paid plan
        gradient_checkpointing=True,
        fp16=True,
        fp16_full_eval=True,
        evaluation_strategy="steps",
        per_device_eval_batch_size=16,
        predict_with_generate=True,
        generation_max_length=225,
        save_steps=500,
        eval_steps=500,
        logging_steps=25,
        report_to=["tensorboard"],
        load_best_model_at_end=True,
        metric_for_best_model="wer",
        greater_is_better=False,
        push_to_hub=False,  #не загружать контрольные точки модели на Hugging Face Hub
    )
    return training_args
#ImportError: Using the `Trainer` with `PyTorch` requires `accelerate>=0.26.0`: Please run `pip install transformers[torch]` or `pip install 'accelerate>=0.26.0'`
#poetry add transformers[torch]
#FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead

def prepare_dataset_my(example):
    waveform, sample_rate = torchaudio.load(example['audio_path'])
    example = processor(
        audio=waveform[0].numpy(),
        sampling_rate=sample_rate,
        text=example["text"],
    )

    # compute input length of audio sample in seconds
    example["input_length"] = len(waveform) / sample_rate

    return example

def get_dataset():
    print(f'start load dataset')
    train_dataset = get_dataset('data/asr_public_stories_2',train=True,only_path = False,top=1500)
    test_dataset = get_dataset('data/asr_public_stories_2',train=False,only_path = False,top=500)

    print(f'start prepared dataset')
    prepared_train_dataset = ListDataset(list(map(prepare_dataset_my,train_dataset)))
    prepared_test_dataset = ListDataset(list(map(prepare_dataset_my,test_dataset)))
    for i in prepared_train_dataset: break
    for i in prepared_test_dataset: break
    return {
        'train':prepared_train_dataset,
        'test':prepared_test_dataset,        
    }

def start_train():
    model = get_model()
    dateset = get_dataset()
    training_args = get_training_args()    
    data_collator = DataCollatorSpeechSeq2SeqWithPadding(processor=processor)
    
    trainer = Seq2SeqTrainer(
        args=training_args,
        model=model,
        train_dataset=dateset['train'],
        eval_dataset=dateset['test'],
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        tokenizer=processor,
    )

    print(f'start_train')
    result = trainer.train()
    return result

if __name__ == '__main__':
    result = start_train()
    print(result)
