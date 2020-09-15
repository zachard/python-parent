# ndarray(NumPy数组)不用编写循环即可对数据执行批量运算

import numpy as np

# 创建一个ndarray
arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])  # 根据二维序列创建一个多维数组
print("初始化的数组为: ")
print(arr1)
print("\n")

arr2 = np.array([[7., 8., 9.], [10., 11., 12.]])
print("第二个初始化的数组为: ")
print(arr2)
print("\n")

arr3 = np.array([13., 14., 15.])
print("初始化一个单维数组: ")
print(arr3)
print("\n")

arr4 = np.array([16., 17.])
print("初始化第二个单维数组: ")
print(arr4)
print("\n")

# 对数组进行自乘操作
print("对数组进行自乘操作后结果为: ")
print(arr1 * arr1)  # 每个位置上对应的元素相乘
print("\n")

print("arr1 * arr2的结果为: ")
print(arr1 * arr2)
print("\n")

print("两个维度不相同的数组相乘, 操作结果为: ")
print(arr1 * arr3)  # 第一个数组的每一维乘以第二个数组
print("\n")
print(arr3 * arr1)
print("\n")
# print(arr1 * arr4)   # 运算出现错误, 长度不统一, 不允许操作
# print("\n")
# print(arr4 * arr1)
# print("\n")

# 对数组进行相减操作
print("数组对自身进行相减操作: ")
print(arr1 - arr1)
print("\n")
print(arr1 + arr2)
print("\n")
print(arr1 + arr3)
print("\n")
# print(arr1 - arr4)   # 运算出现错误, 维度不相同, 不允许操作
# print("\n")

# 数组与标量的算术运算会将标量值传播到各个元素
print("将数组的值乘以0.5: ")
print(arr1 * 0.5)
print("\n")

# 大小相同的数组之间的比较会生成布尔值数组
print("对arr1和arr2两个数组进行大小比较: ")
print(arr1 < arr2)
print("\n")
print("对arr1和arr3两个数组进行大小比较: ")
print(arr1 < arr3)
print("\n")
# print("对arr1和arr4两个数组进行大小比较: ")
# print(arr1 < arr4)    # 运算出现异常, 维度不统一, 不能进行运算
# print("\n")

# 基本的索引和切片
index_arr = np.arange(10)  # 创建一个1*10的ndarray
print("创建一个简单的1*10的数组结果为: ")
print(index_arr)
print("\n")
print("获取数组中索引为5的(第6个)元素: ")
print(index_arr[5])    # 通过数组索引获取元素
print("\n")
print("获取数组中索引为5到8(不包含)的元素: ")
print(index_arr[5:8])  # 数组的切片功能
print("\n")
index_arr[5:8] = 12   # 修改切片的值, 值会自动传播到整个选区
# 跟列表最重要的区别在于, ndarray数组切片是原始数组的视图. 
# 这意味着数据不会被复制, 视图上的任何修改都会直接反映到源数组上.(会修改原始数组的值)
print(index_arr)
print("\n")

# 切片改变初始数据源值的示例
print("=====切片改变初始数据源值的示例开始=====")
print("当前初始数据源值为: ")
print(index_arr)

index_arr_slice = index_arr[5:8]  # 如果想要得到的是ndarray切片的一份副本而非视图, 就需要明确地进行复制操作, 例如: arr[5:8].copy()
print("创造一个索引为5到8的切片, 结果为: ")
print(index_arr_slice)

index_arr_slice[1] = 12345
print("改变切片中索引为1的值, 改变后的切片结果为: ")
print(index_arr_slice)
print("改变后的初始数据源为: ")
print(index_arr)   # 初始数据源的值也改变了

index_arr_slice[:] = 64 
print("对切片进行再切片, 并改变新切片中的值, 切片的值为: ")
print(index_arr_slice)
print("改变后的初始数据源为: ")
print(index_arr)
print("=====切片改变初始数据源值的示例结束=====")
print("\n")

# 高维数组的索引
index_arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 创建一个3*3的数组
print("多维数组各索引位置上的元素不再是标量而是数组: ")
print(index_arr2d[2])
print("\n")
print("可以通过索引列表的方式来选取单个元素: ")
print(index_arr2d[2][1])  # [a][b]和[a, b]的索引方式结果是一样的
print(index_arr2d[2, 1])
print("\n")

# 在多维数组中, 如果省略了后面的索引, 
# 则返回对象会是一个维度低一点的ndarray(它含有高一级维度上的所有数据)
index_arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("初始化2*2*3的数组结果为: ")
print(index_arr3d)
print("\n")
print("index_arr3d[0]将返回一个2*3的数组: ")
print(index_arr3d[0])
print("\n")

