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
import evaluate
metric = evaluate.load("wer")

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch")

torch.cuda.empty_cache()
gc.collect()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model_name_prefix = '_my_small' #_hf
#DEVICE = "cpu"
model = None
pipe = None
from transformers import pipeline
from transformers import WhisperModel
def load_model():
    global model
    # Загружаем предобученную модель
    model = whisper.load_model("small").to(DEVICE) #0.25664  100 за 00:30
    #checkpoint = torch.load("whisper_finetuned.pth", map_location=DEVICE) #0.5412  100 за 06:54
    #model.load_state_dict(checkpoint)   

    #model = WhisperModel.from_pretrained("./whisper-small-dv_1")
    #model
    pass

def load_pipe():
    global pipe
    #pipe = pipeline("automatic-speech-recognition", model="./whisper-small-dv/checkpoint-500") #0.404255 100 за 00:37
    pipe = pipeline("automatic-speech-recognition", model="./whisper-small-dv_1/checkpoint-500") #0.32446 100 за 00:36
#%%
#%%
def get_text(path_text):
    with open(path_text,'r') as f:
        return f.read().strip()

def get_data_file(full_path):
    #full_path = 'data/asr_public_stories_2/1/5d/3193016288ea.opus'
    full_path_text = os.path.splitext(full_path)[0] +'.txt'

    assert os.path.isfile(full_path), f'file not exists {full_path=}'
    assert os.path.isfile(full_path_text), f'file not exists {full_path_text=}'
    
    validate_text = get_text(full_path_text)
    return full_path,normalise_text(validate_text).strip()

def get_dataset(dataset_base_path:str,train:bool,only_path = False,top = None):
    '''
        result {
            audio_path
            text (if only_path == False)
        }
    '''
    files = glob(f'{dataset_base_path}/**/**/*.opus')
    folders = set(['c','d','e','f']) #тестовые папки
    dataset = []
    i = 0
    for file in files:
        base_fold = file.replace(f'{dataset_base_path}/','')
        base_fold = base_fold.split('/')[0]
        if train and base_fold in folders:
            continue        
        if not train and base_fold not in folders:
            continue            
        if only_path:
            dataset.append({
                'audio_path':file,
            })
        else:
            line = get_data_file(file)
            dataset.append({
                'audio_path':line[0],
                'text':line[1],
            })
        i += 1
        if top is not None and i >= top: break
    return dataset
# dataset_test = get_dataset('data/asr_public_stories_2',train=False,only_path = True,top=100)
# print(len(dataset_test))
#%%
def start_valid(replace=False):
    language = 'ru'
    task = 'transcribe'
    

    dataset_test = get_dataset('data/asr_public_stories_2',train=False,only_path = True,top=100)
    print(len(dataset_test))

    with torch.no_grad():
        for ds in tqdm(dataset_test):
            audio_path = ds['audio_path']
            full_path_result = os.path.splitext(audio_path)[0]+f'{model_name_prefix}.txt'
            if not replace and os.path.isfile(full_path_result):
                continue
            #text_fact = ds['text']
            result = None
            if model:
                #full_path = 'data/asr_public_stories_2/1/5d/3193016288ea.opus'
                SPEECH_WAVEFORM, SAMPLE_RATE = torchaudio.load(audio_path)
                result = model.transcribe(SPEECH_WAVEFORM[0],language=language)
                #result = model.transcribe(audio_path, language=language)
            if pipe:
                result = pipe(audio_path)
            #print()
            predicted_text = normalise_text(result["text"]).strip()
            with open(full_path_result,'w') as f:
                f.write(predicted_text)
            
#%%
##result = model.transcribe(SPEECH_WAVEFORM[0], language=language)



def get_all_texts():
    dataset_base_path = 'data/asr_public_stories_2'
    files = glob(f'{dataset_base_path}/**/**/*{model_name_prefix}.txt')
    print(len(files))
    results = []
    for file_predict in tqdm(files):
        file_fact = file_predict.replace(f'{model_name_prefix}.txt','.txt')
        results.append((
            normalise_text(get_text(file_predict)).strip(),
            normalise_text(get_text(file_fact)).strip(),
        ))
    return results

def get_result_metric(texts):
    result_wer = metric.compute(
        predictions=[t[0] for t in texts],
        references=[t[1] for t in texts],
    )
    print(f'{result_wer=}')

def start():
    #load_model()
    load_pipe()
    start_valid(replace=True)
        
    texts = get_all_texts()
    get_result_metric(texts)

if __name__ == '__main__':
    start()
