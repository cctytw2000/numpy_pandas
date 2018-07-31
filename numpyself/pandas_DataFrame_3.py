from pandas_series import printgroup
import pandas as pd
import matplotlib.pyplot as plt
scores = pd.read_excel('data/scores.xlsx')
print(scores)
scoresgroup = scores.groupby('Class')
print(printgroup(scoresgroup))
print(scores.groupby('Class').max())
print(scores.groupby('Class').apply(lambda df: df.describe()))
print(scores.groupby(['Class', 'Gender'])['Math'].mean())
print(scores.groupby(['Class', 'Gender'])['Math'].mean().unstack())
print(scores.pivot_table(index='Class',
                         columns='Gender', values='Math', aggfunc='mean'))
scores['Class'].value_counts().plot.pie()
plt.show()
df = scores.groupby('Class').mean()
print(df)
df.plot.bar()
plt.show()

df.plot.bar(y=['Eng', 'Math'])
plt.show()

df.plot.barh(stacked=True)
plt.show()


df.plot.bar(subplots=True)
plt.show()
# 小測驗
# 各製造商每個月總銷售分析
sell = pd.read_excel('data/Sales.xlsx')
print(sell)
# 鐵達尼號不同性别的活存分析