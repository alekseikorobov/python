

#%%
import svg
#%%
import xml.etree.ElementTree as ET

ET.register_namespace("","http://www.w3.org/2000/svg")
svg_file = 'old2.svg'
ns="http://www.w3.org/2000/svg"
tree = ET.parse(svg_file)
root = tree.getroot()

list_g = root.findall('{http://www.w3.org/2000/svg}g')
g_root = list_g[0]
list_g = g_root.findall('{http://www.w3.org/2000/svg}g')
len(list_g)

for i,g in enumerate(list_g):
    paths_in_g = g.findall('{http://www.w3.org/2000/svg}path')
    print(f'{i} - {len(paths_in_g)}')
    # Если в <g> есть пути <path>, объединяем их
    combined_path = ''
    for i1,path in enumerate(paths_in_g):
        path_data = path.attrib['d']
        if i1 != 0:
            path_data = path_data.replace('M','L')
        combined_path += ' ' + path_data

        # Удаляем оригинальный <g> элемент
        g.remove(path)
    
    new_path_element = ET.Element('{http://www.w3.org/2000/svg}path', {
        'd': combined_path.strip(),
        'fill': 'none',  # Укажите цвет заливки
        'stroke': 'black'  # Укажите цвет обводки
    })
    g.append(new_path_element)

tree.write('merged_output.svg')