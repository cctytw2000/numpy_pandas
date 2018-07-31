import numpy as np
import time

# problem:　
# How do I multiply each element in a list by a number?

myList = [3,4,5,62,33]
print(myList * 30)      # 計算美金
# print(myList * 29.9)  # type error

list1 = []
for n in myList:
    list1.append( n*30)

print(list1)

# ==============================
arr =  np.array(myList)
print (arr)
print (arr * 30)             # arr 的所有元素 * 30 (批次元素運算)
print (arr * 29.9)


#===============================

myList = range(10000000)

list1 = []
start = time.time()
for n in myList:
    list1.append( n*30)
end = time.time()
print (end-start, '秒')


start = time.time()
list2 = [n for n in myList]    # list (串列生成式)
end = time.time()
print (end-start, '秒')

# ==============================
arr =  np.array(myList)
start = time.time()
arr = arr * 30             # arr 的所有元素 * 30 (批次元素運算)
end = time.time()
print (end-start, '秒')