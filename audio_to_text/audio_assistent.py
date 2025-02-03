import os
import wave
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import time
from pynput import keyboard  # Для отслеживания клавиш
import re
import subprocess
from threading import Thread
import logging
from datetime import datetime
from MicSpeech import MicSpeech
from whisper.normalizers.basic import BasicTextNormalizer
import json
import random
from text_to_speech import play_text_sound
#слежение за изменением файлов:
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

log_folder = 'log' #папка с логами

if not os.path.isdir(log_folder):    
    os.mkdir(log_folder)

logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(
                filename=f'{log_folder}/log_{datetime.now():%Y%m%d}.log', #_%H%M%S
                encoding='UTF8',
            ),
            logging.StreamHandler()
        ],
        format="%(asctime)s\t%(filename)s\t%(funcName)s\t[%(levelname)s]\t%(lineno)d\t%(message)s",
)

logging.debug('START')

from test_llm_model import qa_dialog
def run_process(cmd:str):
    '''запуск команды через сабпроцесс
    '''
    try:
        #logging.info('run thread')
        #os.spawnl(os.det, 'some_long_running_command')
        #Thread(target=lambda: subprocess.Popen(cmd + ' &', shell=True),daemon=True).run()
        logging.debug(f'{cmd=}')
        subprocess.Popen('nohup '+ cmd + ' &', shell=True )
    except Exception as ex:
        logging.error('',exc_info=True)        
        
def get_recognizer():
    # Путь к модели
    #с больше моделью  качества лучше но при этом идёт долгий процесс обработки что значительно увеличивает время на  ответ 
    #MODEL_PATH = 'data/vosk-model-ru-0.42'
    # поэтому используется более легковесная  модель для быстроты распознавания звука 
    MODEL_PATH = 'data/vosk-model-small-ru-0.22' 

    # if __name__ == "__main__":
    #     #os.spawnl(os.P_DETACH, 'some_long_running_command')
    #     run_process('konsole')
    #     exit(1)
    # Проверка наличия модели
    if not os.path.exists(MODEL_PATH):
        msg = f"Модель по пути {MODEL_PATH} не найдена. Скачайте её с https://alphacephei.com/vosk/models"
        logging.error(msg)
        exit(1)

    # Инициализация модели
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)
    return recognizer

# Очередь для записи данных с микрофона
audio_queue = queue.Queue()
# Переменные для отслеживания состояния текста
last_partial_text = ""
last_update_time = time.time()
is_key_pressed = False  # Флаг состояния клавиши


def audio_callback(indata, frames, time, status):
    """Получение данных с микрофона и добавление их в очередь."""
    if status:
        logging.info(status)
    audio_queue.put(bytes(indata))
    
def remove_repeated_words(text):
    """Удаляет повторяющиеся слова в тексте."""
    words = text.split()
    filtered_words = []
    for word in words:
        if not filtered_words or word != filtered_words[-1]:
            filtered_words.append(word)
    return " ".join(filtered_words)

my_queue_words = queue.Queue()
my_queue_words_l = []
is_dialog_with_llm = False
is_command = False
text_normalizer = BasicTextNormalizer()
FILE_NAME_COMMAND='commands.json'
command_list = []

def inti_command_list():
    global command_list
    logging.info('init command')
    with open(FILE_NAME_COMMAND,'r') as f:
        obj = json.load(f)
        if 'commands' in obj:
            command_list = obj['commands']
            logging.info(f'{len(command_list)=}')
    


def recognize_command(text_command):
    '''
    распознавания команд из текста 
    '''
    global is_key_pressed,is_dialog_with_llm,is_command
    text_command = text_normalizer(text_command).strip()
    #print(f'{text_command=}')
    is_command = False
    
    for command in command_list:
        if re.match(command['pattern_rx'],text_command):
            is_command = True
            response_speek = random.choice(command['response_speeks'])
            play_text_sound(response_speek)
            #os.system('google-chrome google.ru')
            run_process(command['cmd'])
            break
        
    m = re.match('за( |)гугл(е|и|я) (.*)',text_command)
    if m:
        is_command = True
        gs = m.groups()
        if len(gs)>2:
            text = gs[2]
            text = text.strip()
            if len(text)>3:
                play_text_sound('открываю')
                text = text.replace(' ','+')
                #os.system('google-chrome google.ru')
                run_process(f'google-chrome https://www.google.com/search?q={text}')
                
    if re.match('((режим|открой|открыть|запустить|запусти|запускай) |)(диалог|диалога)',text_command):
        is_command = True
        play_text_sound('режим диалога')
        is_dialog_with_llm = True
        is_key_pressed = False
        
    if re.match('(закрыть|выйти из|) (диалог|диалога)',text_command):
        is_command = True
        play_text_sound('вышли из диалога')
        is_dialog_with_llm = False

    if text_command == 'слушай меня':
        is_command = True
        play_text_sound('говори текст я ввиду')
        is_key_pressed = True

    if text_command == 'ты тут':
        is_command = True
        play_text_sound('да говори')
        
def input_text_to_current_window(filtered_text:str):
    '''
    ввод текста в активное окна 
    '''
    space_last = ' '
    filtered_text = filtered_text.strip(' ')
    os.system(f'xdotool type --delay 10 "{filtered_text}{space_last}"')    
    
from fix_text import fix_text
def recognize_and_type_new():
    ms = MicSpeech(model_name='openai/whisper-large-v3-turbo',#small/large/turbo
                   device='cuda')    
    ms.start_listening(callback_text)
    
