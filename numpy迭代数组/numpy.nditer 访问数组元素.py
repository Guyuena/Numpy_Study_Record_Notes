import numpy as np

a = np.arange(6).reshape(2, 3)
print('原始数组是：')
print(a)
print('迭代输出元素：')
for x in np.nditer(a):  # n-dimension-arrar-iterator
    print(x, end=", ") # 用,来分隔元素
print('\n')

# for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
# for x in np.nditer(a.T, order='C'):C order，即是行序优先；

"即是列序优先"
for x in np.nditer(a,order='F'):
    print(x, end=", ")

print('\n')
"即是行序优先；"
for x in np.nditer(a,order='C'):
    print(x, end=", ")
print('\n')


"""广播迭代   同时迭代数组
如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 
假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。"""

import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('\n')
print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')
print('修改后的数组为：')
for x, y in np.nditer([a, b]):  # 同时迭代访问两个数组,注意这两个数组的（列数）要相同
    print("%d:%d" % (x, y), end=", ")  # 输出效果是：  一个a数组的元素:一个b数组的元素