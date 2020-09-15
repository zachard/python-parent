# NumPy可以创建一个N维数组对象ndarray
# ndarray是一个通用的同构数据多维容器, 
# 也就是说, 其中的所有元素必须是相同类型的. 
# 每个数组都有一个shape(一个表示各维度大小的元组)和一个dtype(一个用于说明数组数据类型的对象)

import numpy as np 

# randn函数返回一个(没有参数时)或一组样本, 具有标准正态分布
nd_data = np.random.randn()
print("传入一个参数时: ")
print(nd_data)
print("\n")

nd_data = np.random.randn(2, 3)   # 返回一个2行, 3列的数组
print("传入两个参数时: ")
print(nd_data)   # 输出数组对象
print("\n")

print("对数组 * 10: ")
nd_data = nd_data * 10   # 不需要进行for循环操作
print(nd_data)
print("\n")

print("对数组进行自加: ")
print(nd_data + nd_data)  # 不需要进行for循环
print("\n")

print("使用shape获取多维度容器的各维度大小: ")
print(nd_data.shape)
print("\n")

print("使用dtype获取多维度容器的数据类型: ")
print(nd_data.dtype)
print("\n")

# nd_data = np.random.randn(2, 3, 4)
# print("传入三个参数时: ")
# print(nd_data)
# print("\n")

# 使用numpy的array函数创建ndarray
# array函数接受一切序列型的对象(包括其他数组), 然后产生一个新的含有传入数据的NumPy数组

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1, dtype=np.float64)  # dtype用于指定数组的数据类型
print("将一个列表传入array函数, 以创建ndarray: ")
print(arr1)   # 这个输入结果我有点没看懂, 相当于将Python的一个简单数组转换为ndarray对象? 
print("arr1数组各维度的大小为: ")
print(arr1.shape)
print("arr1的数据类型为: ")
print(arr1.dtype)
arr1 = arr1.astype(np.int32)
print("将float64数据类型转换为int32类型: ")
print(arr1.dtype)
print("转换后的小数部分将被舍去: ")
print(arr1)
print("\n")

# 将一个嵌套序列转换为多维数组  
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2, dtype=np.int32)   # 利用array函数将嵌套序列转换为多维数组
print("将一个嵌套序列转换为多维数组: ")
print(data2)
print("arr2数组的各维度大小为: ")
print(arr2.shape)
print("arr2数组的数据类型为: ")
print(arr2.dtype)
arr2 = arr2.astype(np.float64)
print("将int32类型的数据转换为float64类型: ")
print(arr2.dtype)
print("转换后的结果为: ")
print(arr2)
print("arr2数组的维度为: ")
print(arr2.ndim)   # 注意这个参数的含义: 表示最外围维度的大小
print("\n")

# 通过zeros函数创建值为0的数组
zeros1 = np.zeros(10)  # 创建一个1*10的值全部为0的数组, 数据类型默认为浮点型
print(zeros1)
print("zeros1各维度大小为: ")
print(zeros1.shape)
print("zeros1数组的数据类型为: ")
print(zeros1.dtype)
print("\n")

zeros2 = np.zeros((3, 6))  # 传入的参数为一个元组
print("用zeros函数创建一个3*6的数组: ")
print(zeros2)
print("zeros2各维度大小为: ")
print(zeros2.shape)
print(zeros2.ndim)
print("\n")

# 通过ones函数创建值为1的数组
ones1 = np.ones((2, 3))
print("创建一个2*3值全部为1的数组: ")
print(ones1)
print("ones1各维度的大小为: ")
print(ones1.shape)
print("\n")

# 利用empty创建没有任何具体值的数组, 只分配内存空间, 但不填充任何值
# 认为np.empty会返回全0数组的想法是不安全的. 
# 很多情况下(如前所示), 它返回的都是一些未初始化的垃圾值.
empty1 = np.empty((2, 3, 2))
print("创建一个2*3*2的空数组: ")
print(empty1)
print("empty1各维度的大小为: ")
print(empty1.shape)
print("empty1的数据类型为: ")
print(empty1.dtype)
print("\n")

# 利用arange函数创建一个数组
arange1 = np.arange(15)
print("利用arange创建的数组为: ")  # 维度为 1*15
print(arange1)
print("arange1各维度大小为: ")
print(arange1.shape)
print(arange1.ndim)
print("\n")

# 如果某字符串数组表示的全是数字, 也可以用astype将其转换为数值形式
# 使用numpy.string_类型时, 一定要小心, 因为NumPy的字符串数据是大小固定的, 
# 发生截取时, 不会发出警告. 
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print("字符串类型的数组为: ")
print(numeric_strings)
numeric_strings = numeric_strings.astype(np.float)
print("字符串类型数组转换为浮点型数组为: ")
print(numeric_strings)
print("\n")