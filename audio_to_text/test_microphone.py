from vosk import Model, KaldiRecognizer
import os

# if not os.path.exists("model-en"):
#     print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model' in the current folder.")
#     exit (1)

import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

#model = Model("model-en")

model = Model(model_path='data/vosk-model-ru-0.10')
rec = KaldiRecognizer(model, 16000)

while True:
    data = stream.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        #print(rec.PartialResult())
        r = rec.PartialResult()
        rj = json.loads(r)
        
        if 'partial' in rj:
            text = rj['partial']
            if len(text)>0:
                print(text)

print(rec.FinalResult())