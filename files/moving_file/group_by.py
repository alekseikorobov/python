
# скрипт для группировки фоток в папки, которые нужно разобрать
# работает так
# 1. на вход из буфера должен получить список путей 
# 2. взять перый и последний файл в этой папке (с сортировкой по названию)
# 3. в папке от первого файла создать новую папку с первым и последним наименованием файла
# 4. переместить все файлы в эту папку

# python /home/aleksei/MyProject/python/files/moving_file/group_by.py

import clipboard
text = clipboard.paste()
from urllib.parse import unquote
import logging
import os


logs_path = f'./log.txt'

logging.basicConfig(
    level='DEBUG',
    format="%(asctime)s\t%(filename)s\t[%(levelname)s]\t%(lineno)d\t%(message)s",
    handlers=[
        logging.FileHandler(logs_path, encoding='utf-8'),
        logging.StreamHandler()
    ]    
)

#logging.debug('debug')


DEBUG_MOD = False

print(f'{text=}')



path_list = [unquote(t.replace('file://','')) for t in text.splitlines()]
logging.debug(f'get files {path_list}')
logging.debug(f'{DEBUG_MOD=}')




file_list = sorted([os.path.splitext(os.path.basename(f))[0] for f in path_list])

first_name,last_name = file_list[0],file_list[-1]

new_folder_name = f'group_{first_name}___{last_name}'


print(f'basename',os.path.basename(path_list[0]))
print(f'dirname',os.path.dirname(path_list[0]))

new_path_name = os.path.join(os.path.dirname(path_list[0]),new_folder_name)

if not os.path.isdir(new_path_name):
    if not DEBUG_MOD:
        os.mkdir(new_path_name)
    logging.debug(f'create {new_path_name=}')
else:
    logging.debug(f'already exists folder {new_path_name=}')

for old_path in path_list:
    
    file_name  = os.path.basename(old_path)
    
    new_path = os.path.join(new_path_name,file_name)
    
    exists_old_file = os.path.isfile(old_path)
    exists_new_file = os.path.isfile(new_path)
    
    if exists_old_file and not exists_new_file:
        if not DEBUG_MOD:
            os.rename(old_path, new_path)
        logging.debug(f'file move {old_path=} ---> {new_path=}')
    elif not exists_old_file and exists_new_file:
        logging.debug(f'file already moved {old_path=} ---> {new_path=}')
    elif not exists_old_file and not exists_new_file:
        logging.error(f'files not exists {old_path=} and {new_path=}')
    elif exists_old_file and exists_new_file:
        logging.debug(f'exists doublicate file {old_path=} and {new_path=}')
    
logging.debug('done')
