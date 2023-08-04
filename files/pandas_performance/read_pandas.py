
import pandas as pd

df = pd.read_csv('data.csv')
print(df.shape)
print(df.memory_usage())

print(df.info(memory_usage="deep"))
print(df.memory_usage(deep=True).sum())

