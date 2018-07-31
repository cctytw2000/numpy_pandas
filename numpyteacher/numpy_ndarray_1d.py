import numpy as np

# region Create ndarray
arr = np.array([1,2,3,4,5])
print (arr)
print (type(arr))

print(arr.ndim, arr.shape, arr.dtype)
print(arr.size, arr.itemsize, arr.nbytes)

arr = np.arange(10)
print(arr)

arr = np.arange(1, 100, 2)
print(arr)

# 小測驗 TODO 陣列元素值 5~49 find the memory size of any array
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

# endregion

# region 數學運算 & 邏輯運算


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print (arr1 + arr2)
print(arr2 - arr1)
print(arr2 * arr1)
print(arr2 / arr1)

arr1 = arr1 * 2
print(arr1)

arr1 = np.array([1,2,3])
# arr1 = arr1 * [2, 2, 2]
arr1 = arr1 * np.array([2,2,2]) 
print (arr1)

# logic 邏輯運算 => boolean array
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print (arr1 > arr2)
print (arr2 > arr1)

mask = arr1 > arr2
print(mask, type(mask), mask.dtype)


arr= np.array([1,2,3,4,5,6,7,8,9,10])
print (arr > 5)

cond1 = arr >=3
cond2 = arr <=8
print ((arr >= 3) & (arr <=8)) # 中間級分同學, 加上括號優先運算
print (cond1 & cond2)

cond1 = arr <3
cond2 = arr >8
print(cond1)
print(cond2)
print (cond1 | cond2)
print ((arr < 3) | (arr > 8))  # 較差和較好 級分

# 小測驗 陣列個元素是否為偶數
# [False True False...]
print (arr % 2 == 0 )

print (arr ==2)
print (arr !=2)

mask = (arr == 2)
print (mask)          # 陣列個元素是否為2
print (~mask)         # 陣列個元素不是 2
# endregion

# region arr [ index...] 陣列選取

arr = np.array([0,100,2,3,4,5,6,7,8,9,10])
print(arr[4])
print (arr[3:9])
print(arr[3:9:2])

print (arr[:4])
print (arr[4:])

print(arr[:])
print(arr[::1])
print(arr[::3])

print(arr[-4:])
print(arr[:-1])   # 不包括 -1 (最後元素)

# 小測驗 陣列倒著排 reverse order
print (arr[::-1])

# 相對於list, 比較特別的索引子 fancy index (int list index)  &   boolean array index  
print(arr[[1,3,5]])
print (arr[[2,4,6]])

arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[[True, True, True,  False, False, False, False, False , False, False]])

mask = arr>5

print (arr)             # [0     1      2      3     4     5     6     7     8    9]
print (mask)            # [False False False False False False  True  True  True  True]
print(arr[mask])

print(arr[arr>5])  # 解讀 : for 陣列的每個元素, where 判斷索引子條件是否是 true, 如果是就 select 出來 

# 小測驗 找陣列偶數元素
#        找陣列奇數元素

arr = np.array([0,11,21,33,84,55,66,77,8,9])
print (arr[arr %2 ==0])
print (arr[arr %2 ==1])

# 小測驗 找陣列中間級
#       較差和較好 級分
print (arr[(arr>=50) & (arr<=80)])
mask = (arr>=50) & (arr<=80)
print (arr[mask])
print(arr[~mask])

# 小測驗 hint size / Any()
# 有沒有任何一個元素 > 90 ?    True or False
# print (arr[arr>90].size > 0)

# 是不是任何一個元素 都大於 5 ? True or False



# endregion

# region view or copy
arr = np.array([0,1,2,3,4,5,6,7,8,9,10])
# working view 
arr[0:4] = 100
print (arr)

# working copy
arr1 = arr[0:4].copy()
arr1[:4] = 999
print(arr)

#=======================
arr = np.arange(100)
# working view 
arr[arr <5] = 0
arr[arr>=5] = 1000
print (arr)

arr = np.arange(100)
result = np.where(arr<5, 0, 1000)  #np.where(條件,如果條件達成,如果沒有達成)
print (result)

# 小測驗 陣列 0~99,  < 5 變 1000; >= 5 變 2000
arr = np.arange(100)
arr[arr <5] = 1000
arr[arr>=5] = 2000
print (arr)


# solution 1:
arr=np.arange(100)
arr = np.where(arr < 5, 1000, 2000)  # as if-else 兩條路走一條路
print(arr)

# solution 2:
arr=np.arange(100)
mask1 = arr < 5
arr[mask1] = 1000
arr[~mask1] = 2000
print(arr)

# endregion

# region aggregaion sum() max () / sort.....

# Universal Functions (ufunc)
# NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, 
# these are called “universal functions”(ufunc). 
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
arr = np.array([1,2,3,4,5,6,7,8,9,10])

print('sum ', arr.sum())
print('sum ', np.sum(arr))

print(arr.min())
print(arr.max())
print(arr.mean())

print(np.median(arr))
print(np.sin(arr))

# 小測驗 學生成績 平均分 / 權重後的平均, 
arr = np.array([90,90,100])               # 三科分數
arr_weight = np.array([0.25,0.25, 0.5])   # 三科分數權重

print(arr.mean())
print( (arr * arr_weight).sum())

# sort
arr = np.array([1,23,44,55,100,99,60])
print(np.sort(arr)) 
print (arr)

arr = np.sort(arr)
print (arr)

# ===============================
arr = np.array([1,23,44,55,100,99,60])
arr.sort()       # Sort an array, in-place.       
print(arr)
print(arr[::-1])  # reverse order

print(reversed(arr))
print (arr.sum)

iterator = reversed(arr)
for n in iterator:
    print (n)

# endregion

# region 小測驗 TODO
# 練習球隊範例 array 各 size 6
players = [56,  8, 19, 14, 6, 71]                                           # list 球隊人數
teams = ['Apple ', 'Orange', 'pineApple', 'Big Apple', 'Bananna', 'Cherry'] # list 球隊 Team

# print(players  > 30)
# print (players *3)

plaryes_arr = np.array(players)
teams_arr= np.array(teams)

# players 總共有幾人 ? 
# Team 總共有幾隊 ? 

# 最多的人的 team 是幾人 ?

# 最多的人的 team 是哪個 team ?
print(teams_arr[[False, False, False, False, False, True]])
print (teams_arr[[plaryes_arr==71]])
# 哪一隊最多人 ?
# 人數大於 10 的組別 ?

# 除了cherry組以外的 players 總數 ?
# endregion

print('end')
