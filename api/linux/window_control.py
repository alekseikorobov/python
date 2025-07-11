from pynput import keyboard

import window_state 

# # Определите функции для обработки нажатий клавиш
# def on_activate():
#     print("Комбинация клавиш Win+1 была нажата!")

# def for_canonical(f):
#     return lambda k: f(l.canonical(k))

# # Определите комбинацию клавиш
# hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<cmd>+1'), on_activate)

# # Создайте слушатель
# with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
#     l.join()



def on_change_position_1_4(): window_state.change_position('1/4')
def on_change_position_2_4(): window_state.change_position('2/4')
def on_change_position_3_4(): window_state.change_position('3/4')
def on_change_position_4_4(): window_state.change_position('4/4')

def on_change_position_1_3(): window_state.change_position('1/3')
def on_change_position_2_3(): window_state.change_position('2/3')
def on_change_position_3_3(): window_state.change_position('3/3')


with keyboard.GlobalHotKeys({
        '<ctrl>+<cmd>+1': on_change_position_1_4,
        '<ctrl>+<cmd>+2': on_change_position_2_4,
        '<ctrl>+<cmd>+3': on_change_position_3_4,
        '<ctrl>+<cmd>+4': on_change_position_4_4,

        '<ctrl>+<cmd>+5': on_change_position_1_3,
        '<ctrl>+<cmd>+6': on_change_position_2_3,
        '<ctrl>+<cmd>+7': on_change_position_3_3,

        }) as h:
    h.join()