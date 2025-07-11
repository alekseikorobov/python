

import subprocess
import os
from tqdm import tqdm

base_folder = os.getenv('BASE_PATH_VIDEO_FROM_CONVERT')
target_folder = os.getenv('BASE_PATH_VIDEO_TO_CONVERT')

for file_name in tqdm(os.listdir(base_folder)):
    source_file = os.path.join(base_folder,file_name)
    target_file = os.path.join(target_folder,file_name)
    
    if not os.path.isfile(target_file):
        print(f'start convert from {source_file}')
        cmd = f'ffmpeg -i "{source_file}" -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov "{target_file}"'
        #subprocess.run(cmd)
        os.system(cmd)
    
    
print('done')