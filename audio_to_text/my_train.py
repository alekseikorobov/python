#дообучение модели whisper!
# %%
import torch
import whisper
from tqdm import tqdm
import gc,torch
import torch.nn as nn
from torch.optim import AdamW
import torchaudio
import torchaudio.transforms as transforms
from whisper.utils import exact_div
from whisper.audio import pad_or_trim
from torch.utils.data import Dataset, DataLoader
import json,os
from whisper.normalizers.basic import BasicTextNormalizer
normalise_text = BasicTextNormalizer()
from glob import glob
import time,datetime

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch")

torch.cuda.empty_cache()
gc.collect()


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
#DEVICE = "cpu"

# Загружаем предобученную модель
model = whisper.load_model("small").to(DEVICE)
model
#%%
#model.forward?
type(model)

#%%
for p in model.parameters():
    print(p.shape)
#%%
import numpy as np
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)
#%%
# Проверяем архитектуру
#print(model)
#-%%
#model.tokenizer
#dir(whisper.tokenizer)
# text = 'привет'
# tokens = whisper.tokenizer.get_encoding("cl100k_base").encode(text)
# tokens
#-%%

#-%%
language = 'ru'
task = 'transcribe'
tokenizer = whisper.tokenizer.get_tokenizer(
                    model.is_multilingual,
                    num_languages=model.num_languages,
                    language=language,
                    task=task)

#MAX_TOKENS = 256  # Фиксированная длина последовательности токенов
#MAX_TOKENS = 51865
MAX_TOKENS = 448
# hard-coded audio hyperparameters
SAMPLE_RATE = 16000
N_FFT = 400
HOP_LENGTH = 160
CHUNK_LENGTH = 30
N_SAMPLES = CHUNK_LENGTH * SAMPLE_RATE  # 480000 samples in a 30-second chunk
N_FRAMES = exact_div(N_SAMPLES, HOP_LENGTH)  # 3000 frames in a mel spectrogram input

N_SAMPLES_PER_TOKEN = HOP_LENGTH * 2  # the initial convolutions has stride 2
FRAMES_PER_SECOND = exact_div(SAMPLE_RATE, HOP_LENGTH)  # 10ms per audio frame
TOKENS_PER_SECOND = exact_div(SAMPLE_RATE, N_SAMPLES_PER_TOKEN)  # 20ms per audio token


def tokenize_text(text, tokenizer):
    tokens = tokenizer.encode(text)

    # Обрезаем слишком длинные токены
    if len(tokens) > MAX_TOKENS:
        tokens = tokens[:MAX_TOKENS]
    else:
        # Дополняем паддингом (используем токен конца `eot_token_id`)
        pad_size = MAX_TOKENS - len(tokens)
        tokens += [tokenizer.eot] * pad_size  # Заполняем `eot_token_id`
    
    return torch.tensor(tokens)#,dtype=torch.float)

#tokenize_text('текст очень длинный',tokenizer).shape

#-%%
tokenizer.encode('')
#-%%
# model.dims.n_mels
# #-%%
# tokenizer.encoding.special_tokens_set
# #-%%





# Фиксированная длина (30 секунд при 16000 Гц → 30000 * 80 / 512 ≈ 300)
# MAX_MEL_FRAMES = 3000

def preprocess_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    
    if sample_rate != 16000:
        resample = transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resample(waveform)
    
    # Преобразуем в Mel spectrogram (Whisper использует 80 mel-банков)
    mel_spec = whisper.log_mel_spectrogram(waveform, model.dims.n_mels, padding=N_SAMPLES).to(DEVICE)    
    
    mel_segment = pad_or_trim(mel_spec, N_FRAMES)#.to(model.device).to(dtype)
    mel_segment = mel_segment.squeeze(0)
    return mel_segment
    
    # #print(f'{mel_spec.shape[-1]=}')
    # if mel_spec.shape[-1] > N_FRAMES:
    #     mel_spec = mel_spec[:, :, :N_FRAMES]  # Обрезаем
    # else:
    #     pad_size = N_FRAMES - mel_spec.shape[-1]
    #     mel_spec = torch.nn.functional.pad(mel_spec, (0, pad_size))  # Дополняем нулями
    # mel_spec = mel_spec.squeeze(0)#.unsqueeze(0)
    # return mel_spec

def get_text(path_text):
    with open(path_text,'r') as f:
        return f.read().strip()

