import pygal

from pygal_die import Die

die_nums = []  # 定义一个空列表来存储每次同骰子的值
d6 = Die()    # 创建一个默认为6个面的骰子
times = 1000   # 投骰子的次数

# 进行100次投骰子操作, 将每次的结果保存到列表
while times > 0:
    die_nums.append(d6.roll())
    times = times - 1

# 分析结果, 分别记录每个骰子每面出现的次数
frequencies = []  # 记录骰子的每一面出现次数的列表
for die_num_side in range(1, d6.num_sizes+1): 
    frequencie = die_nums.count(die_num_side)  # 列表的count函数可以直接计算出元素出现的次数
    frequencies.append(frequencie)

#教科书的循环方法
# for roll_num in range(100):
#     die_nums.append(d6.roll())

# print(die_nums)    # 打印随机出现的投骰子的次数
# print(frequencies)   # 打印投骰子每个点数出现的次数

# 对每次头骰子次数进行可视化
hist = pygal.Bar()    # 用于创建条形图

hist.title = '一个六面的骰子投掷1000出现的频次结果'    # 设置图形的标题
hist.x_labels = ['1', '2', '3', '4', '5', '6']    # 设置x轴的标签
hist.x_title = '点数'    # x轴的坐标标题
hist.y_title = '出现次数'  # y轴的坐标标题

hist.add('D6', frequencies)    # 将一系列值添加到图表中, 这只是添加到图表中的一个类型, 还可以添加其他类型
hist.render_to_file('pygal_roll_die_6_result.svg')   # 将图表渲染保存到svg文件