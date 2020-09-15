# csv文件格式数据分析

import csv   # 导入csv模块, 用于处理csv文件
from matplotlib import pyplot as plt   # 导入绘图模块
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'  # 2014年07月份的数据
# filename = 'sitka_weather_2014.csv'   # 2014年整年的数据
filename = 'death_valley_2014.csv'      # 包含错误数据的版本
with open(filename) as csv_file:     # 打开csv文件
    # reader处理文件中以逗号分隔的第一行数据, 并将每项数据都作为一个元素存储在列表中
    reader = csv.reader(csv_file)    # 通过csv模块读取csv文件内容
    # print(reader)   # 这里打印出来的结果是一个: <_csv.reader object at 0x10de55dd0> 这样的值
    header_row = next(reader)   # 读取文件的下一行, 因为这里只调用了一次next方法, 所以只得到了文件的第一行
    # print(header_row)    # 打印出来的结果是: ['', '', ...]的格式, 但是原始数据里是没有用[]括起来的

    # 打印文件头(第一行数据)及数据
    # for index, column_header in enumerate(header_row):  # enumerate()函数用于获取每个元素的索引及其值
    #     print(index, column_header)
    
    highs = []   # 用来存储最高气温的列表
    dates = []   # 用来存储日期的列表
    lows = []    # 用来存储最低气温的列表
    # 阅读器对象从其停留的地方继续往下读取CSV文件, 每次都自动返回当前所处位置的下一行
    # for row in reader:   # 遍历csv文件中余下的各行 (注: 如果前面没有调用next(reader), highs列表中会包含表头) 
    #     current_date = datetime.strptime(row[0], "%Y-%m-%d")
    #     dates.append(current_date)   # 获取当前的温度的日期, 转换为相应的格式, 并存储到列表中
    #     highs.append(int(row[1]))   # 获取每行数据的用逗号分隔的第二个值(索引从0开始), 读出来是字符串, 要将它们转换为数字, 其实换成浮点型类型会比较好
    #     lows.append(int(row[3]))    # 获取最低气温并存储到列表

    # 处理错误版本
    for row in reader:   # 遍历csv文件中余下的各行 (注: 如果前面没有调用next(reader), highs列表中会包含表头) 
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError: 
            print(current_date, '数据缺失.')  # current_date并非为字符串, 不能直接和字符串拼接, 但是一个print可以同时打印多个值
        else:
            dates.append(current_date)   # 获取当前的温度的日期, 转换为相应的格式, 并存储到列表中
            highs.append(high)   # 获取每行数据的用逗号分隔的第二个值(索引从0开始), 读出来是字符串, 要将它们转换为数字, 其实换成浮点型类型会比较好
            lows.append(low)    # 获取最低气温并存储到列表
    
    # print(highs)

    # 将最高气温绘制成折线图
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # plt.plot(dates, highs, c='red')   # 绘制图像
    # plt.plot(dates, lows, c='blue')   # 绘制最低气温, 想要在同一幅图画两条折线, 只需要再调用一次plot函数
    
    plt.plot(dates, highs, c='red', alpha=0.5)   # 绘制图像, 实参alpha指定颜色的透明度. alpha值为0表示完全透明, 1(默认设置)表示完全不透明
    plt.plot(dates, lows, c='blue', alpha=0.5)   # 绘制最低气温, 想要在同一幅图画两条折线, 只需要再调用一次plot函数
    # 方法fill_between(), 它接受一个x值系列和两个y值系列, 并填充两个y值系列之间的空间
    # 实参facecolor指定了填充区域的颜色, 实参alpha指定颜色的透明度
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    # 设置图表样式
    # plt.title('2014年07月份日最高气温', fontsize=24)
    # plt.title('2014年日最高气温', fontsize=24)
    # plt.title('2014年日最高和日最低气温', fontsize=24)
    plt.title('2014年错误数据版本', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()    # 绘制斜的数据标签, 以免它们彼此重叠, fig对象和plt对象之间区别是什么? 
    plt.ylabel('温度(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()