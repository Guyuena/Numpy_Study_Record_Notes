

"""numpy.save(file, arr, allow_pickle=True, fix_imports=True)"""
#
# file：要保存的文件，扩展名为 .npy，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上。
# arr: 要保存的数组
# allow_pickle: 可选，布尔值，允许使用 Python pickles 保存对象数组，Python 中的 pickle 用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
# fix_imports: 可选，为了方便 Pyhton2 中读取 Python3 保存的数据。

import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)

# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('outfile2', a)