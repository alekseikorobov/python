import os

def deleteFile(path):
    if(os.path.isfile(path)): #or os.path.isfile(‘file’)
        os.remove(path)
        return True
    else:
        print(path + ' not exists')
        return False


with open('on_delete_20210804.txt') as f:
    lines = f.readlines()
    print('All rows - ' + str(len(lines)))
    deleted = 0
    for l in lines:
        s = l.replace('\n','')
        if(deleteFile(s)):
            deleted = deleted + 1
    print('Deleted files - ' + str(deleted))

print('done')