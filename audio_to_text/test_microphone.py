from vosk import Model, KaldiRecognizer
import os
import json
import time
import pyautogui
import keyboard
# if not os.path.exists("model-en"):
#     print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model' in the current folder.")
#     exit (1)

import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

#model = Model("model-en")

model = Model(model_path='data/vosk-model-ru-0.42')
rec = KaldiRecognizer(model, 16000)

qwerty = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
ycuken = "йцукенгшщзхъфывапролджэячсмитьбюё"
tr = dict(zip(ycuken, qwerty))

def send_text_to_active_window(text):
    # Эмулируем ввод текста
    os.system(f'xdotool type --delay 1 "{text}"')
    
while True:
    data = stream.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        obj = rec.Result()
        obj = json.loads(obj)
        text_to_type = obj['text']
        print(obj)
        if text_to_type is not None and len(text_to_type)>0:
            print(f'send - {text_to_type}')
            send_text_to_active_window(text_to_type)
            # for t in text_to_type:
            #     t_en = tr.get(t,t)
            #     pyautogui.typewrite(t_en)
    else:
        r = rec.PartialResult()
        print(r)
        rj = json.loads(r)
        
        if 'partial' in rj:
            text = rj['partial']
            if len(text)>0:
                print(text)
        pass

print(rec.FinalResult())