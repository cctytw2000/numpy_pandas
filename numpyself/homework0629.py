
import pandas as pd
import matplotlib.pyplot as plt


# 小測驗
score = pd.read_excel('data/scores.xlsx')
print(score)
# 共幾個 學員成績 ?


print(score.count())
# 找出 前面三個 的學員所有科目成績
print(score.head(3))
# 找出 後面兩個 的學員所有科目成績
print(score.tail(2))
# 找出 ID 'a','b','c' 的學員國文英文科目成績
print(score.loc[['a', 'b', 'c'], ['Chi', 'Eng']])

# 找出某x學員的學員成績
print(score.loc['a'])
# 找出除了某學員的學員的所有成績 (x 退學)	!=
print(score.loc[score.Name != 'ccc', ['Math', 'Chi', 'Eng']])
# 找出 'aaa', 'bbb' 'ccc' 學員 國文數學兩科 科目成績  |	 np.isin(...)
print(score.loc[['a', 'b', 'c'], ['Chi', 'Eng', 'Math']])

# 數學不及格 ... 是誰
print(score.loc[score.Math < 60, ['Math']])

# 小測驗
# 各製造商每個月總銷售分析
sell = pd.read_excel('data/Sales.xlsx')
# print(sell)
# print('==================================')
print(sell.groupby(['Month'])['Product'].size())

# 鐵達尼號不同性别的活存分析