from matplotlib import pyplot as plt
import numpy as np


"""Matplotlib 可以将直方图的数字表示转换为图形。 pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。"""
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()


# matplotlib.pyplot.hist(

# x, bins=10, range=None, normed=False,
# weights=None, cumulative=False, bottom=None,
# histtype=u’bar’, align=u’mid’, orientation=u’vertical’,
# rwidth=None, log=False, color=None, label=None, stacked=False,
# hold=None, **kwargs)