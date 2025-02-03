

import speech_recognition as sr
import warnings
warnings.filterwarnings("ignore")
from transformers import pipeline

class MicSpeech:
    
    def __init__(self, model_name, device, language = 'russian'):
        # Инициализация слушителя
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 100/2  # Уменьшаем порог для лучшей чувствительности
        self.recognizer.dynamic_energy_threshold = False  # Отключаем автонастройку
        self.recognizer.pause_threshold = 0.2  # Уменьшаем паузу перед обработкой
        self.recognizer.non_speaking_duration = 0.2  # Минимальная пауза между словами
        
        #модель
        self.whisper = pipeline("automatic-speech-recognition",
                                model= model_name, 
                   generate_kwargs={"task": "transcribe",
                                    'language':language,
                                    # 'suppress_tokens':"",
                                    # 'beam_size':5,
                                    # 'vad_filter':True,
                                    # 'vad_parameters':dict(min_silence_duration_ms=1000)
                                    }, device=device)
    
    def start_listening(self,callback=None):
        with sr.Microphone() as source:
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
                    data = audio.get_wav_data(convert_rate=16000)
                    result = self.whisper(data)
                    if callback is not None:
                        #print("Распознанный текст:", result["text"])
                        callback(result["text"])
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
    