# 绘制随机漫步图形

import matplotlib.pyplot as plt  # 导入系统包

from random_walk_def import RandomWalk  # 导入自定义的类

while True: 
    rw = RandomWalk(50000)
    rw.fill_walk()   # 开始随机漫步, 获取随机漫步的点

    point_numbers = list(range(rw.num_points))  # range函数只指定了一个参数, 表示从0到rw.num_points, 这里生成的点一定是num_points个, len(self.x_values) == num_points

    # 需要给形参figsize指定一个元组, 向matplotlib指出绘图窗口的尺寸, 单位为英寸. 
    # dpi表示对应的分辨率
    plt.figure(dpi=128, figsize=(10, 6))   # 指定绘制图像的大小、分辨率等数据

    # rw.x_values和rw.y_values不应该作为c的参数值, 因为它不会是一个递增的数组, 而edgecolor表示去除数据点的边缘
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)  # 通过scatter绘制随机漫步的图形, 其实就是取随机漫步类存储的一系列坐标点绘图
    
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)  # 在(0,0)位置上重新绘制, 覆盖之前的点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100) # 重新绘制终点, 覆盖之前的点
    
    # 隐藏坐标轴 axes()方法是获取图形的坐标轴? 
    plt.axes().get_xaxis().set_visible(False)   # 隐藏x坐标轴
    plt.axes().get_yaxis().set_visible(False)   # 隐藏y坐标轴

    plt.show() # 展示图形

    keep_running = input('是否生成另外一个随机漫步图形?(y/n) ')

    if keep_running == 'n':   # 通过输入n的标志来表示退出
        break