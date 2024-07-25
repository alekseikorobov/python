from tqdm import tqdm
import json
import wave
import sys

from vosk import Model, KaldiRecognizer

import moviepy
import moviepy.editor as ed


def recognize_file(model, path):
  print(f'rec from {path=}')
  wf = wave.open(path, "rb")
  if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
      raise Exception("Audio file must be WAV format mono PCM.")

  c = 8000
  N = wf.getnframes()
  count_chank = N//c
  i = 1 if (N/c - count_chank)>0 else 0
  k = 0

  result_text = []

  rec = KaldiRecognizer(model, wf.getframerate())

  for _ in tqdm(range(count_chank + i)):
      data = wf.readframes(c)
      if len(data) == 0:
          break
      if rec.AcceptWaveform(data):
          r = rec.Result()
          rj = json.loads(r)
          if 'text' in rj and rj['text'] != '':
              result_text.append(rj['text'])

  r = rec.FinalResult()
  rj = json.loads(r)
  if 'text' in rj and rj['text'] != '':
      result_text.append(rj['text'])

  return result_text

def extract_audio_from_mkv(path,path_out):
  print(f'start extract wav from mkv {path=}')
  #path = r'c:\Users\aakorobov\Videos\2024-07-15_11-07-23.mkv'
  ac = ed.AudioFileClip(path)
  ac.write_audiofile(path_out, ffmpeg_params=["-ac", "1"])
  print(f'done extract {path_out=}')

import os
if __name__ == '__main__':
  print('model load...')
  model = Model(model_path='data/vosk-model-ru-0.10')
  print('model loaded')

  base_path_v = r'c:\Users\aakorobov\Videos'
  base_path_a = r'c:\Users\aakorobov\Videos\audio'
  base_path_t = r'c:\Users\aakorobov\Documents\obsidian\work\Meeting\recognition\text'
  for file_name in tqdm(os.listdir(base_path_v),colour='green'):
    if not '.mkv' in file_name:
      continue
    path_v = os.path.join(base_path_v, file_name)
    path_in = os.path.join(base_path_a, file_name.replace('.mkv','.wav'))
    path_out = os.path.join(base_path_t, file_name.replace('.mkv','.md'))

    if not os.path.isfile(path_in):
      extract_audio_from_mkv(path_v,path_in)

    if not os.path.isfile(path_out):
      res = recognize_file(model, path_in)
      with open(path_out,'w',encoding='UTF-8') as f:
        for line in res:
          f.writelines(line + '\n')
  print('done')