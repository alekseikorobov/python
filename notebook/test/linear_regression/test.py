import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# грузим датасет
url = 'https://raw.githubusercontent.com/razority/R_data/main/Exam.xlsx'
exam = pd.read_excel(url)
exam['school'] = exam['school'].map(lambda x: str(x))

# рисуем диаграмму рассеяния 
fig, ax = plt.subplots(figsize=(8,8))
g = sns.scatterplot(x='standLRT', y='normexam', hue='school', data=exam)
# немного надо трансформировать легенду
h,l = g.get_legend_handles_labels()
g.legend(h,l, ncol=4, bbox_to_anchor=(1, 1), loc=2)

# исследуем модель
model = smf.ols('normexam ~ standLRT', data=exam).fit()
display(model.summary())

# линейная регрессия
plt.figure(figsize=(8,8))
x = np.array(exam.loc[:,'standLRT'])
y = np.array(exam.loc[:,'normexam'])

sns.scatterplot(x='standLRT', y='normexam', data=exam)
b1, b0 = np.polyfit(x, y, 1) #  b0 - intercept, b1 - slope
sns.lineplot(x, b0 + b1*x, color='red')
plt.grid()