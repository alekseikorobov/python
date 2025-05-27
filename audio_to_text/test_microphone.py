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
import sys

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
device_index = 7
device_info = p.get_device_info_by_index(device_index) if device_index is not None else p.get_default_input_device_info()
print()
print(device_info)

stream = p.open(format=pyaudio.paInt32, channels=1, rate=48000, input=True, frames_per_buffer=1000,input_device_index=7)
stream.start_stream()

#sys.exit(0)

# #model = Model("model-en")

# model = Model(model_path='data/vosk-model-ru-0.42')
# rec = KaldiRecognizer(model, 16000)

# qwerty = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
# ycuken = "йцукенгшщзхъфывапролджэячсмитьбюё"
# tr = dict(zip(ycuken, qwerty))

# def send_text_to_active_window(text):
#     # Эмулируем ввод текста
#     os.system(f'xdotool type --delay 1 "{text}"')
import time
while True:
    data = stream.read(1000)
    if len(data) == 0:
        break

    time.sleep(1)
    print(len(data))
    

print('done')
#print(rec.FinalResult())