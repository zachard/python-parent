# matplotlib绘制自动计算数据的图形

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# edgecolor表示要删除图表中数据点的轮廓, 
# 要指定自定义颜色, 可传递参数c, 可以将其设置为颜色名称, 也可将其设置为一个元组, 
# 其中包含三个0~1之间的小数值, 它们分别表示红色、绿色和蓝色分量, 例如: c=(0, 0, 0.8)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# 使用颜色映射
# 颜色映射(colormap)是一系列颜色, 它们从起始颜色渐变到结束颜色. 
# 在可视化中, 颜色映射用于突出数据的规律, 
# 例如: 你可能用较浅的颜色来显示较小的值, 并使用较深的颜色来显示较大的值
# c被设置成一个y值的列表
# 注: 参数cmap告诉pyplot使用哪个颜色映射, 代码将y值较小的点显示为浅蓝色, 并将y值较大的点显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置标题及坐标标签
plt.title('1-1000的平方', fontsize=24)
plt.xlabel('值', fontsize=14)    # 为X轴设置标题及标题的大小
plt.ylabel('值的平方', fontsize=14)  # 为Y轴设置标题及标题的大小
# which参数表示设置刻度线, 默认为major表示设置主刻度线, minor表示设置副刻度线, both表示同时设置
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])  # 设置每个坐标轴的取值范围, 前两个数为x轴的取值范围, 后两个数为y轴的取值范围
# plt.show()   # 显示图表

# 第一个参数表示要保存图表的名字, 第二个参数表示将图表多余的空白区域裁剪掉
plt.savefig('值的平方.png', bbox_inches='tight')  # 保存图表