import os
import wave
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import time
from pynput import keyboard  # Для отслеживания клавиш
import re

# Путь к модели
MODEL_PATH = 'data/vosk-model-ru-0.42'  # Укажите путь к распакованной модели
MODEL_PATH = 'data/vosk-model-small-ru-0.22'  # Укажите путь к распакованной модели

# Проверка наличия модели
if not os.path.exists(MODEL_PATH):
    print(f"Модель по пути {MODEL_PATH} не найдена. Скачайте её с https://alphacephei.com/vosk/models")
    exit(1)

# Инициализация модели
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Очередь для записи данных с микрофона
audio_queue = queue.Queue()
# Переменные для отслеживания состояния текста
last_partial_text = ""
last_update_time = time.time()
is_key_pressed = False  # Флаг состояния клавиши


def audio_callback(indata, frames, time, status):
    """Получение данных с микрофона и добавление их в очередь."""
    if status:
        print(status)
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

def recognize_command(text_command):
    global is_key_pressed    
    if re.match('(открой|открыть|запустить|запусти|запускай) (гугл)',text_command):
        play_text_sound('открываю')
        os.system('google-chrome google.ru')
        return True
    
    if re.match('(открой|открыть|запустить|запусти|запускай) (почту|ящик)',text_command):
        play_text_sound('открываю')
        os.system('google-chrome e.mail.ru')
        return True
    
    if re.match('(открой|открыть|запустить|запусти|запускай) (дион)',text_command):
        play_text_sound('открываю')
        os.system('google-chrome https://dion.vc/')
        return True
    
    if re.match('((открой|открыть|запустить|запусти|запускай) |)(телегу|телега|телеграмм|телеграм)', text_command):
        play_text_sound('открываю')
        os.system('telegram-desktop &')
        return True
        
    if re.match('(открой|открыть|запустить|запусти|запускай) (заметки|заметку)',text_command):
        play_text_sound('вот тебе заметки')
        os.system('open "obsidian://open?vault=work&file=Weekly%2F2025%2FWeek%2004"')
        return True
    
    if re.match('(открой|открыть|запустить|запусти|запускай) (питон|пайтон)',text_command):
        play_text_sound('вот тебе питон')
        os.system('konsole -e python &')
        return True
    
    if re.match('(открой|открыть|запустить|запусти|запускай) (консоль|терминал)',text_command):
        play_text_sound('открываю')
        os.system('konsole &')
        return True
    
    
    if text_command == 'слушай меня':
        play_text_sound('говори текст я ввиду')
        is_key_pressed = True
        return True
    
    
    if text_command == 'ты тут':
        play_text_sound('да говори')
        return True
    return False

def recognize_and_type():
    """Распознавание речи и отправка текста в активное окно."""
    
    global last_partial_text, last_update_time, my_queue_words
    
    # Настройка микрофона
    with sd.RawInputStream(samplerate=16000, blocksize=16000, dtype="int16",
                           channels=1, callback=audio_callback):
        print("Говорите что-нибудь...")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                # Распознаем текст
                result = recognizer.Result()
                text = eval(result)["text"]  # Получаем распознанный текст
                #print(f"Распознанный текст: {text}")
                
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
                
                # print(f"Промежуточный текст: {partial_text}")
                
                
                # Удаляем повторяющиеся слова
                filtered_text = remove_repeated_words(partial_text_new)
                filtered_text = filtered_text.strip()
                if filtered_text == '':
                    continue
                print(f"Промежуточный текст: {filtered_text}")
                is_command = recognize_command(filtered_text)
                if is_command:
                    continue
                                
                # Проверяем изменения текста
                if filtered_text and filtered_text != last_partial_text:
                    current_time = time.time()

                    # Добавляем временной фильтр: выводим текст не чаще 0.5 секунд
                    if current_time - last_update_time > 0.5 and len(filtered_text) > 0:
                        
                        if is_key_pressed:
                            os.system(f'xdotool type --delay 10 "{filtered_text} "')
                            last_partial_text = filtered_text
                            last_update_time = current_time
                
# def on_press(key):
#     """Обработчик нажатия клавиши."""
#     global is_key_pressed
#     try:
#         # Нажатие определённой клавиши, например, 'shift'
#         if key == keyboard.Key.scroll_lock:
#             is_key_pressed = True
#             print("Клавиша shift нажата. Распознавание включено.")
#     except Exception as e:
#         print(f"Ошибка в on_press: {e}")

def change_cursor_color(enable):
    """Меняет курсор в зависимости от состояния is_key_pressed."""
    if enable:
        # Меняем курсор на красный (например, на "watch")
        os.system("xsetroot -cursor_name watch")
    else:
        # Возвращаем курсор к стандартному
        os.system("xsetroot -cursor_name left_ptr")
        
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
            print(f"{is_key_pressed=}")
    except Exception as e:
        print(f"Ошибка в on_release: {e}")

import pyttsx3
from text_to_speech import play_text_sound
if __name__ == "__main__":
    #engine = pyttsx3.init()
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', 125)
    text = "Привет, я твой голосовой помошник. Если что-то нужно обращайся"

    play_text_sound(text)
    # Воспроизведение текста
    #engine.say(text)
    #engine.say("Hello World!")

    # Ожидание завершения воспроизведения
    #engine.runAndWait()
    
    try:
        listener = keyboard.Listener(on_release=on_release)
        listener.start()
        
        recognize_and_type()
    except KeyboardInterrupt:
        print("\nПрограмма остановлена.")
