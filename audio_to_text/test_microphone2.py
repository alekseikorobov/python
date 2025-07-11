import sounddevice as sd
import whisper
import queue
import time
#import numpy as np

# Загружаем модель Whisper
#model = whisper.load_model("base")
from vosk import Model, KaldiRecognizer
SAMPLE_RATE = 48000

is_only_test=False

model,rec = None, None
if not is_only_test:
    model = Model(model_path='data/vosk-model-ru-0.42')
    rec = KaldiRecognizer(model, SAMPLE_RATE)

# Частота дискретизации

# Очереди для микрофона и динамиков
mic_queue = queue.Queue()
speaker_queue = queue.Queue()

# Callback для записи с микрофона
def mic_callback(indata, frames, time, status):
    if status:
        print(f"Микрофон статус: {status}")
    #mic_queue.put(indata.copy())
    mic_queue.put(bytes(indata))

# Callback для записи с динамиков
def speaker_callback(indata, frames, time, status):
    if status:
        print(f"Динамики статус: {status}")
    #speaker_queue.put(indata.copy())
    speaker_queue.put(bytes(indata))

# Функция обработки аудио и транскрипции
def process_audio():
    print("Начинаем транскрипцию...")
    while True:        
        if not mic_queue.empty():
            mic_data = mic_queue.get()
            if is_only_test:
                print(f'mic_data:{len(mic_data)=},{sum(mic_data)}')
            else:
                if rec.AcceptWaveform(mic_data):
                    rec_val = rec.Result()
                    print(f'mic_data:{rec_val=}')
            
            # mic_audio = np.frombuffer(mic_data, dtype=np.float32)
            # mic_result = model.transcribe(mic_audio, fp16=False)
            # print(f"[Микрофон]: {mic_result['text']}")

        if not speaker_queue.empty():
            speaker_data = speaker_queue.get()
            if is_only_test:
                print(f'speaker_data:{len(speaker_data)=}')
            else:
                if rec.AcceptWaveform(speaker_data):
                    rec_val = rec.Result()
                    print(f'speaker_data:{rec_val=}')
            
            # speaker_audio = np.frombuffer(speaker_data, dtype=np.float32)
            # speaker_result = model.transcribe(speaker_audio, fp16=False)
            # print(f"[Динамики]: {speaker_result['text']}")

# Определяем устройства для микрофона и динамиков
devices = sd.query_devices()
print("Доступные устройства:")
for i, device in enumerate(devices):
    print(f"{i}: {device['name']} {device['max_input_channels']}")

# Введите номера устройств вручную
mic_device = 8    #int(input("Введите номер устройства для микрофона: "))
speaker_device = 0#int(input("Введите номер устройства для динамиков: "))

#device_info = devices[mic_device]
channels = sd.query_devices(mic_device)['max_input_channels']
print(f'{channels=}')
# Запускаем потоки для записи с микрофона и динамиков
try:
    mic_stream = sd.InputStream(device=mic_device,blocksize = 8000*4, channels=channels, dtype="int16",  samplerate=SAMPLE_RATE, callback=mic_callback)
    #speaker_stream = sd.InputStream(device=speaker_device,blocksize = 8000,dtype="int16", channels=1, samplerate=SAMPLE_RATE, callback=speaker_callback)
    
    with mic_stream:#,speaker_stream:
        process_audio()
except KeyboardInterrupt:
    print("Остановлено пользователем.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
