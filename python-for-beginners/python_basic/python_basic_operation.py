# %%
# +号字符串拼接
str_a = "10"    # str(a)
str_b = "20.0"  # str(b)
str_c = str_a + str_b
print(str_c)  

# %%
# *号字符串复制
str_a = "10"    # str(a)
str_b = "20.0"  # str(b)
str_c = str_a * 3
str_d = str_b * 2
print(str_c)
print(str_d)

# print(str_c * str_d) # 语法报错

# %%
# **用于计算数值的幂次方
a = 2
print(a**3)

# %%
# not用于取反操作，等同于!
print(not True)
print(not False)

# print(!True) # 语法报错

# %%
# and用于逻辑与操作，等同于&&
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# %%
# or用于逻辑或操作，等同于||
print(True or True)
print(True or False)
print(False or True)

# %%
# in,not in用于判断元素是否在列表中
# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 判断元素是否在列表中
print(3 in my_list)  # True
print(6 in my_list)  # False
# 判断元素是否不在列表中
print(3 not in my_list)  # False
print(6 not in my_list)  # True

# %%
# is,is not用于判断两个对象是否是引用同一个内存地址
import copy
a = [1, 2, 3]
b = a  # 视图 b 引用 a 的内存地址
c = [1, 2, 3]
d = a.copy()

print(a is b) # 输出 True，因为 a 和 b 引用同一个内存地址
print(a is not c) # 输出 True，因为 a 和 c 引用不同的内存地址
print(a == c) # 输出 True，因为 a 和 c 的值相等
print(a is not d) # 输出 True，因为 a 和 d 引用不同的内存地址
print(a == d) # 输出 True，因为 a 和 d 的值相等

a_2_layers = [1, 2, [3, 4]]
a_2_layers
d_2_layers = a_2_layers.copy()  # 浅复制
d_2_layers
e_2_layers = copy.deepcopy(a_2_layers) # 深复制
e_2_layers

print(a_2_layers is d_2_layers) # 输出False，因为a_2_layers和d_2_layers引用不同的内存地址
print(a_2_layers[2] is d_2_layers[2]) # 请特别关注: 输出True，因为a_2_layers和d_2_layers的[2]引用同一个内存地址(浅复制只复制最外层)
print(a_2_layers is e_2_layers) # 输出False，因为a_2_layers和e_2_layers引用不同的内存地址
print(a_2_layers[2] is e_2_layers[2]) # 输出False，因为a_2_layers和e_2_layers的[2]引用不同的内存地址(深复制复制了所有层级)

# %%