# 标量值和数组都可以被赋值给索引出来的数组
old_values = index_arr3d[0].copy()  # 将索引出来的数组赋值给old_values
index_arr3d[0] = 42  # 将标量值赋值给索引出来的数组, 以改变原数组的值
print("将标量值赋给索引出来的数组后, 原数组结果为: ")
print(index_arr3d)
print("\n")
print("将数组赋给索引出来的数组, 原数组结果为: ")
index_arr3d[0] = old_values
print(index_arr3d)
print("\n")

# 多维数组的切片
print("多维数组切片的原始数组为: ")
print(index_arr2d)
print("index_arr2d[:2]表示沿着一个轴选取元素: ")
print(index_arr2d[:2])  # 注意理解, 由一个3*3的数组切片成为了2*3的数组
print("传入多个切片时, 切片结果为: ")
print(index_arr2d[:2, 1:])  # 先进行:2的切片, 再进行1:的切片, 由一个3*3的数组切片成为了2*2的数组
print("通过索引与切片的混合, 得到低维度的切片, 结果为: ")
print(index_arr2d[1, :2])  # 先索引得到一个一维数组, 再切片其中的元素
print("\n")
print(index_arr2d[:2, 2])  # 先索引得到一个2ndim的数组, 再索引每个数组中单个元素组成一个一维数组
print("\n")
print("对高维轴进行切片的示例: ")
print(index_arr2d[:, :1])
print("\n")

# 布尔型索引
# 通过布尔型索引选取数组中的数据, 将总是创建数据的副本, 即使返回一模一样的数组也是如此
index_names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) # 将一个列表转换为ndarray字符串数组
print("初始化的字符串数组为: ")
print(index_names)
index_data = np.random.randn(7, 4)  # 随机生成一个7*4符合正态分布的数组
print("初始化的7*4的数组为: ")
print(index_data)
print("\n")
print("选出字符串中符合特定条件的行, 通过相等于进行比较: ")
# 还可使用其他条件, 比如: index_names != "Bob", ~(index_names == "Bob"), 
# 及使用 & 和 | 运算符, 比如: (index_names == "Bob") | (index_names == "Will")
print(index_names == "Bob")
print("\n")
print("用布尔型数组对数组进行索引: ")  # 布尔型数组的长度必须跟被索引的轴长度一致
print(index_data[index_names == "Bob"])  # 满足条件的行会被索引出来
print("\n")
print("布尔型索引与整数索引/切片混合使用, 结果为: ")
print(index_data[index_names == 'Bob', 2:])  # 结合切片使用
print("\n")
print(index_data[index_names == 'Bob', 3])
print("\n")
index_data[index_names == 'Bob', 3] = 0
print("改变布尔型索引的值, 修改后的值为: ")
print(index_data[index_names == 'Bob', 3])
print("修改布尔型索引值后, 原数据结果(同步修改)为: ")
print(index_data)
print("\n")

print("通过布尔型索引将数组中的负值修改为0: ")
index_data[index_data < 0] = 0  # 修改值
print(index_data)
print("\n")

# 花式索引: 一个NumPy术语, 指的是利用整数数组进行索引
# 无论数组是多少维, 花式索引总是一维的(注是花式索引是一维的, 而不是索引出来的结果是一维的)
# 花式索引跟切片不一样, 它总是将数据复制到新数组中. 
fancy_index = np.empty((8, 4))  # 创建一个8 * 4的空数组
for i in range(8):
    fancy_index[i] = np.random.randn(1, 4)    # 对空数组进行赋值

print("花式索引的初始化测试数据为: ")
print(fancy_index)
print("\n")
print("同时获取数组中多个索引组成新的数组: ")
print(fancy_index[[4, 3, 0, 6]])  # 例如: 获取索引下标为4, 3, 0和6的数组组成新的数组
print("\n")
print("使用负数索引从末尾开始选取行: ")
print(fancy_index[[-3, -5, -7]])
print("\n")

# 一次传入多个索引数组会返回一个一维数组
multi_array_index = np.arange(32).reshape((8, 4))
print("一次传入多个索引数组的初始测试数据为: ")
print(multi_array_index)
print("\n")
print("通过多个索引数组截取出一个一维数组: ")
# 相当于取(1, 0), (5, 3), (7, 1), (2, 2)位置上的元素组成一个一维数组
print(multi_array_index[[1, 5, 7, 2], [0, 3, 1, 2]])
print("\n")
# print(multi_array_index[[1, 5, 7, 2], [0, 4, 1, 2]])  # 报错, 数组越界了
# print(multi_array_index[[1, 5, 7, 2], [0, 3, 1]])  # 报错, 两个索引数组的长度不一致

print("一个预期结果不一致的花式索引, 结果如下: ")
print(multi_array_index[[1, 5, 7, 2]][:, [0, 3, 1, 2]])  # 预期应与multi_array_index[[1, 5, 7, 2], [0, 3, 1, 2]]结果一致