
'''
по заданному пути собираем все пути всех подпапок в указанный файл.
добавляем параметр для чтения архивов и получение путей из этого архива
в таблице будут следующие поля:
- полный путь
- наиенование
- расширение
- размер
- Hash < 2Мб (можно выключить)
- дата
'''

import os
import hashlib
import zipfile
import os
import tarfile


class Header:    
    sep = ','    
    def __init__(self,dirpath = None,filename = None,extention = None,
                 st_size = None,st_atime = None,st_mtime = None,
                 st_ctime = None,hash_val = None,comment = None, type = None):
        self.dirpath = dirpath
        self.filename = filename
        self.extention = extention
        self.st_size = st_size
        self.st_atime = st_atime
        self.st_mtime = st_mtime
        self.st_ctime = st_ctime
        self.hash_val = hash_val
        self.comment = comment
        self.type = type
    @staticmethod
    def get_header():
        return ('dirpath' + Header.sep +
                'filename' + Header.sep +
                'extention' + Header.sep +
                'st_size' + Header.sep +
                'st_atime' + Header.sep +
                'st_mtime' + Header.sep +
                'st_ctime' + Header.sep +
                'hash_val' + Header.sep +
                'type' + Header.sep +
                'comment'
        )
    
    def get_values(self):
        return  (  f'"{self.dirpath if self.dirpath else ""}"'
                + Header.sep
                + f'"{self.filename if self.filename else ""}"'
                + Header.sep
                + f'"{self.extention if self.extention else ""}"'
                + Header.sep
                + str(self.st_size if self.st_size else "")
                + Header.sep
                + str(self.st_atime if self.st_atime else "")
                + Header.sep
                + str(self.st_mtime if self.st_mtime else "")
                + Header.sep
                + str(self.st_ctime if self.st_ctime else "")
                + Header.sep
                + f'"{self.hash_val if self.hash_val else ""}"'
                + Header.sep
                + f'"{self.type if self.type else ""}"'
                + Header.sep
                + f'"{self.comment if self.comment else ""}"'
            )
        


def get_file_names_from_tgz(full_name_tar):
    result = []
    with tarfile.open(full_name_tar, 'r:gz') as tar:
        for member in tar.getmembers():
            #print(member.name)  # Относительное имя файла/директории внутри архива
            filename = member.name
            
            #filename = member.name.encode('latin1').decode('windows-1251')
            #filename = member.name.encode('latin1').decode('cp1251')
            #filename = member.name.encode('utf-8', errors='ignore').decode('latin1')
            
            # Полный путь (от корня архива)
            full_path_in_archive = os.path.normpath(filename)
            result.append(full_path_in_archive)
    return result

def get_file_names_from_zip(full_name_zip):
    result = []
    with zipfile.ZipFile(full_name_zip, 'r') as zipf:
        for info in zipf.infolist():
            
            filename = info.filename
            #filename = info.filename.encode('latin1').decode('windows-1251')
            #filename = info.filename.encode('latin1').decode('cp1251')
            #filename = info.filename.encode('utf-8', errors='ignore').decode('latin1')
            
            full_path = os.path.normpath(filename)
            result.append(full_path)
            #print(f"Имя файла: {full_path}")
    
    return result



def get_hash_file(file):
    BLOCK_SIZE = 65536 # The size of each read from the file
    
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()


def get_full_information(dirpath, filename, sep = ',', max_hash_mb = 200)->Header:
#     st_size − size of file, in bytes.
#     st_atime − time of most recent access.
#     st_mtime − time of most recent content modification.
#     st_ctime − time of most recent metadata change.    
    
    header = Header()
    header.dirpath = dirpath    
    #res = sep.join([f'"{dirpath}"', f'"{filename}"']) 
    header.filename = filename
    #res += sep
    #res += os.path.splitext(filename)[1].lower()
    header.extention = os.path.splitext(filename)[1].lower()
    #res += sep
    
    fullname = os.path.join(dirpath, filename)    
    info = None
    if os.path.isfile(fullname):
        info = os.stat(fullname)
    else:
        header.comment = 'not_exists'
    if info is not None:
        #res += sep.join(str(i) for i in [info.st_size,info.st_atime,info.st_mtime,info.st_ctime])
        header.st_size = info.st_size
        header.st_atime = info.st_atime
        header.st_mtime = info.st_mtime
        header.st_ctime = info.st_ctime
    #else:
    #    res += sep.join(str(i) for i in ['','','',''])
    #res += sep
    #result_hash = ''
    # if info is not None and info.st_size < max_hash_mb*1024*1024:
    #      result_hash = get_hash_file(fullname)
    #res += result_hash
    
    return header

