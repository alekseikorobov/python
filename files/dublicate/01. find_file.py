#  ## Сбор файлов Yandex Disk
#     Сначала мы соберем все файлы в один **csv** файл
#     
#     в таблице будут следующие поля:
#     - полный путь
#     - наименование
#     - Hash < 200Мб
#     - 

import os;
import hashlib

def get_hash_file(file):
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()


def get_full_information(dirpath, filename, sep = ',', max_hash_mb = 200):
    #     st_size − size of file, in bytes.
    #     st_atime − time of most recent access.
    #     st_mtime − time of most recent content modification.
    #     st_ctime − time of most recent metadata change.    
    fullname = os.path.join(dirpath, filename)    
    info = os.stat(fullname)
    res = sep.join([f'"{dirpath}"', f'"{filename}"']) 
    # res += sep
    # res += os.path.splitext(filename)[1].lower()
    # res += sep
    # res += sep.join(str(i) for i in [info.st_size,info.st_atime,info.st_mtime,info.st_ctime])
    res += sep
    if(info.st_size < max_hash_mb*1024*1024):
            res += get_hash_file(fullname)
    return res


def append_files(file_result,startPath,ignored_folders,sep = '|'):
        print(f'Start by {startPath}')
        counter_files = 0
        counter_dirs = 0
        #append files
        with open(file_result,'a') as file:
            for dirpath, dirnames, filenames in os.walk(startPath):
                is_skip_folder = False
                for name in dirnames:
                    if name in ignored_folders:
                        is_skip_folder = True
                
                if is_skip_folder:
                    continue
                        
                for filename in filenames:
                    line_string = get_full_information(dirpath, filename, sep)
                    file.write(line_string + '\n')
                    print(f'write {filename}')
                counter_files += len(filenames)
                counter_dirs += len(dirnames)
                print(f'{counter_files=}, {counter_dirs=}')
        print('done')
        print('counter_files',counter_files,'counter_dirs',counter_dirs)


startPath = '/media/aleksei/data/nastya/cloud/yandex/'
file_result = '/media/aleksei/data/nastya/cloud/files_20230801.csv'
ignored_folders = ['.sync']
append_files(file_result, startPath,ignored_folders)