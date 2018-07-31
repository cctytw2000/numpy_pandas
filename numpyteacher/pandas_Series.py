import pandas as pd
import numpy as np

# region Create Series
series1 =pd.Series([1,2,3,4], index=['a','b','c','d'])

print(series1.values, type(series1.values))
print(series1.index)

# 背後 ndarray, 借 numpy ndarray 的 Power
print(series1.ndim, series1.shape, series1.dtype)
series1.index.name = 'id'
series1.name = 'Chi'

print(series1)

# ValueError: Wrong number of items passed 4, placement implies 3
# series1 =pd.Series([1,2,3,4], index=['a','b','c'])
# print(series1)

#endregion

# region index [ ] 篩選資料

# 直接索引[] confuse
series1 =pd.Series([1,2,3,4], index=[3,4,1,5])
print(series1[3]) # index
print(series1)

series1 =pd.Series([1,2,3,4])
print(series1[3])  # position
print(series1)

series1 =pd.Series( np.arange(10), index=list('abcdefghij'))
print(series1)

# int pos location - iloc  
print(series1.iloc[3])
print(series1.iloc[2:7])
print(series1.iloc[[1,3,4]])

print(series1.loc['a'])
print(series1.loc['a':'f'])
print(series1.loc[['a','d','e']])

print(series1.loc[series1 % 2 == 0])
print(series1>5)
print(series1.loc[series1 >5])
print(series1[(series1 >5) & (series1 <8)])

def myfunc(series):
    # ........logic
    return (series > 5) & (series < 8)

print(series1.loc[myfunc])                      # 具名方法
print (series1.loc[lambda  x: (x >5) & (x<8)])  # 匿名方法

# iat /at - for scalar value
print(series1.iat[0])
print(series1.at['a'])

# 小測驗
series1 = pd.Series( np.arange(10), index=[2,3,1,6,7,8,9,10,11,5])
print(series1)
print(series1*30.3)

# print(series1.iloc[:3])
# print(series1.loc[:3])

print('end')
# endregion

# region apply() map()

series1 = pd.Series([1,2,3,4,5,6,7])

def myfunc(x):
    #  if x % 2==0:
    #      return 'Even'
    #  else:
    #      return 'Odd'    
    return 'Even' if x%2==0 else 'Odd'

print( series1.apply(myfunc))        # 具名方法

# series1 = series1.apply(myfunc)    # 具名方法
# print(series1)

print(series1.apply(lambda  x:  'Even' if x%2==0 else 'Odd'))       # 匿名方法

# 小測驗 >3 *30 else *20
print(series1.apply(lambda x: x*30 if x > 3 else x*20) )            # 匿名方法

print (series1.apply(np.sin))
print (series1.apply(np.log))
print (series1.apply(np.abs))
print(series1.apply(float))

# 小測驗 apply 高中低 ABCDE 
def myfunc(value):
   if (value<60):
       grade= 'E'
   elif (value<70):
      grade='D'
   elif (value<80):
       grade= 'C'   
   elif (value<90):
       grade= 'B'
   else:
      grade='A'   
   return '{0} ({1})'.format(value, grade) 

series1 = pd.Series(np.random.randint(60, 101, 100))
print(series1.apply(myfunc))  

# map
series1=pd.Series(['female','male','female','male'])
print (series1)
print(series1.map({'female':1, 'male':0}))


# endregion

# region series CRUD

# 新增
series1 = pd.Series([1,2,3,4], index=['a','b','c','d'], name='Chi')
print(series1)
series1['e'] = 10
print(series1)

print(series1.append(series1))

# 刪除

series1.drop('a', inplace=True)
print(series1)

series1.drop(['b','c'], inplace=True)
print(series1)

# del series1['c']

# 修改 apply / map  
series1 = pd.Series([1,2,3,4], index=['a','b','c','d'], name='Chi')
series1['a']=999
print(series1)

# 小測驗 偶數累加 100
series1.loc[series1%2==0] +=100
print(series1)

# endregion

# region aggregation  sum() min() max()  agg().....

series1= pd.Series(np.random.randint(60, 101, 100))
print(series1.sum())
print(series1.min())
print(series1.max())
print(series1.mean())
print(series1.count())

# 小測驗 最高和最低差多少
print(series1.max()- series1.min())

print(series1.describe())
print(series1.agg([np.sum, np.min, np.max])) 

temp=series1.agg([np.sum, np.min, np.max])
print(type(temp))
print( temp)

# endregion

# region groupby() split- apply - combine

series1=pd.Series([1,2,3,4,5,6,7])
# split
mygroup = series1.groupby(['x','x','x','x','y','y','y'])  # by key
print (mygroup.groups)
print(mygroup)    #<pandas.core.groupby.SeriesGroupBy object at 0x0000023A40C3AA58>

def DisplayGroup(mygroup): 
    for k,v in mygroup:
        print (k)
        print (v)
        print('==============================')

DisplayGroup(mygroup)

# apply - combine
print(mygroup.count())


# split- apply - combine
print(series1.groupby(['x','x','x','x','y','y','y']).min())
print(series1.groupby(['x','x','x','x','y','y','y']).max())
print(series1.groupby(['x','x','x','x','y','y','y']).apply(np.max))

def peak(series):
    return series.max() - series.min()

print(series1.groupby(['x','x','x','x','y','y','y']).apply(peak))

#   by : mapping, function, str, or iterable
#             Used to determine the groups for the groupby.
#             If ``by`` is a function, it's called on each value of the object's
#             index. 
# 
# If a dict or Series is passed, the Series or dict VALUES
#             will be used to determine the groups (the Series' values are first
#             aligned; see ``.align()`` method). If an ndarray is passed, the
#             values are used as-is determine the groups. A str or list of strs
#             may be passed to group by the columns in ``self``
by_series = series1 % 2 
by_series = series1.apply (lambda x: 'even' if (x % 2) == 0 else 'odd')
print (by_series)

DisplayGroup(series1.groupby(by_series))

print(series1.groupby(by_series ).count())
print(series1.groupby(by_series ).max())


# 小測驗 TODO groupby 隨機 統計  split=> 分成 三群 '待加強' '佳' '優良'
#  
# x
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# ==============================
# y
# 4    5
# 5    6
# 6    7
# dtype: int64
# ==============================

# endregion

# region value_counts

print(by_series.value_counts())

series1=pd.Series([80,80,80,90,90,100])
print(series1.value_counts())
print(series1.value_counts(normalize=True))

# endregion

# region datetime series  sort_values() sort_index()

dateindex = pd.date_range(start='1/1/2011',periods=1000)
print(dateindex)

series1 = pd.Series(np.random.randint(100, 200, 1000), index=dateindex )
print (series1)

series1.sort_values(ascending=False, inplace=True)
print(series1)

series1.sort_values(ascending=True, inplace=True)
print(series1)

series1.sort_index(ascending=False, inplace=True)
print(series1)

print(series1.index.year)

print(series1.groupby(series1.index.year).sum())
print(series1.groupby(series1.index.month).sum())
print(series1.groupby([series1.index.year,  series1.index.month]).sum())

print(series1.groupby([series1.index.year,  series1.index.month]).sum().unstack())
# endregion

print('end')