def callback_text(text):
    #global last_partial_text, last_update_time, my_queue_words
    
    logging.info(f'{text=}')
    
    recognize_command(text)
    if is_command:
        return
    
    if is_key_pressed:
        input_text_to_current_window(text)

def recognize_and_type():
    """Распознавание речи
       используется для распознавания команд
       в случае если указан флаг вода текста тогда отправляется текстов активное окно       
    """
    
    global last_partial_text, last_update_time, my_queue_words
    recognizer = get_recognizer()
    # Настройка микрофона
    with sd.RawInputStream(samplerate=16000, blocksize=16000, dtype="int16",
                           channels=1, callback=audio_callback):
        logging.info("Говорите что-нибудь...")
        
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                # Распознаем текст
                result = recognizer.Result()
                text = eval(result)["text"]  # Получаем распознанный текст
                if len(text)>0:
                    logging.info(f'{text=}')
                
                if not is_command:
                    recognize_command(text)
                    if is_command:
                        continue
                    
                if is_dialog_with_llm:
                    if len(text)>0:
                        answe = qa_dialog(text)
                        play_text_sound(answe)
                        continue
                
                if is_key_pressed:
                    if len(my_queue_words_l) > 0:
                        last_text = ' '.join(my_queue_words_l)
                        ost_text = fix_text(last_text,text)
                        if ost_text != '':
                            # если присутствует остаток текста которой не ввели, и он присутствует в финальном тексте 
                            input_text_to_current_window(ost_text)
                        logging.info(f'{last_text=},{ost_text=}')
                    elif len(text)>0:
                        #это случилось случае когда промежуточного текста не было 
                        #и был только основной текст, чтобы не пропустить сказанное 
                        input_text_to_current_window(text)                    
                
                #logging.info(f"Распознанный текст: {text}")
                
                #my_queue_words = queue.Queue()
                with my_queue_words.mutex:
                    my_queue_words.queue.clear()
                    
                my_queue_words_l.clear()

                # if text.strip():  # Если текст не пустой
                #     # Отправляем текст в активное окно через xdotool
                #     os.system(f'xdotool type --delay 50 "{text}"')
            else:
                partial_result = recognizer.PartialResult()
                partial_text = eval(partial_result)["partial"]
                partial_texts = partial_text.split()
                
                partial_text_new = ''
                for word in partial_texts:
                    if word not in my_queue_words_l:
                        my_queue_words_l.append(word)
                        partial_text_new += word + ' '
                
                # logging.info(f"Промежуточный текст: {partial_text}")
                
                
                # Удаляем повторяющиеся слова
                #filtered_text = remove_repeated_words(partial_text_new)
                filtered_text = partial_text_new.strip()
                if filtered_text == '':
                    continue
                logging.info(f"Промежуточный текст: {filtered_text}")
                
                recognize_command(filtered_text)
                if is_command:
                    continue
                                
                # Проверяем изменения текста
                if filtered_text and filtered_text != last_partial_text:
                    current_time = time.time()

                    # Добавляем временной фильтр: выводим текст не чаще 0.5 секунд
                    if current_time - last_update_time > 0.5 and len(filtered_text) > 0:
                        
                        if is_key_pressed:
                            input_text_to_current_window(filtered_text)
                            last_partial_text = filtered_text
                            last_update_time = current_time
                
# def on_press(key):
#     """Обработчик нажатия клавиши."""
#     global is_key_pressed
#     try:
#         # Нажатие определённой клавиши, например, 'shift'
#         if key == keyboard.Key.scroll_lock:
#             is_key_pressed = True
#             logging.info("Клавиша shift нажата. Распознавание включено.")
#     except Exception as e:
#         logging.info(f"Ошибка в on_press: {e}")

# смена курсора на данный момент не  работает 
# def change_cursor_color(enable):
#     """Меняет курсор в зависимости от состояния is_key_pressed."""
#     if enable:
#         # Меняем курсор на красный (например, на "watch")
#         os.system("xsetroot -cursor_name watch")
#     else:
#         # Возвращаем курсор к стандартному
#         os.system("xsetroot -cursor_name left_ptr")
        
def on_release(key):
    """Обработчик отпускания клавиши."""
    global is_key_pressed
    try:
        # Отпускание клавиши 'Ctrl'
        if key == keyboard.Key.scroll_lock:
            is_key_pressed = not is_key_pressed
            if is_key_pressed:
                play_text_sound('говори текст я ввиду')
            else:
                play_text_sound('больше не ввожу текст')
            logging.info(f"{is_key_pressed=}")
    except Exception as e:
        logging.error(f"Ошибка в on_release: {e}",exc_info=True)


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self,callback):
        self.callback = callback
        super().__init__()

    def on_modified(self, event):
        #print(f"File '{event.src_path}' has been modified.")
        self.callback()

observer = Observer()
def file_wather():
    handler = FileChangeHandler(inti_command_list)
    observer.schedule(handler, FILE_NAME_COMMAND, recursive=True)
    observer.start()


if __name__ == "__main__":
    #engine = pyttsx3.init()
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', 125)
    texts = [
        "Привет, я твой голосовой помошник. Если что-то нужно обращайся",
        "Привет",
        "Привет. Я запущен",
        ]
    text = random.choice(texts)

    play_text_sound(text)
    # Воспроизведение текста
    #engine.say(text)
    #engine.say("Hello World!")

    # Ожидание завершения воспроизведения
    #engine.runAndWait()
    
    try:
        listener = keyboard.Listener(on_release=on_release)
        listener.start()
        
        inti_command_list()
        
        file_wather()
        
        recognize_and_type_new()
    except KeyboardInterrupt:
        observer.stop()
        logging.info("\nПрограмма остановлена.")
    observer.join()
