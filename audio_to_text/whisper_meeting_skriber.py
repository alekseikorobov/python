#можно улучшить если сделать как в статье
#https://huggingface.co/learn/audio-course/ru/chapter7/transcribe-meeting
import whisper
import time
from pyannote.audio import Pipeline
import torch
from tqdm import tqdm
import os
import subprocess
import gc
torch.cuda.empty_cache()
gc.collect()
import datetime
from dotenv import load_dotenv
load_dotenv()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# It can be re-enabled by calling
#    >>> import torch
#    >>> torch.backends.cuda.matmul.allow_tf32 = True
#    >>> torch.backends.cudnn.allow_tf32 = True

class Recognizer():
    def __init__(self,token:str):
        # import torch
        # torch.backends.cuda.matmul.allow_tf32 = True
        # torch.backends.cudnn.allow_tf32 = True
        # Загрузка модели Whisper
        #self.model_name = 'medium_s'
        self.model_name = 'turbo'
        self.model = 'turbo'
        self.whisper_model = whisper.load_model(self.model, device="cuda")  # Можно выбрать модель: tiny, base, small, medium, large        
        
        self.diarization_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",use_auth_token=token)

        self.diarization_pipeline = self.diarization_pipeline.to(torch.device('cuda'))
        
        self.base_path_v = os.getenv('BASE_PATH_VIDEO')
        if self.base_path_v is None:
            raise(Exception(f'not set param - BASE_PATH_VIDEO'))
        
        self.base_path_t = os.getenv('BASE_PATH_RESULT_TEXT')
        if self.base_path_t is None:
            raise(Exception(f'not set param - BASE_PATH_RESULT_TEXT'))
        self.use_ext = ['.mkv','.mp3']
        self.result_ext = 'md' #расширение в который нужно записать выходной текст

    def convert_seconds_to_hms(self,seconds):
        total_time = datetime.timedelta(seconds=seconds)
        
        hours = total_time.seconds // 3600
        minutes = (total_time.seconds % 3600) // 60
        seconds_left = total_time.seconds % 60
        
        return f"{hours:02d}:{minutes:02d}:{seconds_left:02d}"



    # Функция для транскрибации аудиофайла с разделением по спикерам
    def transcribe_with_speaker_diarization(self, audio_file):
        # Применяем дизаризацию
        print('diarization_pipeline...')
        diarization = self.diarization_pipeline(audio_file)

        print('whisper.load_audio...')
        # Открываем аудиофайл с помощью Whisper
        audio = whisper.load_audio(audio_file)

        # Обрабатываем каждый сегмент
        transcriptions = []
        i = 0
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            # Вырезаем сегмент аудио
            start_sample = int(turn.start * 16000)  # Whisper ожидает частоту 16 кГц
            end_sample = int(turn.end * 16000)
            segment_audio = audio[start_sample:end_sample]

            # Транскрибируем сегмент с помощью Whisper
            result = self.whisper_model.transcribe(segment_audio, language="ru")
            text = result["text"]
            
            f"{speaker}: (с {turn.start:.1f} до {turn.end:.1f} секунд)"
            
            #print(f'{i}:{speaker}: {len(text)=} (с {turn.start:.1f} до {turn.end:.1f} секунд)')

            # Добавляем результат в список
            transcriptions.append(f"{speaker} ({self.convert_seconds_to_hms(turn.start)}-{self.convert_seconds_to_hms(turn.end)}): {text}")
            i+=1
            # if i > 10:
            #     break

        return "\n".join(transcriptions)

    # Пример использования
    
    def get_audio_file(self, from_file):
        base_path, ext = os.path.splitext(from_file)
        if ext.lower() == '.mp3':
            return from_file
        file_result = f"{base_path}.wav"
        if os.path.isfile(file_result):
            return file_result
        
        command = f'ffmpeg -i "{from_file}" "{file_result}"'
        #subprocess.run(cmd)
        subprocess.call(command, shell=True)
        return file_result
    
    
    def run_one(self, path_v):
        _,file_name = os.path.split(path_v)
        file_name_b,ext = os.path.splitext(file_name)
        if not ext in self.use_ext:
            raise(Exception(f'not support ext - {ext}, use: {self.use_ext}'))
        path_out = os.path.join(self.base_path_t, file_name.replace(ext,f'_{self.model_name}.{self.result_ext}'))

        # if os.path.isfile(path_out):
        #   os.remove(path_out)
        
        if not os.path.isfile(path_out):
            path_wav = self.get_audio_file(path_v)
            res = self.transcribe_with_speaker_diarization(path_wav)
            with open(path_out,'w',encoding='UTF-8') as f:
                f.write(res)
        print(f'done - {path_v}')
    
    def run_all(self):
        start = time.time()       
        
        if not os.path.isdir(self.base_path_t):
            os.mkdir(self.base_path_t)
        
        for file_name in tqdm(os.listdir(self.base_path_v),colour='green'):    
            file_name_b,ext = os.path.splitext(file_name)
            if not ext in self.use_ext:
                continue
            # if file_name != '2024-09-03_17-02-22.mkv':
            #   continue
            
            path_v = os.path.join(self.base_path_v, file_name)
            
            self.run_one(path_v)            
            #break
            #break
        end = (time.time() - start)
        
        
        
        print(f'done, {datetime.timedelta(seconds=end)}')

if __name__ == '__main__':
    # Загрузка модели для дизаризации 
    r = Recognizer(os.getenv('TOKEN_HF'))
    r.run_all()
    
    