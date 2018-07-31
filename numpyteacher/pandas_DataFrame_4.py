import pandas as pd
import numpy as np


# scoresToClean.xlsx=>scoresToCleanOut.xlsx

# region DataFrame 處理遺失值 (清洗資料) 

#處理遺失值
#dropna() 方法 - filtering Out Missing Data
#fillna() 方法 - Filling in Missing Data - 有洞 holes 的 就填補

df = pd.read_excel('data/scoresToClean.xlsx', 'Sheet1')

df = pd.DataFrame(df)
print(df.info())

print(df.isna())
print (df.notna())
print(pd.isna(df))

print(df.fillna('X'))  # 全部有遺失值的觀測值填補 'X'
print(df.fillna(0)  )    

# =====================================# 
# 以下都 inplace=True

df.drop(['Avg','Rank','Sum','Max','Min','Good'],axis=1, inplace=True) 
df.drop([8,9],axis =0, inplace=True) 
 
# ==========================================================

# 缺失數據填充 平均值
df['Eng'] = df['Eng'].fillna(df['Eng'].mean()).round(2)      # 用平均值填充空值 series 
df.Eng.fillna(df.Eng.mean(), inplace=True)

df.dropna(axis=0, how='any', inplace=True)                  # 有遺失值的觀測值都刪除
df.dropna(axis=1, how='any', inplace=True)                 

# Name 變大寫
df['Name'] = df['Name'].str.upper()

# Transforming Data using a function or mapping (mapping, str)
df['Gender'] = df['Gender'].map({'Male':1, 'Female':0}).astype(int).astype(int)
df['Class'] = df['Class'].map({'CS_101':1, 'CS_102':2, 'CS':3}).astype(int)
df['Grade'] = df['Grade'].map({'A':1, 'B':2, 'C':3,'D':4})


# 用小數 兩位
df['Eng'] = df['Eng']/100
df['Math'] = df['Math']/100
df['Chi'] = df['Chi']/100

print(df)

df.to_excel('data/scoresToCleanOut.xlsx')
df.to_csv('data/scoresToCleanOut.csv')

#endregion

# region DataFrame wrangle data 資料角力 - merge(join) concate(union) reshape

# Demo Merge, join, and concatenate¶ 

# ==============================================================
# merge join
import numpy as np
dic_Products = {'ProductID':[1,2,3,4,5], 
       'ProductName':['chicken', 'xxx', 'pork', 'apple', 'orange'], 
       'CategoryID':[1,np.nan,1,2,2],
       'UnitPrice':[11,22,21, np.nan,55], 
        'Quantity':[11,33,33,4,5] 
} 

dic_Categories = {
       'CategoryName':['meat','fruit','xxx'], 
       'CategoryID':[1,2, 3]
} 


df_Products = pd.DataFrame(dic_Products)
df_Categories = pd.DataFrame(dic_Categories)

result =df_Categories.merge(df_Products, on='CategoryID',how='inner') # default inner join, instance method 也可以
print(result)

result =df_Categories.merge(df_Products, on='CategoryID',how='left') # default inner join, instance method 也可以
print(result)

result =df_Categories.merge(df_Products, on='CategoryID',how='right') # default inner join, instance method 也可以
print(result)

# Now this can be joined by passing the two key column names:
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
  
print(left)
print('================================')
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
   
print(right)
result = pd.merge(left, right, on=['key1', 'key2'])
print(result)


# concat
#  ========================================
dic1 = {'ProductID':[1,2,3,4,5], 
       'ProductName':['chicen', 'beef', 'pork', 'apple', 'orange'], 
       'CategoryName':['meat','meat','meat','fruit','fruit'],
       'UnitPrice':[11,22,21,44,55], 
        'Quantity':[11,33,33,4,5] 
} 


df1 = pd.DataFrame(dic1, index=dic1['ProductID'])

dic2 = {'ProductID':[6,7,8], 
       'ProductName':['coffee', 'cake', 'tea'], 
       'CategoryName':['drink','dessert','drink'],
       'UnitPrice':[11,22,21], 
        'Quantity':[11,33,33] 
} 


df2 = pd.DataFrame(dic2, index=dic2['ProductID'])

frames = [df1, df2]

# 加觀測值
result = pd.concat(frames)          # concat 一定是用 module function, 非物件方法
print(result)

# axis = 1 加欄位
dic3 = { 
       'ProductName2':['coffee', 'cake', 'tea'], 
       'CategoryName2':['drink','dessert','drink']
} 
df3 = pd.DataFrame(dic3)
result = pd.concat([df1,df3], axis=1)
print(result)

# 移除重複
# 建立一個有重複值的 data frame
name = ['aaa', 'aaa', 'bbb', 'ccc', 'ccc', 'ddd']
age = [19, 19, 17, 21, 21, 19]
duplicated_dict = {
    'name': name,
    'age': age
}
duplicated_df = pd.DataFrame(duplicated_dict)

# 判斷是否重複
print(duplicated_df)
print(duplicated_df.duplicated())

# 去除重複觀測值
print(duplicated_df.drop_duplicates(inplace=True ))
print(duplicated_df)

#endregion

print('end')