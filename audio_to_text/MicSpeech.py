

import speech_recognition as sr
import warnings
warnings.filterwarnings("ignore")
from transformers import pipeline
import numpy as np
import whisperx

class MicSpeech:
    
    def __init__(self, model_name, device, language = 'russian',device_index = 7):
        # Инициализация слушителя
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 100/2  # Уменьшаем порог для лучшей чувствительности
        self.recognizer.dynamic_energy_threshold = False  # Отключаем автонастройку
        self.recognizer.pause_threshold = 0.2  # Уменьшаем паузу перед обработкой
        self.recognizer.non_speaking_duration = 0.2  # Минимальная пауза между словами
        self.batch_size = 5
        self.device_index = device_index
        self.version = 'v1' #use v1=whisperx, v2=whisperx
        
        #модель
        if self.version == 'v1':
            self.whisper = pipeline("automatic-speech-recognition",
                                    model= model_name, 
                       generate_kwargs={"task": "transcribe",
                                        'language':language,
                                        # 'suppress_tokens':"",
                                        # 'beam_size':5,
                                        # 'vad_filter':True,
                                        # 'vad_parameters':dict(min_silence_duration_ms=1000)
                                        }, device=device)
        else:
            compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)
            self.whisper = whisperx.load_model("large-v2", device, compute_type=compute_type)
    
    def start_listening(self,callback=None):
        with sr.Microphone(self.device_index) as source:
            print("Настройка микрофона...")
            # Автоматическая настройка уровня шума
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Микрофон настроен. Слушаю...")
                    #print("Скажите что-нибудь...")
                    
            # stop_listening = recognizer.listen_in_background(mic, callback,phrase_time_limit=1)

            # try:
            #     while True:
            #         pass  # Основной поток продолжает работать (можно заменить на другую логику)
            # except KeyboardInterrupt:
            #     stop_listening(wait_for_stop=False)  # Останавливаем прослушивание при выходе
            #     print("Программа завершена.")

            while True:
                try:
                    try:
                        audio = self.recognizer.listen(source) #timeout=5.0, phrase_time_limit=1.0 timeout=3, phrase_time_limit=2
                    except sr.exceptions.WaitTimeoutError:
                        continue
                    
                    #for audio in recognizer.listen(source,stream=True):
                        # Запись аудио с микрофона
                        #audio = recognizer.listen(source,stream=True) #timeout=5.0, phrase_time_limit=1.0

                        # Попытка распознать речь с помощью Google Web Speech API
                        #text = recognizer.recognize_google(audio, language="ru-RU")
                    #print(f"Вы сказали: {type(audio)=}")
                    
                    if self.version == 'v1':
                        data = audio.get_wav_data(convert_rate=16000)
                        result = self.whisper(data)
                        if callback is not None:
                            #print("Распознанный текст:", result["text"])
                            callback(result["text"])
                    else:
                        # Преобразование AudioData в numpy.ndarray
                        #audio_bytes = audio.get_raw_data()  # Получаем сырые байты
                        #audio_array = np.frombuffer(audio_bytes, dtype=np.float32)  # Преобразуем в массив int16

                        # Если нужно нормализовать в диапазон [-1.0, 1.0]
                        #audio_array_normalized = audio_array.astype(np.float32) / 32768.0  # Для 16-битного звука
                        data = audio.get_wav_data(convert_rate=16000)
                        result = self.whisper.model.model(data)
                        print(result)

                        # result = self.whisper.transcribe(audio_array, batch_size=self.batch_size)
                        print(result) # before alignment
                        # if callback is not None:
                        #     #print("Распознанный текст:", result["text"])
                        #     callback(result["segments"])

                except sr.UnknownValueError:
                    # Если речь не распознана
                    raise(Exception("Речь не распознана. Пожалуйста, повторите."))
                except sr.RequestError as e:
                    # Если возникла ошибка при запросе к API
                    raise(Exception(f"Ошибка сервиса распознавания речи; {e}"))
                # except KeyboardInterrupt:
                #     # Выход по Ctrl+C
                #     print("Остановка...")
                #     break
    

def callback(text):
    print(text)

if __name__ == '__main__':
    
    model_name = 'openai/whisper-large-v3-turbo' #small/large/turbo
    device = 'cuda'
    
    ms = MicSpeech(model_name, device)
    try:
        ms.start_listening(callback)
    except KeyboardInterrupt:
        print('программа остановлена')
    