def get_data_file(full_path):
    #full_path = 'data/asr_public_stories_2/1/5d/3193016288ea.opus'
    full_path_text = os.path.splitext(full_path)[0]+'.txt'

    assert os.path.isfile(full_path), f'file not exists {full_path=}'
    assert os.path.isfile(full_path_text), f'file not exists {full_path_text=}'
    
    validate_text = get_text(full_path_text)
    return full_path,normalise_text(validate_text).strip()

class WhisperDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        audio_path = self.data[idx]["audio_path"]
        text = self.data[idx]["text"]
        
        mel_spec = preprocess_audio(audio_path)        
        tokens = tokenize_text(text,tokenizer)
                
        #print(mel_spec.type(),tokens.type())
        
        return mel_spec, tokens

def get_dataset(dataset_base_path:str,train:bool,top = None):
    '''
        result {
            audio_path
            text
        }
    '''
    files = glob(f'{dataset_base_path}/**/**/*.opus')
    folders = set(['c','d','e','f']) #тестовые папки
    dataset = []
    for i,file in enumerate(files):
        base_fold = file.replace(f'{dataset_base_path}/','')
        base_fold = base_fold.split('/')[0]
        if train and base_fold in folders:
            continue        
        if not train and base_fold not in folders:
            continue            
        line = get_data_file(file)
        dataset.append({
            'audio_path':line[0],
            'text':line[1],
        })
        if top is not None and i >= top: break
    return dataset
        

dataset = get_dataset('data/asr_public_stories_2',train=True)
print(len(dataset))
# потом для валидации проверим:
# dataset_test = get_dataset('data/asr_public_stories_2',train=False)
# print(len(dataset_test))
#%%

# # Загружаем датасет из JSON
# with open("data/dataset.json", "r", encoding="utf-8") as f:
#     dataset = json.load(f)

train_dataset = WhisperDataset(dataset)
train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True, collate_fn=None)
# for mel_spec, tokens in tqdm(train_loader):
#     print(mel_spec.shape, tokens.shape)
#     print(mel_spec.type(), tokens.type())
#     break
# #-%%
# print(tokenizer.eot)
# print(tokenizer.sot)

#-%%


# Игнорируем паддинг-токены при вычислении лосса


#%%
def my_train():
    criterion = nn.CrossEntropyLoss(ignore_index=tokenizer.eot)
    optimizer = AdamW(model.parameters(), lr=1e-5, weight_decay=1e-4)

    NUM_EPOCHS = 20

    model.train()

    start = time.time()

    for epoch in range(NUM_EPOCHS):
        epoch_loss = 0
        for mel_spec, tokens in tqdm(train_loader):
            mel_spec, tokens = mel_spec.to(DEVICE), tokens.to(DEVICE)

            optimizer.zero_grad()
            
            # Энкодинг аудио
            encoded_audio = model.encoder(mel_spec)

            # Teacher forcing: подаём "сдвинутые вправо" токены как вход
            #decoder_input = tokens[:, :-1]
            #target = tokens[:, 1:]

            #print(f'{encoded_audio.type()=}, {decoder_input.type()=}')
            # Прогоняем через декодер
            outputs = model.decoder(tokens,encoded_audio)
            #print(outputs.shape,tokens.shape)
            # Переформатируем выходные данные для CrossEntropyLoss
            loss = criterion(outputs.view(-1, outputs.size(-1)), tokens.view(-1))
            
            #loss = criterion(outputs, tokens)
            
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
        
        print(f"Epoch [{epoch+1}/{NUM_EPOCHS}], Loss: {epoch_loss:.4f}")

    end = time.time() - start

    print(f'done train {datetime.timedelta(seconds=end)}')
    print('save model')
    result_path = "whisper_finetuned.pth"
    if os.path.isfile(result_path):
        os.remove(result_path)
    torch.save(model.state_dict(), result_path)
#%%
def test():
    full_path = 'data/asr_public_stories_2/1/5d/3193016288ea.opus'
    SPEECH_WAVEFORM, SAMPLE_RATE = torchaudio.load(full_path)
    text = get_text(full_path.replace('.opus','.txt'))    
    with torch.no_grad():
        result = model.transcribe(SPEECH_WAVEFORM[0].numpy())

    normalise_text(text).strip(),normalise_text(result['text']).strip()
    from IPython.display import Audio
    Audio(full_path)
    
if __name__ == '__main__':
    my_train()