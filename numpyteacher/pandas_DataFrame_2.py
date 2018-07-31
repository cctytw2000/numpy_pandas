import pandas as pd

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

# region aggregation sum(axis =0, 1)
# df = pd.DataFrame(scores_df['',''])

print(scores_df[['Chi','Eng','Math']].sum(axis=0))
print(scores_df[['Chi','Eng','Math']].sum(axis=1))

scores_df['Max'] = scores_df[['Chi','Eng','Math']].max(axis=1)

scores_df['Min'] = scores_df[['Chi','Eng','Math']].min(axis=1)

print(scores_df)

# 小測驗
#scores_df.to_excel('data/scores統計.xlsx')

# endregion

# region apply(axis=0, 1 ) applymap()
# 小測驗
# 所有班級 國英數 各科最高和最低差多少分

# solution 1:
maxSeries= scores_df[['Chi','Eng','Math']].max(axis=0)
minSeries= scores_df[['Chi','Eng','Math']].min(axis=0)

print(maxSeries)
print(minSeries)
print(maxSeries-minSeries)

# solution 2:
print(scores_df[['Chi','Eng','Math']].apply(lambda x: x.max()-x.min(),axis=0))

# 小測驗
# 個人 國英數三科最高和最低差多少分

def peak(series):
    return series.max() - series.min()

print(scores_df[['Chi', 'Eng', 'Math']].apply(lambda x: x.max()-x.min(), axis=1) )
print(scores_df[['Chi', 'Eng', 'Math']].apply(peak, axis=1))

# b    20
# f     0
# d    15
# a    30
# e    30
# c    25

print(scores_df[['Chi', 'Eng', 'Math']].applymap(float))

print(scores_df[['Chi', 'Eng', 'Math']].applymap(lambda x: '{0:.2f}'.format(x)))

f = lambda x: '{0:.2f}'.format(x)
print(scores_df[['Chi', 'Eng', 'Math']].applymap(f))


# endregion

print('end')