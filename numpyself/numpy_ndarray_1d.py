import numpy as np
# region Create array
arr = np.array([0, 1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.ndim, arr.dtype, arr.shape)
print(arr.size, arr.itemsize, arr.nbytes)


arr = np.arange(1, 100, 2)
print(arr)
print(arr.ndim, arr.dtype, arr.shape)
print(arr.size, arr.itemsize, arr.nbytes)


arr = np.array(["aaa", "bbb", "ccc", "ddd"])
print(arr, arr.dtype)
arr = np.array([True, False, True, False])
print(arr, arr.dtype)
arr = np.array([True, False, 1, 2])
print(arr, arr.dtype)
# endregion

# region 運算  邏輯運算

c1 = np.array([1, 2, 3])
c2 = np.array([4, 5, 6])
print(c1+c2)
print(c1-c2)

print(c1*c2)

c1 = np.array([1, 2, 3])
c2 = np.array([4, 5, 6])
answer = c1 * 2
print(answer)
c1 = np.array([1, 2, 3])
c2 = np.array([4, 5, 6])
print(c1 * [2, 2, 2])
# 邏輯
c1 = np.array([1, 2, 3])
c2 = np.array([4, 5, 6])
print(c1 < c2)
print(c1 > c2)
answer = c1 > c2
print(answer, type(answer), answer.dtype)
if answer.dtype == 'bool':
    print('yes')
else:
    print('no')


arr1 = np.arange(1, 11)
print(arr1)
print((arr1 >= 3) & (arr1 <= 8))
ans1 = arr1 >= 3
ans2 = arr1 <= 8
print(ans1 & ans2)
ans1 = arr1 < 3
ans2 = arr1 > 8
print(ans1)
print(ans2)
print(ans1 | ans2)
print((arr1 < 3) | (arr1 > 8))
answer = arr1 % 2 == 0
print(answer)
print(arr1 == 2)
print(arr1 != 2)
msk = arr1 == 2
print(msk)
print(~msk)
# endregion
# region
arr = np.arange(101)
print(arr[0:4])
print(arr[::-1])
print(arr[-4:])
print(arr[:-4])
print(arr[[0, 2, 4, 6, 8, 10]])
print(arr[[-1, -3, -5, -7, -9, -11]])

ans = (arr >= 3) & (arr <= 8)
print(arr[[ans]])
print(arr[[(arr > 60) & (arr <= 80)]])
print('偶數:', arr[[arr % 2 == 0]])
print('奇數:', arr[[arr % 2 != 0]])
answer = arr.size // 2
print(answer)
print('中間:', arr[[answer]])
print(arr[arr > 90])
print(arr[arr > 90].size > 0)
# endregion
# region
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr[0:4] = 100
print(arr)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = arr[0:4].copy()
arr1[:4] = 100
print(arr1)

arr2 = np.arange(100)
arr2[arr2 <= 49] = 1
arr2[arr2 >= 50] = 2
print(arr2)
arr = np.arange(101)
arr = np.where(arr <= 60, '1', "2")
print(arr)

arr = np.arange(101)
arr = np.where(arr > 5, 2000, 1000)
print(arr)
# endregion
# region
arr = np.arange(101)
print('總和', arr.sum())
print('最小', arr.min())
print('最大', arr.max())
print('平均', arr.mean())
print('中位數', np.median(arr))


# endregion
# region
arr = np.array([1, 55, 44, 332, 11, 99, 33, 44, 11, 22, 100])
arrshort = np.sort(arr)
print(arrshort)
# endregion
