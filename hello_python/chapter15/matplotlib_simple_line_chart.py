# 利用matplotlib绘制简单的折线图

import matplotlib.pyplot as plt  # 模块pyplot包含很多用于生成图表的函数

# 解决中文问题-方式一(永久解决)
# 文件路径: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/mpl-data
# 网上(https://www.fontpalace.com/font-details/SimHei/)下载中文字体 SimHei.ttf 安装, 并放到mpl-data/fonts文件夹下面
# print(matplotlib.matplotlib_fname()) 找到相应的配置文件, 修改三项配置
# font.family : sans-serif  这行去掉注释
# font.sans-serif : SimHei, Bitstream Vera Sans  这行加入前面的SimHei字体
# axes.unicode_minus:False 这行去掉注释, 解决负号'-'显示为方块的问题
# from matplotlib.font_manager import _rebuild
# _rebuild() 重新加载一下字体(尤其重要)

# 解决中文问题-方式二(每次都需要, 其实这样添加可以防止环境不一致的问题)
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签, 系统应该要安装SimHei字体
# plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号

# 当你向plot()提供一系列数字时, 它假设第一个数据点对应的x坐标值为0
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]   # 需要绘制图形的数据

# plt.plot(squares, linewidth=5)     # 绘制图形, linewidth表示折线图线条的粗细
plt.plot(input_values, squares, linewidth=5)  # 指定input_values为输入值, 确保x轴坐标是正确的

plt.title('平方数', fontsize=24)  # 指定图表的标题, 及标题的字体大小
plt.xlabel('值', fontsize=14)    # 为X轴设置标题及标题的大小
plt.ylabel('值的平方', fontsize=14)  # 为Y轴设置标题及标题的大小

# 设置刻度样式, both表示将x轴和y轴的字号都设置为14, x表示只设置x轴的字号, y表示只设置y轴的字号
plt.tick_params(axis='both', labelsize=14)

plt.show()            # 显示绘制的图形

# 使用scatter绘制散点图
# 要绘制单个点, 可使用函数scatter(), 并向它传递一对x和y坐标, 它将在指定位置绘制一个点

# plt.scatter(2, 4, s=200)  # 传入x,y的坐标, 绘制单个散点, s表示单个点的大小

x_values = [1, 2, 3, 4, 5]     # 使用scatter绘制一系列的点
y_values = [1, 4, 9, 16, 25]   # x_values和y_values长度需要一致, 否则绘图时程序报错
plt.scatter(x_values, y_values, s=100)

plt.title('平方数', fontsize=24)  # 指定图表的标题, 及标题的字体大小
plt.xlabel('值', fontsize=14)    # 为X轴设置标题及标题的大小
plt.ylabel('值的平方', fontsize=14)  # 为Y轴设置标题及标题的大小

# which参数表示设置刻度线, 默认为major表示设置主刻度线, minor表示设置副刻度线, both表示同时设置
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()