import os;
import hashlib

#скрипт который сравнивает две папки и находит дубликаты
#

folder1 = '/home/aleksei/cloud/yandex_offline/iCloud Photos/'
folder2 = '/home/aleksei/cloud/yandex/Pictures/photo/Насти/DCIM/'
dictfile = {}



def get_hash_file(file):
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()


def get_list_with_hash(dictfile, startPath):
    list_files = []
    counter_files = 0
    counter_dirs = 0
    for dirpath, dirnames, filenames in os.walk(startPath):
        for filename in filenames:            
            fullname = os.path.join(dirpath, filename)
            
            hash = get_hash_file(fullname)
            if hash in dictfile:
                dictfile[hash].append(fullname)
                #break;
            else:
                dictfile[hash] = [fullname]
        counter_files += len(filenames)
        counter_dirs += len(dirnames)
    print('done')
    print('counter_files',counter_files,'counter_dirs',counter_dirs)


get_list_with_hash(dictfile, folder1)
get_list_with_hash(dictfile, folder2)

list_result = []
for key in dictfile:
    if len(dictfile[key])>1:
        for l in dictfile[key]:
            list_result.append(l)
print(len(list_result))