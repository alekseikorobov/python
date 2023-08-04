# вывод дубликатов


import pandas as pd

df = pd.read_csv('/media/aleksei/data/nastya/cloud/files_20230801.csv',sep='|',names=['path','file','hash'])

# находим все дубликаты:
#keep=False
res = df[df['hash'].duplicated() & df['hash'].notna()].sort_values('hash')

#записываем дубликаты в файл, далее обработка должна происходить вручную
res.to_csv('/media/aleksei/data/nastya/cloud/files_20230801_d.csv')


