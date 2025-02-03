from tqdm import tqdm
import json
import wave
import sys
import os
import whisper
#pip uninstall whisper
#pip install git+https://github.com/openai/whisper.git
#pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
from dotenv import load_dotenv
load_dotenv()

def recognize_file(model, path):
  print(f'rec from {path=}')
  result = model.transcribe(path,language='ru')
  result_text = result['text']

  result_text = result_text.replace('. ','.\n')

  return result_text

import time
if __name__ == '__main__':
  print('model load...')
  model_name = 'medium' #'large' - not work on 8Gb GPU
  model = whisper.load_model(model_name, device="cuda")
  print('model loaded')

  start = time.time()
  base_path_v = os.getenv('BASE_PATH_VIDEO')
  base_path_t = os.getenv('BASE_PATH_RESULT_TEXT')
  if not os.path.isdir(base_path_t):
    os.mkdir(base_path_t)
  for file_name in tqdm(os.listdir(base_path_v),colour='green'):    
    if not '.mkv' in file_name:
      continue
    # if file_name != '2024-09-03_17-02-22.mkv':
    #   continue
      
    path_v = os.path.join(base_path_v, file_name)
    
    path_out = os.path.join(base_path_t, file_name.replace('.mkv',f'_{model_name}.txt'))

    # if os.path.isfile(path_out):
    #   os.remove(path_out)
    
    if not os.path.isfile(path_out):
      res = recognize_file(model, path_v)
      with open(path_out,'w',encoding='UTF-8') as f:
          f.write(res)
    #break
  end = (time.time() - start)*1000
  print(f'done, {end} ms')

#34 012.63475418091 base cpu
# 1 354.2332649230957 base 
#16 690.029621124268 base cuda
#15 878.006219863892 base cuda

#21 631.630182266235 small cuda
#48 073 medium cuda
