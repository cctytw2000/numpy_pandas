import pandas as pd

# region DataFram 結構


# dataFrame 
# 1. 就如 Table 表格,  多個 series, 共享相同的 index, 每個 series 可以不同 的 Data Type
# 2. 列索引與欄索引 (列標籤與欄標籤) [row_indexer , col_indexer]
# 3. axis 方向很重要 => 做相關 apply / aggregation sum, min.. / groupby
# 4. 方法功能 都有相對應 sql 語法

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
print(scores_df)


print(scores_df.ndim, scores_df.shape)
print(scores_df.index)
print(scores_df.columns)
print(scores_df.values, type(scores_df.values))

print(scores_df.info())
print(scores_df.describe())
print(scores_df.head(3))
print(scores_df.tail())

# scores_df.to_csv('data/scores.csv')
# scores_df.to_excel('data/scores.xlsx')
# scores_df.to_html('data/scores.html')

# ===============================

# df = pd.read_csv('http://bit.ly/imdbratings')
# df.to_csv('data/movies.csv')
# print(df.head())
# print(df.info())

# df = pd.read_csv('http://bit.ly/kaggletrain')
# df.to_csv('data/titanic.csv') # 鐵達尼號
# print(df.head())
# print(df.info())


# # iris 鳶尾花資料集
# url = "https://storage.googleapis.com/2017_ithome_ironman/data/iris.json" # 在雲端上儲存了一份 JSON 檔
# df = pd.read_json(url)
# df.to_csv('data/iris.csv') #
# print(df.head())
# print(df.info())
# print(df.describe())

# endregion

# region 選欄位 column []  , iloc[row pos , column pos], loc[row index, column index]
print(scores_df['Chi'])
print (scores_df.Chi)
print(scores_df.Chi.sum())

print(scores_df.Name.apply(lambda x: x.upper()))

# print(scores_df.Name)
# scores_df.Name['a'] = 'AAA'

print(scores_df.Name.str.upper())

# multi column
print(scores_df[['Chi', 'Eng', 'Math']])

print(scores_df.iloc[1:3, 1:4])
print(scores_df.loc['a':'c', 'Chi':'Math' ])
print(scores_df.loc['a':'c', ['Chi','Eng'] ])

# 英文不及格 ... 是誰 
print(scores_df.loc[scores_df.Eng>=60, ['Class', 'Name']])
print(scores_df.loc[scores_df.Eng<60, ['Class', 'Name']])

print(scores_df>=60)
print(scores_df[scores_df>=60])
print(scores_df[scores_df<60])

print(scores_df)

# 小測驗
# 共幾個 學員成績 ?						
				
# 找出 前面三個 的學員所有科目成績					
# 找出 後面兩個 的學員所有科目成績					
												
# 找出 ID 'a','b','c' 的學員國文英文科目成績					
					
# 找出某x學員的學員成績			==		
# 找出除了某學員的學員的所有成績 (x 退學)	!=
# 							
# 找出 'aaa', 'bbb' 'ccc' 學員 國文數學兩科 科目成績  |	 np.isin(...)					
# 數學不及格 ... 是誰 

# endregion

print('end')