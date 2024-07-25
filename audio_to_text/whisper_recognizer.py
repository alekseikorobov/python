from tqdm import tqdm
import json
import wave
import sys

from vosk import Model, KaldiRecognizer

import moviepy
import moviepy.editor as ed


def recognize_file(model, path):
  print(f'rec from {path=}')
  result = model.transcribe(path,language='ru')
  result_text = result['text']

  result_text = result_text.replace('. ','.\n')

  return result_text

import os
import whisper
if __name__ == '__main__':
  print('model load...')
  model = whisper.load_model("base")
  print('model loaded')

  base_path_v = r'c:\Users\aakorobov\Videos'
  base_path_t = r'c:\Users\aakorobov\Videos\text'
  for file_name in tqdm(os.listdir(base_path_v),colour='green'):
    if not '.mkv' in file_name:
      continue
    path_v = os.path.join(base_path_v, file_name)
    path_out = os.path.join(base_path_t, file_name.replace('.mkv','.txt'))

    if not os.path.isfile(path_out):
      res = recognize_file(model, path_v)
      with open(path_out,'w',encoding='UTF-8') as f:
          f.write(res)
    #break
  print('done')