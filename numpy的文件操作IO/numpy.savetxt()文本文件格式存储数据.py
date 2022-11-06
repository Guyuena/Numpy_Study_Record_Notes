"""

savetxt()
savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据。

np.loadtxt(FILENAME, dtype=int, delimiter=' ')
np.savetxt(FILENAME, a, fmt="%d", delimiter=",")  文件名、数据源、格式、 分隔符
参数 delimiter 可以指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等。"""

import numpy as np

a = np.array([1, 2, 3, 4, 5])
np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')
print(b)
print('\n')


"""使用 delimiter 参数："""

a1=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("out2.txt",a1,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b2 = np.loadtxt("out2.txt",delimiter=",") # load 时也要指定为逗号分隔

print(b2)