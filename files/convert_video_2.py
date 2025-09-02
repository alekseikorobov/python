

import subprocess
import os
from tqdm import tqdm

base_folder = os.getenv('BASE_PATH_VIDEO_FROM_CONVERT')
target_folder = base_folder
#print(os.listdir(base_folder))
for file_name in tqdm(os.listdir(base_folder)):
    source_folder = os.path.join(base_folder,file_name)    

    source_files = os.listdir(source_folder)
    if len(source_files) == 2:
        continue

    source_file = os.path.join(source_folder,source_files[0])

    target_file = source_file

    source_file = os.path.splitext(source_file)
    source_file = source_file[0] + '_src' +source_file[1]
    os.rename(target_file, source_file)
        
    print(f'start convert from {source_file}')
    cmd = f'ffmpeg -i "{source_file}" -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov "{target_file}"'
           #ffmpeg -i ""              -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov ""
    #subprocess.run(cmd)
    os.system(cmd)
    #break
    
    
# print('done')