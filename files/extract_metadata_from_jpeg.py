#скрипт для переименовывания фотографий
# - из метаданных вытаскивается дата и подставляется в нименование
# - если именование файла уже содержит дату, тогда подводится к стандартному виду
# - иначе без изменения


#pip install pillow-heif
#pip install pillow
#pip install piexif
#pip install tqdm
#pip install python-dotenv
#%%
import re
from formating_date import formating
from PIL import Image, ExifTags
import pyheif
import piexif
v = {v:k for k,v in ExifTags.TAGS.items() if 'date' in v.lower()}
from tqdm import tqdm
import os
from dotenv import load_dotenv
load_dotenv()
#dotenv_path = Path('path/to/.env')
#load_dotenv(dotenv_path=dotenv_path)



def extract_formating_date_from_image_heic(file_path):
    # Чтение HEIC файла
    heif_file = pyheif.read(file_path)

    # Получение метаданных
    metadata = heif_file.metadata

    # Инициализация даты
    date_taken = None

    # Поиск даты в метаданных
    for item in metadata:
        if item['type'] == 'Exif':
            exif_data = item['data']            
            exif_dict = piexif.load(exif_data)
            if piexif.ExifIFD.DateTimeOriginal in exif_dict["Exif"]:
                date_taken = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
                date_taken = date_taken.decode('UTF8')
                break
            elif piexif.ExifIFD.DateTimeDigitized in exif_dict["Exif"]:
                date_taken = exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized]
                date_taken = date_taken.decode('UTF8')
                break
                
    if date_taken is None:
        return None
        
    f,_ = formating(date_taken)
    return f
                
# file_path = '/media/aleksei/data/cloud/yandex/Pictures/photo/2018/2018 Прочее/IMG_0190.heic'
# extract_formating_date_from_image_heic(file_path)


def extract_formating_date_from_image(file_path):
    img = Image.open(file_path)
    exifs = img._getexif()
    if exifs is None:
        return None
    v = {v:k for k,v in ExifTags.TAGS.items() if 'date' in v.lower()}
    dt_text = exifs.get(v['DateTime'])
    if dt_text is None:
        dt_text = exifs.get(v['DateTimeOriginal'])
    if dt_text is None:
        dt_text = exifs.get(v['DateTimeDigitized'])
    if dt_text is None:
        return None
    f,_ = formating(dt_text)
    return f


def is_corect_name(file_name):
    patern = r'^\d\d\d\d-\d\d-\d\d \d\d-\d\d-\d\d'
    return re.match(patern,file_name) is not None


#%%
def read_paths_from_file(path:str,base_path:str,path_where_find:str):
    all_paths = []
    with open(path,'r') as f:
        all_paths = f.readlines()
        all_paths = [p.strip() for p in all_paths]
    print(len(all_paths))
    base_path = base_path.rstrip('/')
    all_files = [base_path +'/' + f[2:] for f in all_paths if os.path.isfile(base_path +'/' + f[2:])]
    print(len(all_files))
    all_files1 = [f for f in all_files if f.startswith(path_where_find) and 'dtrash' not in f]
    print(len(all_files))
    print(len(all_files1))
    return all_files1


#%%
def get_group_extentions(all_files1):
    from collections import defaultdict
    group_ext = defaultdict(int)
    for f in all_files1:
        left_path,ext = os.path.splitext(f)
        group_ext[ext.lower()] += 1
    print(len(group_ext))
    import pandas as pd
    df_group_ext = pd.DataFrame(group_ext.items())
    df_group_ext.shape
    df_group_ext.columns  = ['ext','c']
    return df_group_ext.sort_values('c',ascending=False).head(50)



#%%
def action_rename(all_files1):
    result_renames = []
    try:
        #avaliable_exts = ['.jpg','.png','.jpeg']
        #avaliable_exts = ['.png']
        avaliable_exts = ['.jpg','.jpeg','.heic']
        for f in tqdm(all_files1):
            if not os.path.isfile(f):
                continue
            left_path,ext = os.path.splitext(f)
            if ext.lower() not in avaliable_exts:
                continue
            basename = os.path.basename(f)
            basename_not_ext = os.path.basename(left_path)
            if is_corect_name(basename_not_ext):
                continue
                
            correct_formating,source_find = formating(basename_not_ext)
            new_name = None
            if correct_formating is not None:
                #это означает что смогли из имени извлечь корректное название
                # поэтому просто переименовываем            
                new_name = basename_not_ext.replace(source_find, correct_formating) + ext
            else:
                new_left_name = None
                if ext.lower() == '.heic':
                    new_left_name = extract_formating_date_from_image_heic(f)    
                else:
                    new_left_name = extract_formating_date_from_image(f)
                if new_left_name is not None:
                    #print(f'{new_left_name=}')
                    new_name = new_left_name + '_'+ basename
                    
            if new_name is None:
                continue
            
            dirname = os.path.dirname(f)                
            new_full_name = dirname + '/' + new_name
            i = 0
            while os.path.isfile(new_full_name):
                i += 1
                new_left_path,ext = os.path.splitext(new_full_name)
                new_full_name = new_left_path+f'({i})'+ext
            #print(f'{new_full_name=}')
            result_renames.append(f"{f}->{new_full_name}\n")
            os.rename(f, new_full_name)
        #result_renames
    finally:
        print(len(result_renames))
        with open('result_rename_2.txt','a') as f:
            f.writelines(result_renames)
            
            
if __name__ == '__main__':
    base_path = os.getenv('BASE_PATH')
    path_where_find = os.getenv('PATH_WHERE_FIND') 
    path_list = os.getenv('PATH_LIST')
    
    all_files1 = read_paths_from_file(path_list, base_path, path_where_find)
    df = get_group_extentions(all_files1).head(50)
    print(df)
    action_rename(all_files1)
    