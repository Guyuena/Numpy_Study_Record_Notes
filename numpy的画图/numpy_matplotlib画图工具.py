import numpy as np

from matplotlib import pyplot as plt   #  pyplot 标出; 绘制(图表);




# 普通不能带中文的画图
x = np.arange(1,11)
y =  2  * x +  5
x2 = np.arange(1,20)
y2 =  1.5 * x2 + 2
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,'ro',x2,y2,'gv')  # 注意格式是组合在一起的  如： ro就是 'r'和‘o’这两个格式的组合
plt.show()


# **kwargs : 第二组或更多(x,y,format_string)
# color : 控制颜色, color='green'
# linestyle : 线条风格, linestyle='dashed'
# marker : 标记风格, marker='o'
# markerfacecolor: 标记颜色, markerfacecolor='blue'
# markersize: 标记尺寸, markersize=20


# b = np.arange(5)
# plt.plot(b,b*1.0,'g.-',b,b*1.5,'rx',b,b*2.0, 'b')
# plt.show()


# plt.plot(x, y, format_string, **kwargs)
# x	X轴数据，列表或数组，可选
# y	Y轴数据，列表或数组
# format_string	控制曲线的格式字符串，可选
"""**kwargs	第二组或更多(x,y,format_string)，可画多条曲线"""
# format_string 由颜色字符、风格字符、标记字符组成
# 颜色字符
# 'b' 蓝色 'm' 洋红色 magenta
# 'g' 绿色 'y' 黄色
# 'r' 红色 'k' 黑色
# 'w' 白色 'c' 青绿色 cyan
# '#008000' RGB某颜色 '0.8' 灰度值字符串
# 多条曲线不指定颜色时，会自动选择不同颜色
# 风格字符
# '‐' 实线
# '‐‐' 破折线
# '‐.' 点划线
# ':' 虚线
# '' ' ' 无线条
# 标记字符
# '.' 点标记
# ',' 像素标记(极小点)
# 'o' 实心圈标记
# 'v' 倒三角标记
# '^' 上三角标记
# '>' 右三角标记
# '<' 左三角标记...等等
#
