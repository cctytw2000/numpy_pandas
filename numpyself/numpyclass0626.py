import numpy as np
import time
mylist = [3, 6, 9, 18, 32, 64]
print(mylist*30)
list1 = []
for n in mylist:
    list1.append(n*30)
print(list1)
# =============================
arr = np.array(mylist)
print(arr)
print(arr*30)
print(arr*29.9)
# =============================
mylist = range(10000000)

list1 = []
start = time.time()
for n in mylist:
    list1.append(n*30)
end = time.time()
print(end - start, '秒')
#=============================
list1 = []
start = time.time()
list1=[n for n in mylist]
end = time.time()
print(end - start, '秒')
# =============================
arr = np.array(mylist)
start = time.time()
arr = arr * 30
end = time.time()
print(end - start, '秒')


# =============================
