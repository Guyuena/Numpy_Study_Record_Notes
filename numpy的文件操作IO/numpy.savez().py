"""numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件中。"""

# numpy.savez(file, *args, **kwds)
# 参数说明：
#
# file：要保存的文件，扩展名为 .npz，如果文件路径末尾没有扩展名 .npz，该扩展名会被自动加上。
# args: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为 arr_0, arr_1, …　。
# kwds: 要保存的数组使用关键字名称。

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
# np.savez("runoob.npz", a, b, c)
np.savez("runoob.npz", a, b, sin=c)  #给C数组一个名字
r = np.load("runoob.npz")
print(r.files)  # 查看各个数组名称
print(r["arr_0"])  # 数组 a
print(r["arr_1"])  # 数组 b
print(r["sin"])  # 数组 c