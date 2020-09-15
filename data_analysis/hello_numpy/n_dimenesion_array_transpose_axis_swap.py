# 数组转置和轴兑换
# 转置是重塑的一种特殊形式, 它返回的是源数据的视图(不会进行任何复制操作). 
# 数组不仅有transpose方法, 还有一个特殊的T属性

import numpy as np

transpose_swap_array = np.arange(15).reshape(3, 5)
print("数组转置和轴对换的初始测试数组为: ")
print(transpose_swap_array)
print("\n")
print("利用数组的T属性对数组进行转置, 结果如下: ")
print(transpose_swap_array.T)
print("转置后原数组为: ")
print(transpose_swap_array)  # 原数组并没有产生改变
print("\n")

# 对于高维数组, transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
hign_dimension_array = np.arange(16).reshape((2, 2, 4))
print("高维数组进行转置初始化数据为: ")
print(hign_dimension_array)
print("\n")
print("利用transpose方法对数组进行转置, 结果如下: ")
print(hign_dimension_array.transpose((1, 0, 2)))
print("转置后, 原始数组为: ")
print(hign_dimension_array)  # 原始数组并未发生改变
print("\n")

print("利用swapaxes方法进行轴交换, 结果如下: ")
print(hign_dimension_array.swapaxes(1, 2))
print("轴交换之后, 原始数组为: ")  # 原始数组并没有发生改变
print(hign_dimension_array)