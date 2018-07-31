import numpy as np
import matplotlib.pyplot as plt

# 二維 陣列
# arr [ row, column]

# # 沿著 row 的方向 axis = 0,  沿著column 的方向 axis = 1, 
# axis =0  代表 兩個學生
# axis =1, 代表 每個學生 國英數成績


# region Create 2d ndarray
arr =np.array(
                [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [10,11,12]
                ]
             )
print(arr)



# shape (2,3) tuple 元祖 (兩個列, 三個欄) <class 'tuple'>
print(arr.ndim, arr.shape, arr.dtype)
print(arr.size, arr.itemsize, arr.nbytes)

# arr =np.array(
#                 [
#                     [1,2],
#                     [4,5,6]
#                 ]
#              )

# print(arr.ndim, arr.shape, arr.dtype)
# print(arr.size, arr.itemsize, arr.nbytes)



            

# endregion

# region arr [ row, column] 陣列選取
print(arr[2,2])
print (arr[0:2, 0:2])

print (arr[ : , 0:2])

print (arr[0:2 : , : ])
print (arr[0:2])

print (arr[::-1, :])  # reverser order
print(arr[::-1, ::-1])

print(arr[0:12, 0:12])  # test exception

print (arr[:,[0,2]])
print (arr[arr>5])

# 小測驗 偶數而且>5元素 ; 偶數元素 set 1001 ; else 奇數元素 set  1
print(arr[ (arr %2==0)  &  (arr >5) ])


# 小測驗 周邊 0, 內部 1 -Create a 2d array with 0 on the border and 1 inside (★☆☆)¶ 
arr = np.zeros((10,10))
arr[1:-1,1:-1] = 1
print(arr)

arr = np.ones((10,10))
arr[1:-1,1:-1] = 0
print(arr)



#endregion

# region reshape/T
arr_1d = np.arange(12)
print(arr_1d)

arr_2d = np.arange(12).reshape((3,4))
print (arr_2d)
print (arr_2d.T)


print(np.arange(12).reshape((2,6)))
print(np.arange(12).reshape((6,2)))
print(np.arange(12).reshape((2,2,3))) # 3d

print (arr_2d.reshape((12,)))


# arr 3d
arr_3d =np.array( [
                    [
                        [1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]
                    ],
                    [
                        [1,2,3],
                        [4,5,6],
                        [7,8,9],
                        [10,11,12]
                    ]
                    ]
             )
 
print(arr_3d.ndim, arr.shape, arr.dtype)
print(arr_3d.size, arr.itemsize, arr.nbytes)

print(arr_3d)

# endregion

# region axis
arr =np.array(
                [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ]
             )
print(arr)

# # 沿著 row 的方向 axis = 0,  沿著column 的方向 axis = 1, 
# axis =0  代表 兩個學生
# axis =1, 代表 每個學生 國英數成績

print(arr.sum(axis= None))
print(arr.sum())

print(arr.sum(axis=0))
print(arr.sum(axis=1))

print (arr.mean(0))
print (arr.mean(1))

print (arr.max(0))
print (arr.max(1))

print (arr.min(0))
print (arr.min(1))

print(np.mean([1,2,100,200,333]))
print(np.median([1,2,100,200,333]))


arr = np.array([[3,1],
                [1,4]])
              
print (arr.sort(axis=0)) # sort an array in place
print (arr)


# endregion

# region random  & plt

arr = np.random.randint(60,101,(10,3))
print (arr)


arr = np.array(  np.random.randint(60,101,(100)))
arr.sort() #Sort an array, in-place.

print (arr)

# plot(x, y, color='green', marker='o', markersize=12 ,linestyle='dashed', linewidth=2)
#        
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

# x, y
plt.plot(arr, color='red', marker='x')
plt.show()

years = np.arange(2009,2019)
population = np.random.randint(25,33,(years.size))

plt.plot(years, population, color='green')
plt.plot(years, population*1.5, color='blue',linestyle='dashed', linewidth=2)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Simple Plot')

plt.show()

plt.pie(population, autopct='%.2f %%')  # 只要一個資料參數 y, x 可省略
plt.show()

x = np.random.randn(100)
y = np.random.randn(100)

print(x>0)

plt.scatter(x[x>0], y[x>0], c='r')
plt.scatter(x[x<=0], y[x<=0], c='g')
plt.show()

# 小測驗 scatter y > 0 紅色 
print(y>0)

plt.scatter(x[y>0], y[y>0], c='r')
plt.scatter(x[y<=0], y[y<=0], c='g')
plt.show()

print(x)
print(y)



# 小測驗　冰島人口成長率
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
# endregion

print('end')

