from Xlib import X, display, Xatom
from array import array
from ewmh import EWMH



def unmaximize(window):
    ewmh = EWMH()
    ewmh.setWmState(window, 0, "_NET_WM_STATE_MAXIMIZED_VERT")
    ewmh.setWmState(window, 0, "_NET_WM_STATE_MAXIMIZED_HORZ")
    ewmh.setWmState(window, 2, "_NET_WM_STATE_NORMAL")

def change_position(part_str:str):

    screen_size_w, screen_size_h = map(int,'2560x1080'.split('x'))

    part_1, part_2 = map(int,part_str.split('/'))
    
    width_size = screen_size_w//part_2
    


    # Получаем текущее активное окно
    d = display.Display()
    root = d.screen().root
    window_id = root.get_full_property(d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType).value[0]
    window = d.create_resource_object('window', window_id)

    # Получаем свойство _NET_STATE окна
    net_state = window.get_full_property(d.intern_atom('_NET_WM_STATE'), X.AnyPropertyType)
    #print(net_state)
    unmaximize(window)

    # Получаем идентификаторы атомов для состояния
    #maximized_vert = d.intern_atom('_NET_WM_STATE_MAXIMIZED_VERT')
    #maximized_horz = d.intern_atom('_NET_WM_STATE_MAXIMIZED_HORZ')

    if net_state:
        # Превратим свойства в список
        state_atoms = net_state.value
        
        # Преобразуем массив в обычный список для удобства
        state_atoms_list = list(state_atoms)
        #print(state_atoms_list)

        # Проверяем, максимизировано ли окно
        # if maximized_vert in state_atoms_list and maximized_horz in state_atoms_list:
        #     print("Окно максимизировано, теперь его нужно восстановить.")
        # else:
        #     print("Окно не максимизировано.")

        # Убираем состояние максимизации
        # window.change_property(
        #     d.intern_atom('_NET_WM_STATE'),
        #     Xatom.ATOM,
        #     32,
        #     []  # Убираем максимизацию
        # )
        
        #window = d.create_resource_object('window', window_id)

        # Получаем свойство _NET_STATE окна
        #net_state = window.get_full_property(d.intern_atom('_NET_WM_STATE'), X.AnyPropertyType)
        #print(net_state)
        
        # Добавляем состояние обычного окна
        # window.change_property(
        #     d.intern_atom('_NET_WM_STATE'),
        #     Xatom.ATOM,
        #     32,
        #     [d.intern_atom('_NET_WM_STATE_NORMAL')]
        # )
        
        target_x = (width_size) * (part_1-1) + 10
        target_y = 29
        
        target_width = width_size
        target_height = screen_size_h-target_y - 40

        # Перемещаем и изменяем размер окна
        window.configure(
            x=target_x,
            y=target_y,
            width=target_width,
            height=target_height,
            stack_mode=X.Above
        )

        d.flush()  # Обновляем изменения
        
#change_position('2/3')