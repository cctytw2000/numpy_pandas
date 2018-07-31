import numpy as np
import matplotlib.pyplot as plt
# region
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
arr1 = np.array([[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
], [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]])
print('二維陣列\n', arr)
print('三維陣列\n', arr1)
print(arr.ndim, arr.dtype, arr.shape)
print(arr.size, arr.itemsize, arr.nbytes)
print(arr[0, 1])
print(arr[0:4, 0:3])
print(arr[(arr > 5) & (arr % 2 == 0)])
# print(arr[[arrmax5 % 2 == 0]])
arr = np.zeros((10, 10))
arr[1:9, 1:9] = 1
arr[arr != 1] = 2
print(arr)
# endregion
# region
arr = np.arange(12)
print(arr)
print(arr.reshape(2, 6))
print(arr.reshape(4, 3))
print(arr.reshape(3, 4))
print(arr.reshape(6, 2))
print(arr.reshape(12))
# endregion
# region
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# 總和
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
# 最大值
print(arr.max())
print(arr.max(0))
print(arr.max(1))
# 最小值
print(arr.min())
print(arr.min(0))
print(arr.min(1))
# 平均值
print(arr.mean())
print(arr.mean(0))
print(arr.mean(1))
# endregion
# region
# arry = np.random.randint(0, 101, (10, 3))
# arrx = np.random.randint(0, 101, (100))
# plt.plot(arrx)
# plt.show()


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
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x[x > 0], y[x > 0], c='g')
plt.scatter(x[x <= 0], y[x <= 0], c='r')
plt.show()
plt.scatter(x[y > 0], y[y > 0], c='g')
plt.scatter(x[y <= 0], y[y <= 0], c='r')
plt.show()

# endregion
