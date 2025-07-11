# Валидация модели.
#%%
import os
import warnings
warnings.filterwarnings("ignore")
from transformers import pipeline
import librosa
import evaluate
import pandas as pd
from glob import glob
from tqdm import tqdm
from whisper.normalizers.basic import BasicTextNormalizer
normalise_text = BasicTextNormalizer()
metric = evaluate.load("wer")
#%%
# model_name = 'openai/whisper-small'
# model_name_prefix = '_p_small' # 0.32 4:26:36 (78183)  0.38483

# model_name = 'openai/whisper-large-v3-turbo'
# model_name_prefix = '_p_v3_turbo' #0.24847 11:10:35 (78183)

# model_name = 'openai/whisper-medium'
# model_name_prefix = '_p_medium' #?0.27387 11:52:28



device = 'cuda'
language = 'russian'

whisper = pipeline("automatic-speech-recognition",
                    model= model_name,
                    generate_kwargs={"task": "transcribe",'language':language,
                                    # 'suppress_tokens':"",
                                    # 'beam_size':5,
                                    # 'vad_filter':True,
                                    # 'vad_parameters':dict(min_silence_duration_ms=1000)
                                    }, device=device)


# %%
def get_text(path_text):
    with open(path_text,'r') as f:
        return normalise_text(f.read()).strip()
        
def get_data_file(full_path):
    #full_path = 'data/asr_public_stories_2/1/5d/3193016288ea.opus'
    full_path_text = os.path.splitext(full_path)[0]+'.txt'

    assert os.path.isfile(full_path), f'file not exists {full_path=}'
    assert os.path.isfile(full_path_text), f'file not exists {full_path_text=}'

    data, rate = librosa.load(full_path)
    validate_text = get_text(full_path_text)
    return data,normalise_text(validate_text).strip()

def predict_by_files(full_paths):    
    datas = []
    validate_texts = []
    full_path_to_predict = []
    for full_path in full_paths:
        full_path_result = os.path.splitext(full_path)[0]+f'{model_name_prefix}.txt'
        if os.path.isfile(full_path_result):
            continue
        full_path_to_predict.append(full_path)
        data,validate_text = get_data_file(full_path)
        datas.append(data)
        validate_texts.append(validate_text)
    # print(f'{len(data)=}, {rate=}')
    if len(datas) == 0:
        return
    
    results = whisper(datas)
    
    predicted_texts = [normalise_text(result['text']).strip() for result in results]
    for predicted_text,full_path in zip(predicted_texts,full_path_to_predict):
        full_path_result = os.path.splitext(full_path)[0]+f'{model_name_prefix}.txt'
        with open(full_path_result,'w') as f:
            f.write(predicted_text)
    
    #wer = metric.compute(references=[predicted_text_n], predictions=[validate_text_n])
    # return [{
    #     'predicted_text':predicted_text,
    #     'validate_text':validate_text,
    #     'wer':metric.compute(predictions=[predicted_text],references=[validate_text])
    # } for predicted_text,validate_text in zip(predicted_texts,validate_texts)]
    # print(predicted_text_n)
    # print(validate_text_n)
    # print()

def predict_all():
    #df = pd.DataFrame()
    dataset_base_path = 'data/asr_public_stories_2'
    files = glob(f'{dataset_base_path}/**/**/*.opus')
    print(len(files))
    #i = 0
    
    batch_size = 50
    cur_count = 0
    file_batch = []
    for file in tqdm(files):
        
        file_batch.append(file)
        cur_count+= 1
        
        if cur_count == batch_size:            
            predict_by_files(file_batch)
            #df = pd.concat([df,pd.DataFrame(res)])
            file_batch.clear()
            cur_count = 0
        
        # if i > 5:
        #     break
        # i+=1

    if cur_count>0:
        predict_by_files(file_batch)
    
    #return df
#%%


def get_all_texts():
    dataset_base_path = 'data/asr_public_stories_2'
    files = glob(f'{dataset_base_path}/**/**/*{model_name_prefix}.txt')
    print(len(files))
    results = []
    for file_predict in tqdm(files):
        file_fact = file_predict.replace(f'{model_name_prefix}.txt','.txt')
        results.append((
            get_text(file_predict),
            get_text(file_fact)
        ))
    return results

def get_result_metric(texts):
    result_wer = metric.compute(
        predictions=[t[0] for t in texts],
        references=[t[1] for t in texts],
    )
    print(f'{result_wer=}')

#%%
predict_all()
texts = get_all_texts()
get_result_metric(texts)

# %%
