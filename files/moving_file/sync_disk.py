# цель сортировать файлы на внешнем жестком диске, привести к такому же виду как на яндекс диске

# проходимся по всем файлам яндекса
# если файл существует, то переносим его в папку такую же как на яндекс
# если файл не существует копируем новый

import os
import shutil
from paths import *


old_file_dict = {}
for root,dirs,files in os.walk(path_to):
    for file in files:
        full_name = os.path.join(root,file)
        if file not in old_file_dict:
            old_file_dict[file] = full_name
        else:
            print(f'duplicate name {file}, {old_file_dict[file].replace(path_to,"")}, {full_name.replace(path_to,"")}')

print(len(old_file_dict))

for root,dirs,files in os.walk(path_from_test):
    for file in files:
        full_name = os.path.join(root,file)
        r_path = full_name.replace(path_from,'')
        
        new_full_name = os.path.join(path_to,r_path)
        full_new_dir = os.path.dirname(new_full_name)
        if not os.path.isdir(full_new_dir):
            print('create dirs ', full_new_dir)
            os.makedirs(full_new_dir)
        if not os.path.isfile(new_full_name):        
            if file in old_file_dict:                
                print('move',old_file_dict[file], '->',new_full_name)                
                shutil.move(old_file_dict[file], new_full_name)
            else:
                print('copy',full_name, '->',new_full_name)
                shutil.copy(full_name,new_full_name)



for root,dirs,files in os.walk(path_to):
    if len(files) == 0 and len(dirs) == 0:
        os.rmdir(root)  