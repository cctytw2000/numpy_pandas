import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 小測驗 陣列元素值 5~49 
arr = np.arange(5, 50, 1)
print(arr)
print (arr.size * arr.itemsize)
print(arr.nbytes)
# ==========================================

arr= np.array(['aaa','bbb','ccc'])
print(arr.ndim, arr.shape, arr.dtype)

arr= np.array([True, False, True])
print(arr.ndim, arr.shape, arr.dtype)

arr= np.array([True, False, True, 33,78])
print(arr.ndim, arr.shape, arr.dtype)

arr= np.array([1,2,3,4,5,6,7,8,9,10])
# 小測驗 陣列個元素是否為偶數
print (arr % 2 == 0 )

print (arr ==2)
print (arr !=2)

mask = (arr == 2)
print (mask)      
print (~mask)  
# 小測驗 倒著排 
print (arr[::-1]) 
# 小測驗 找偶數
#        找奇數

arr = np.array([0,11,21,33,84,55,66,77,8,9])
print (arr[arr %2 ==0])
print (arr[arr %2 ==1])
# 小測驗 找陣列中間級

print (arr[(arr>=50) & (arr<=80)])
mask = (arr>=50) & (arr<=80)
print (arr[mask])
print(arr[~mask])
# 小測驗  有沒有任何一個元素 > 90 
print (arr[arr>90].size > 0)
# 小測驗 陣列 0~99,  < 5 變 1000; >= 5 變 2000
arr = np.arange(100)
arr[arr <5] = 1000
arr[arr>=5] = 2000
print (arr)
# 小測驗 成績平均
arr = np.array([90,90,100])           # 三科分數   
arr_weight = np.array([0.25,0.25, 0.5]) # 分數權重 
print(arr.mean())
print( (arr * arr_weight).sum())


# region 
players = [56, 8, 19, 14, 6, 71]
teams = ["apple", "organse", "pineapple", "big apple", "bananna", "cherry"]
players_arr = np.array([players])
teams_arr = np.array([teams])
print('Players總共有', players_arr.sum(), '人')
print('共有', teams_arr.size, '隊')
maxteam = players_arr == players_arr.max()
print('最多人的TEAM是', players_arr[maxteam], '人')
print('人數最多的隊伍是', teams_arr[[maxteam]])
max10team = players_arr > 10
print('人數大於10的隊伍是', teams_arr[[max10team]])
nocherryteam = teams_arr != 'cherry'
nocherrysum = players_arr[[nocherryteam]].sum()
print('除了CHERRY組別的加總人數', nocherrysum)

# 小測驗 偶數而且>5元素 ; 偶數元素 set 1001 ; else 奇數元素 set  1
arr =np.array(
                [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12]
                ]
             )

# 小測驗 偶數而且>5元素 

print(arr[ (arr %2==0)  &  (arr >5) ])
# 小測驗 0     1 
arr = np.zeros((10,10))
arr[1:-1,1:-1] = 1
print(arr)

arr = np.ones((10,10))
arr[1:-1,1:-1] = 0
print(arr)
# 小測驗 
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x[y>0], y[y>0], c='r')
plt.scatter(x[y<=0], y[y<=0], c='g')
plt.show()

# 小測驗　冰島人口
year = np.arange(2007, 2017,)
people = np.array(np.random.randint(10, 50, (year.size)))
people.sort()

plt.plot(year, people, color="green")
plt.plot(year, people*2, color="blue", linestyle='dashed', linewidth=2)
plt.xlabel("year")
plt.ylabel("people")
plt.title("Iceisland")
plt.show()
plt.pie(people, autopct='%.2f %%')
plt.show()


# 小測驗
scores = pd.read_excel('data/scores.xlsx')
print(scores)
# 共幾個 學員成績 ?
print(scores.count())
# 找出 前面三個 的學員所有科目成績
print(scores.head(3))
# 找出 後面兩個 的學員所有科目成績
print(scores.tail(2))
# 找出 ID 'a','b','c' 的學員國文英文科目成績
print(scores.loc[['a', 'b', 'c'], ['Chi', 'Eng']])

