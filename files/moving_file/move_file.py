import os
from tqdm import tqdm

from dotenv import load_dotenv
load_dotenv()
base_path = '/media/aleksei/home/video/m_n/'
print(base_path)

files = os.listdir(base_path)

for file in tqdm(files):
    
    filename = os.path.join(base_path,file)

    if os.path.isdir(filename):
        continue

    date = file.split(' ')[0]
    dirname = os.path.join(base_path,date)
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    
    filename_new = os.path.join(dirname, file)
    os.rename(filename,filename_new)