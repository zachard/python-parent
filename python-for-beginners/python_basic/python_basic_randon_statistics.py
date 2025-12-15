# %%
# 频率直方图的纵轴表示数据集中每个数值或数值范围的出现次数。每个数据点或数据范围对应一个
# 柱状条，柱状条的高度表示该数据点或数据范围在数据集中出现的次数。 这种情况下， 直方图所有柱状
# 条的高度之和为样本的数量
# 概率直方图的纵轴表示每个数据点或数据范围在数据集中出现的概率。 直方图所有柱状条的高度之和为 1
import random
import statistics
import matplotlib.pyplot as plt

random.seed(0) # 方便复刻结果
mean1, std1, size1 = 0, 1, 300 # 定义均值，标准差，样本数量
data1 = [random.gauss(mean1, std1) for _ in range(size1)] # 生成300个服从N(0, 1**2)的随机数

# 生成700个服从N(10, 5**2)的随机数 
mean2, std2, size2 = 10, 5, 700
data2 = [random.gauss(mean2, std2) for _ in range(size2)]

# 将两组随机数混合
mixed_data = data1 + data2
mean_loc = statistics.mean(mixed_data) # 计算1000个样本的均值
std_loc  = statistics.stdev(mixed_data) # 计算1000个样本的标准差

# 绘制混合数据的直方图
# bins=30: 将数据分成30个区间
# density=True: 将纵轴表示为概率密度，即所有柱状条的面积总和等于 1。如果
# 设置为 False，纵轴将表示频率，即所有柱状条的高度总和为样本数，即 1000。
# edgecolor='black': 柱状条的边框颜色
# alpha=0.7: 柱状条的透明度
# color='blue': 柱状条的颜色
# label='Mixed data': 柱状条的标签
# Mean: 均值
# Mean ± std: 均值 ± std
plt.hist(mixed_data, bins=30, density=True, edgecolor='black', 
         alpha=0.7, color='blue', label='Mixed data')
# 绘制竖直参考线，用来展示均值位置。 并设置参考线颜色为红色， 以及图例标签。
plt.axvline(mean_loc, color = 'red', label='Mean')
# 绘制竖直参考线，用来展示均值 ± std 位置。 并设置参考线颜色为粉色， 以及图例标签为 Mean ± std。
plt.axvline(mean_loc + std_loc, 
            color = 'pink', label='Mean ± std')
plt.axvline(mean_loc - std_loc, color = 'pink') # 画了两条粉红色的线
plt.xlabel('Value') # 横轴的标签Value
plt.ylabel('Density') # 纵轴的标签Density
plt.legend() # 显示图例
plt.title('Histogram of Mixed Data') # 图形的标题
plt.grid(True) # 显示网格
plt.show() # 显示图形

# %%
# 线性回归
# 导入包
import random
import statistics
import matplotlib.pyplot as plt

# 产生在区间[0, 10)内均匀分布的50个随机数
num = 50
random.seed(0)
x_data = [random.uniform(0, 10) for _ in range(num)]
# 噪音
noise =  [random.gauss(0,1) for _ in range(num)]
y_data = [0.5 * x_data[idx] + 1 + noise[idx]
          for idx in range(num)] # 数据中混入噪音，0.5为斜率， 1为截距

         
# 绘制散点图
fig, ax = plt.subplots()
ax.scatter(x_data, y_data) # 绘制散点图
ax.set_xlabel('x'); ax.set_ylabel('y') # 设置横轴和纵轴的标签
ax.set_aspect('equal', adjustable='box') # 设置横轴和纵轴的比例相等
ax.set_xlim(0,10); ax.set_ylim(-2,8) # 设置横轴和纵轴的取值范围
ax.grid() # 显示网格

# 一元线性回归；对数据进行线性回归，得到斜率和截距
slope, intercept = statistics.linear_regression(x_data, y_data)
print("斜率:", slope, "截距:", intercept)

# 生成一个等差数列
start, end, step = 0, 10, 0.5
x_array = []
x_i = start

while x_i <= end:
    x_array.append(x_i)
    x_i += step

# 计算x_array预测值；相当于根据斜率和截距，计算出一组[x, y]的预测值，用于绘制一元线性回归直线
y_array_predicted = [slope * x_i + intercept for x_i in x_array]

# 可视化一元线性回归直线
fig, ax = plt.subplots()
ax.scatter(x_data, y_data) # 绘制散点图(原始的数据点)
ax.plot(x_array, y_array_predicted, color = 'r') # 绘制一元线性回归直线(函数回归预测的函数曲线)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0,10); ax.set_ylim(-2,8)
ax.grid()
# %%
