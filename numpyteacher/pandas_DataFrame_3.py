import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dic ={
         'Name':['aaa' ,'bbb','ccc','ddd','eee','fff'] ,
         'Gender':['Male','Male','Female','Female','Female','Female'],
         'Class':['CS_101', 'CS_101','CS_101', 'CS_102','CS_101', 'CS_102' ],
         'Chi':[80, 100, 60, 80, 80, 80],
         'Eng':[80, 80, 50, 70, 80, 80],
         'Math':[50, 100, 75, 85, 50, 80]
     } 
        
scores_df = pd.DataFrame(dic ,  
            columns=['Name', 'Gender', 'Class', 'Chi', 'Eng','Math'],
            index=list('abcdef') )

print(scores_df.groupby('Class').mean())
print(scores_df.groupby('Class').max())


print(scores_df.groupby('Class').apply(lambda df: df.head(2)))
print(scores_df.groupby('Class').apply(lambda df: df.describe()))

print(scores_df.groupby('Class').apply(np.mean, axis = 0))
print(scores_df.groupby('Class').apply(np.mean, axis = 1))

# 復合的 groupkey
print(scores_df.groupby(['Class','Gender'])['Math'].mean())  # multi -index
print(scores_df.groupby(['Class','Gender'])['Math'].mean().unstack())

print(scores_df.pivot_table(index='Class',columns='Gender', values='Math',aggfunc='mean'))


# # region DataFrame 資料排序 (axis =0 or 1)

# 各科排序 , 前幾名	
print(scores_df['Math'].sort_values(ascending=False).head(3)) 

print(scores_df.sort_values(by='Math', ascending=False).head(3))
print(scores_df.sort_values(by='Chi', ascending=False, inplace=True))
print(scores_df.sort_values(by=['Chi','Math']))                           
print(scores_df.sort_values(by=['Chi','Math'], ascending= [True, False]))  

print(scores_df.sort_index(ascending=False))         # axis = 0 依 row index
print(scores_df.sort_index(axis=1, ascending=False)) # axis = 1 依欄位

# endregion

# region plot
# series plot
print(scores_df['Class'].value_counts())
scores_df['Class'].value_counts().plot.pie()
plt.show()


# endregion