# 找出某x學員的學員成績
print(scores.loc['a'])
# 找出除了某學員的學員的所有成績 (x 退學)	!=
print(scores.loc[scores.Name != 'ccc', ['Math', 'Chi', 'Eng']])
# 找出 'aaa', 'bbb' 'ccc' 學員 國文數學兩科 科目成績  |	 np.isin(...)
print(scores.loc[['a', 'b', 'c'], ['Chi', 'Eng', 'Math']])

# 數學不及格 ... 是誰
print(scores.loc[scores.Math < 60, ['Math']])

# 小測驗
# 各製造商每個月總銷售分析
sell = pd.read_excel('data/Sales.xlsx')
# print(sell)
# print('==================================')
print(sell.groupby(['Month'])['Product'].size())

# 鐵達尼號不同性别的活存分析



dic ={
         'Name':['aaa' ,'bbb','ccc','ddd','eee','fff'] ,
         'Gender':['Male','Male','Female','Female','Female','Female'],
         'Class':['CS_101', 'CS_102','CS_101', 'CS_102','CS_101', 'CS_102' ],
         'Chi':[80, 100, 60, 80, 80, 80],
         'Eng':[80, 80, 50, 70, 80, 80],
         'Math':[50, 100, 75, 85, 50, 80]
     } 
        
scores_df = pd.DataFrame(dic ,  
            columns=['Name', 'Gender', 'Class', 'Chi', 'Eng','Math'],
            index=list('abcdef') )
scores_df['Max'] = scores_df[['Chi','Eng','Math']].max(axis=1)

scores_df['Min'] = scores_df[['Chi','Eng','Math']].min(axis=1)
print(scores_df)
# 小測驗
scores_df.to_excel('data/scores統計.xlsx')
# 小測驗
# 所有班級 最高最低差多少

# answer 1:
maxSeries= scores_df[['Chi','Eng','Math']].max(axis=0)
minSeries= scores_df[['Chi','Eng','Math']].min(axis=0)

print(maxSeries)
print(minSeries)
print(maxSeries-minSeries)

# answer 2:
print(scores_df[['Chi','Eng','Math']].apply(lambda x: x.max()-x.min(),axis=0))
# 小測驗
# 個人最高和最低

def peak(series):
    return series.max() - series.min()

print(scores_df[['Chi', 'Eng', 'Math']].apply(lambda x: x.max()-x.min(), axis=1) )
print(scores_df[['Chi', 'Eng', 'Math']].apply(peak, axis=1))
# 小測驗
series1 = pd.Series( np.arange(10), index=[2,3,1,6,7,8,9,10,11,5])
print(series1)
print(series1*30.3)
# 小測驗 >3 *30 else *20
print(series1.apply(lambda x: x*30 if x > 3 else x*20) ) 
# 小測驗 apply 高中低 ABCDE 
def Grading(value):
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
print(series1.apply(Grading)) 

# 小測驗 偶數累加
series1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
series1.loc[series1%2==0] +=100
print(series1) 

# 小測驗 最高和最低差多少
series1= pd.Series(np.random.randint(60, 101, 100))
print(series1.max()- series1.min())
# 小測驗 TODO groupby 隨機 統計  split=> 分成 三群 '待加強' '佳' '優良'
series1 = pd.Series(np.random.randint(0, 101, 50))


def check(series):
    if series < 60:
        return'待加強'
    elif series < 80:
        return '佳'
    else:
        return'優良'

def printgroup(seriesgroup):
    for k, v in seriesgroup:
        print(k)
        print(v)
        print("="*50)

by_series = series1.apply(check)
series1_group = series1.groupby(by_series)
print(printgroup(series1_group))
print(series1_group.count())