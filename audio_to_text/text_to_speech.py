#%%

#%%
import torch
import time
from pprint import pprint
from omegaconf import OmegaConf
from IPython.display import Audio, display
import torch
#import sounddevice as sd
from playaudio import MyPlayAudio

# torch.hub.download_url_to_file('https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
#                                'latest_silero_models.yml',
#                                progress=False)
# models = OmegaConf.load('latest_silero_models.yml')


# available_languages = list(models.tts_models.keys())
# print(f'Available languages {available_languages}')

# for lang in available_languages:
#     _models = list(models.tts_models.get(lang).keys())
#     print(f'Available models for {lang}: {_models}')
    
    


language = 'ru'
model_id = 'v4_ru'
#device = torch.device('cuda')
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)

print(model)
model.to(device)  # gpu or cpu


sample_rate = 48000
speaker = 'xenia'
put_accent=True
put_yo=True
example_text = 'В недрах тундры выдры в г+етрах т+ырят в вёдра ядра к+едров.'

example_text = 'Привет! Я твой голосовой помощник, можешь давать команды.'

sd = MyPlayAudio()

def play_text_sound(text:str):
    '''функция для озвучивание текста 
    '''
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo,)
    #print(example_text)
    #display(Audio(audio, rate=sample_rate))
    #print(type(audio),audio.shape)
    # import torchaudio
    # torchaudio.io.play_audio(audio,sample_rate=sample_rate)

    #Audio(audio, rate=sample_rate,autoplay=True)

    #fs = sample_rate
    sd.play(audio.numpy())

#time.sleep(10)

if __name__ == '__main__':
    #print(sd.query_devices())
    play_text_sound('привет? как дела, я тут говорю!')
