import numpy as np
import matplotlib.pyplot as plt


"""subplot() 函数允许你在同一图中绘制不同的东西。"""
# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,  2,  1  )  # 页面分为两行2列，在第1个区域绘制
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  2,  2  ) # 页面分为两行2列，在第2个区域绘制
plt.plot(x, y_cos)
plt.title('Cosine')


t=np.arange(0.0,2.0,0.1)
s=np.sin(t*np.pi)#2×np.pi就相当于2π

plt.subplot(2,2,3)#两行两列,这是第三个图
plt.plot(3*t,s,'m--')
plt.title('123')
plt.ylabel('y3')

plt.subplot(2,2,4)#两行两列,这是第四个图
plt.plot(4*t,s,'k--')
plt.title('456')
plt.ylabel('y4')

# 展示图像
plt.show()


"""subplot(numRows, numCols, plotNum)"""#
# 图表的整个绘图区域被分成 numRows 行和 numCols 列
# 然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1
# plotNum 参数指定创建的 Axes 对象所在的区域
# 如果 numRows ＝ 2, numCols ＝ 3, 那整个绘制图表样式为 2X3 的图片区域, 用坐标表示为
# (1, 1), (1, 2), (1, 3)
# (2, 1), (2, 2), (2, 3)