def append_files(file_result,startPath,exclude_folders,global_exclude_folders,sep = '|'):
    counter_files = 0
    counter_dirs = 0
    counter_erorr = 0
    #append files
    #if True:
    print(f'start - {startPath=}')
    with open(file_result,'a') as file:
        for dirpath, dirnames, filenames in os.walk(startPath):
            for dir_name in global_exclude_folders:
                if dir_name in dirnames:
                    dirnames.remove(dir_name)
            #print(dirpath)
            for filename in filenames:            
                full_name = os.path.join(dirpath , filename)
                
                #print(full_name)
                header_line = get_full_information(dirpath, filename, sep)
                
                
                _,ext = os.path.splitext(filename)
                
                if ext.lower() in ['.zip','.tgz']:
                    
                    try:
                        file_names = []
                        if ext.lower() == '.zip':
                            file_names = get_file_names_from_zip(full_name)
                        elif ext.lower() == '.tgz':
                            file_names = get_file_names_from_tgz(full_name)
                            
                        for file_name in file_names:
                            _,ext = os.path.splitext(file_name)
                            filename_new = filename + '<from_archive>' + file_name
                            
                            _header = Header()
                            _header.dirpath = dirpath
                            _header.filename = filename_new
                            _header.extention = ext
                            _header.type='arhive'
                            file.write(_header.get_values() + '\n')
                    except Exception as e:
                        counter_erorr += 1
                        header_line.comment = str(e)
                
                file.write(header_line.get_values()  + '\n')
                
            counter_files += len(filenames)
            counter_dirs += len(dirnames)
    print('done')
    print(f'{counter_files=},{counter_dirs=}, {counter_erorr=}')

def start():
    
    sep = ','
    startPaths = [
        '/media/aleksei/data/',
        '/media/aleksei/home/',
        '/home/aleksei/',
        '/media/aleksei/6a6e8d81-9ecd-488e-baf9-a02ad2489a52/Data/',
        #'/home/aleksei/work/'
    ]
    #startPath = '/media/aleksei/home/MyProject/python/ml/'
    file_result = '/home/aleksei/Downloads/files.csv'
    exclude_folders = [
        # 'timeshift',
        # 'boot',
        # 'SteamLibrary',
        # 'lost+found',
        # '/media/aleksei/home/MyProject/python/ml/analysis_charge',
        # '/media/aleksei/home/MyProject/python/ml/face_embedding',        
    ]
    global_exclude_folders = ['.venv',
                              '.git',
                              'timeshift',
                              'boot',
                              'SteamLibrary',
                              'lost+found',
                              '.vscode',
                              'node_modules',
                              'plugins',
                              'venv',
                              '__pycache__',
                              '.wine',
                              '.ipynb_checkpoints'
                              ]
    
    #/home/aleksei/.cache
    #/home/aleksei/.config

    #is_only_append = True
    #if not is_only_append:
    head = Header.get_header()
    print(head)
    with open(file_result,'w') as file:
        file.write(head + '\n')
    
    for startPath in startPaths:
        append_files(file_result, startPath, exclude_folders, global_exclude_folders,sep=sep)
    
if __name__ == '__main__':
    start()
    # print('*'*100)
    # print(get_file_names_from_zip('/media/aleksei/data/home/Download/Zip/Занятие_9._Компьютерное_зрение.zip'))
    # print('*'*100)
    # print(get_file_names_from_tgz('/media/aleksei/data/home/Download/Zip/REDrocketX-2.1.34.0_Resolve.tgz'))
    # #print(get_file_names_from_zip('/media/aleksei/data/home/Download/Zip/Лекция_14.ipynb.zip'))
    # print('*'*100)