import pandas as pd
import numpy as np
# region
series1 = pd.Series(range(0, 4), index=['a', 'b', 'c', 'd'])
print(series1)
print(series1.values)
print(series1.index.values)
print(series1.index)

print(series1.shape)
print(series1.ndim)
series1.name = "score"
series1.index.name = "eng"
print(series1)

series1 = pd.Series(range(0, 4), index=['a', 'b', 'c', 'd'])
print(series1['b'])
series1 = pd.Series(range(0, 4))
print(series1[1])
# endregion
# region
series1 = pd.Series(np.arange(10), index=list("abcdefghij"))
print(series1)
print(series1.iloc[5])
print("-------------------------")
print(series1.iloc[2:8])
print("-------------------------")
print(series1.iloc[[3, 6.7]])
print("-------------------------")
print(series1.loc['c'])
print("-------------------------")
print(series1.loc[['c', 'd', 'e']])
print("-------------------------")
print(series1.loc['b':'j'])
print(series1.at['b'])
print(series1.iat[2])

print(series1.loc[series1 % 2 == 0])
print(series1[series1 % 2 == 0])
print(series1.loc[(series1 > 4) & (series1 < 8)])

print(series1.iloc[series1.values > 5])
print(series1.values)
print(series1[(series1 > 4) & (series1 < 8)])


def myfunc(serier):
    return (serier > 4) & (serier < 8)


print(series1.loc[myfunc])
print(series1.loc[lambda x: (x > 4) & (x < 8)])


series1 = pd.Series(np.arange(10), index=[2, 3, 1, 6, 7, 8, 9, 10, 11, 5])
print(series1.iloc[:3])  # 2  3  1
print(series1.loc[:3])  # 2  3

# endregion
# region
series1 = pd.Series(np.arange(0, 50))


def fun1(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'


print(series1.apply(fun1))
print(series1.apply(lambda x: 'Even' if x % 2 == 0 else 'Odd'))


series1 = pd.Series(np.random.randint(0, 101, 50))
print(series1)


def fun2(x):
    if x < 60:
        grade = 'E'
    elif x < 70:
        grade = 'D'
    elif x < 80:
        grade = 'C'
    elif x < 90:
        grade = 'B'
    else:
        grade = 'A'
    return "{0} ({1}) ".format(x, grade)


print(series1.apply(fun2))
series1 = pd.Series(['female', 'male', 'female', 'male',
                     'female', 'male', 'female', 'male', 'female'])
print(series1.map({'female': 1, 'male': 2}))
math = pd.Series([0, 1, 2, 3, 4, 5, 6, 7])
print(math.apply(np.sin))
print(math.apply(np.log))
print(math.apply(np.cos))
print(math.apply(np.max))
# endregion
# region
series1 = pd.Series([1, 2, 3, 4], index=list('abcd'), name="idx")
print(series1)
series1['e'] = 10
print(series1)
series1 = series1.append(series1)

# 刪除
series1.drop('a', inplace=True)
print(series1)
series1.drop(['b', 'c'], inplace=True)
print(series1)
series1 = pd.Series([1, 2, 3, 4], index=list('abcd'), name="idx")
series1['a'] = 999
print(series1)
series1.iloc[series1.values % 2 == 0] += 100
print(series1)
series1.loc[series1 % 2 == 0] += 100
print(series1)
# endregion
# region
series1 = pd.Series(np.random.randint(60, 101, 100))
print(series1)
print(series1.sum())
print(series1.max())
print(series1.min())
print(series1.mean())
print(series1.max() - series1.min())
# 小測驗 最高和最低差多少
print(series1.max() - series1.min())

print(series1.describe())
print(series1.agg([np.sum, np.min, np.max]))

temp = series1.agg([np.sum, np.min, np.max])
print(type(temp))
print(temp)
# endregion
# region
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7])
indexlise = list('xxxxyyy')
seriesgroup = series1.groupby(indexlise)
print(seriesgroup.groups)
print(seriesgroup)


def printgroup(seriesgroup):
    for k, v in seriesgroup:
        print(k)
        print(v)
        print("="*50)


printgroup(seriesgroup)
print(seriesgroup.count())
print(seriesgroup.min())
print(seriesgroup.max())
print(seriesgroup.count())


# split- apply - combine
print(series1.groupby(['x', 'x', 'x', 'x', 'y', 'y', 'y']).min())

print(series1.groupby(['x', 'x', 'x', 'x', 'y', 'y', 'y']).max())
print(series1.groupby(['x', 'x', 'x', 'x', 'y', 'y', 'y']).apply(np.max))


def peak(series):
    return series.max() - series.min()


print(series1.groupby(['x', 'x', 'x', 'x', 'y', 'y', 'y']).apply(peak))
series1 = pd.Series([1, 2, 3, 4, 5, 6, 7])
# by_series = series1 % 2
by_series = series1.apply(lambda x: 'even' if (x % 2 == 0) else 'odd')
print(by_series)
printgroup(series1.groupby(by_series))
print(series1.groupby(by_series).count())
print(series1.groupby(by_series).max())
print(series1.groupby(by_series).min())
print(by_series.value_counts())


# 小測驗 TODO groupby 隨機 統計  split=> 分成 三群 '待加強' '佳' '優良'
series1 = pd.Series(np.random.randint(0, 101, 50))


def check(series):
    if series < 60:
        return'待加強'
    elif series < 80:
        return '佳'
    else:
        return'優良'


by_series = series1.apply(check)
series1_group = series1.groupby(by_series)
print(printgroup(series1_group))
print(series1_group.count())
# region
ts = pd.Series(np.random.randint(100,300,1000),index=pd.date_range('1/1/2000', periods=1000))
print(ts)
print(ts.groupby(ts.index.year).sum())
print(ts.groupby(ts.index.month).sum())
print(ts.groupby([ts.index.year,ts.index.month]).sum())