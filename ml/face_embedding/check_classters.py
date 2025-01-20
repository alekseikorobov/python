

#%%
import pandas as pd
#%%
df = pd.read_feather('data_1.feather')
print(f'{df.shape=}')

# %%
df['cluster'].value_counts().head(30)

#208

#%%

#df[df['cluster'] == 187]['image_path'].values
res_list = []
for index in df['cluster'].value_counts().head(30).index:
    vals = df[df['cluster'] == index]['image_path'].values[0:3]
    for v in vals:
        if '00280' in v:
            print(f'{index=},{vals=}')
    #res_list.extend()

len(res_list)
#%%
with open('res.txt','w') as f:
    for l in res_list:
        f.write(f'{l}\n')

#%%

with open('all_208.txt','w') as f:
    for l in df[df['cluster'] == 208]['image_path'].sort_values().values:
        f.write(f'{l}\n')


