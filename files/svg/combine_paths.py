#pip install svgpathtools
# скрипт в указанном файле объединяет пути в один
#%%
svg_file = 'old2.svg'

import xml.etree.ElementTree as ET
from svgpathtools import Path, parse_path, wsvg

#%%

# Функция для объединения путей из тегов <g>
#def merge_paths_from_g(svg_file):
    # Парсим SVG файл
tree = ET.parse(svg_file)
root = tree.getroot()

#%%
list_g = root.findall('{http://www.w3.org/2000/svg}g')
g_root = list_g[0]
list_g = g_root.findall('{http://www.w3.org/2000/svg}g')
len(list_g)
#%%

# Создаем новый путь для объединенных путей
combined_path = ''

# Ищем все теги <g>
for i,g in enumerate(list_g):
    paths_in_g = g.findall('{http://www.w3.org/2000/svg}path')
    print(f'{i} - {len(paths_in_g)}')
    # Если в <g> есть пути <path>, объединяем их
    for i1,path in enumerate(paths_in_g):
        path_data = path.attrib['d']
        if i1 != 0:
            path_data = path_data.replace('M','L')
        combined_path += ' ' + path_data

    # Удаляем оригинальный <g> элемент
    g_root.remove(g)

# Добавляем объединенный путь в корень SVG
new_path_element = ET.Element('{http://www.w3.org/2000/svg}path', {
    'd': combined_path.strip(),
    'fill': 'none',  # Укажите цвет заливки
    'stroke': 'black'  # Укажите цвет обводки
})
g_root.append(new_path_element)

# Сохраняем измененный SVG файл
tree.write('merged_output.svg')

# Использование функции
#merge_paths_from_g(file_path)

