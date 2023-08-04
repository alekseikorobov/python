
#%%

import pandas as pd

df = pd.read_csv('/media/aleksei/data/nastya/cloud/files_20230801_d.csv',sep=',')
df

#%%
df['full_path'] = df['path'] + '/'+df['file']

#%%
df['is_delete'] = 0
#%%

#df['path'].value_counts()
import os
def delete_file(s):
    if os.path.isfile(s):
        try:
            os.remove(s)
            return 1
        except Exception as ex:
            print(ex)
            return -2
    else:
        return -1


index = df.index

df.loc[index,'is_delete']  = df.loc[index]['full_path'].apply(delete_file)
    

#df[df['path'] == '/media/aleksei/data/nastya/cloud/yandex/Фотокамера']['full_path'].head(1).apply(delete_file)
# %%
df['is_delete'].value_counts()



# %%
df[df['is_delete'] == -1]