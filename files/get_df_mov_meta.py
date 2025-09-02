#%%



import os
import subprocess
from tqdm import tqdm
base_path = '/media/aleksei/home/video/m_n/'
import json
import pandas as pd
#%%

results = []
for file in tqdm(os.listdir(base_path)):
    filename=os.path.join(base_path,file)
    result = subprocess.run(["exiftool", "-j", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    
    data_str = result.stdout
    data = json.loads(data_str)
    results.extend(data)    

print(len(results))
#%%
df = pd.DataFrame(results)
df.shape
# %%
c = df['FileName'].str.contains(' 2')
#%%
to_folder = 'double'
for file in df[c]['SourceFile']:
    if not os.path.isfile(file):
        continue
    base_path, fn = os.path.split(file)
    base_path = os.path.join(base_path,to_folder)
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    filename_new = os.path.join(base_path,fn)
    os.rename(file,filename_new)
# %%

for file in tqdm(os.listdir(base_path)):
    filename=os.path.join(base_path,file)
    base_path_1, fn = os.path.split(filename)
    fn,ext = os.path.splitext(fn)
    fn = fn+' 2'+ext
    base_path_1 = os.path.join(base_path_1,to_folder)
    filename_new = os.path.join(base_path_1,fn)
    if os.path.isfile(filename_new):
        filename_new_s = os.stat(filename_new).st_size
        filename_s = os.stat(filename).st_size
        if filename_new_s != filename_s:
            print(filename_new)
#%%
results = []
for file in tqdm(os.listdir(base_path)):
    filename=os.path.join(base_path,file)
    result = subprocess.run(["exiftool", "-j", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    
    data_str = result.stdout
    data = json.loads(data_str)
    results.extend(data)
print(len(results))
#%%
df = pd.DataFrame(results)
df.shape

# %%
pd.options.display.max_columns = 200
#%%
df.head(1)
# %%
df[~df['CreationDate'].isna()]
# %%

for i,row in df[~df['CreationDate'].isna()].iterrows():
    if row['CreationDate'] is None:
        continue
    file_new = row['CreationDate'][0:19].replace(':','-')
    filename = row['SourceFile']
    if not os.path.isfile(filename):
        continue
    file = file.replace('.MOV','').replace('IMG_','')
    file_new = file_new+'_'+file + '.MOV'
    bp,file = os.path.split(filename)
    filename_new = os.path.join(bp,file_new)
    os.rename(filename,filename_new)