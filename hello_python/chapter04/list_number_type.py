# 通过range()函数生成一系列数字
# 函数range()让Python从你指定的第一个值开始数, 并在到达你指定的第二个值后停止, 因此输出不包含第二个值(这里为5).
for num in range(1,5): 
    print(num)  # 注: 这里只会输出1~4, 不会输出5, 要输出5需要采用range(1,6)

# 通过list()函数将range()生成的一系列数字转换为数值列表
num_list = list(range(1,5))
print('生成的数值列表为: ')
print(num_list)

# range()函数可以指定步长(第三个参数)
print('生成0～10之内的偶数数值列表: ')
even_num_list = list(range(2, 11, 2))
print(even_num_list)

# 利用range()函数输出1~10的平方的数值列表
square_list = []
for num in range(1, 11): 
    square_list.append(num**2)
print('\n')
print('生成1-10的二次方数值列表为: ')
print(square_list)

# 数值列表的简单统计计算
num_statistics_list = [5, 3, 59, 182, 262, 2, 47]
print('\n')
print('用于统计计算的初始化列表为: ')
print(num_statistics_list)
print('通过min函数找出数值列表中最小值为: ' + str(min(num_statistics_list)))
print('通过max函数找出数值列表中最大值为: ' + str(max(num_statistics_list)))
print('通过sum函数求的数值列表的总和为: ' + str(sum(num_statistics_list)))
# 求平均数的函数需要导入其他包

# 列表解析: 简化生成列表的代码
parse_list = [value ** 2 for value in range(1, 10)]
print('\n')
print('通过列表解析生成的数值列表为: ')
print(parse_list)

# 打印3-30范围内可以被3整除的数字
print('\n')
print('3-30范围内可以被3整除的数为: ')
for num_3 in list(range(3, 31, 3)): 
    print(num_3)