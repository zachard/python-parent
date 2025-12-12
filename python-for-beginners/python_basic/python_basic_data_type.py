# %%
def my_function(x, y):
    """
    这个自定义函数计算两个数值x和y的和
    函数输入为:
        x: The first number to be added.
        y: The second number to be added.
    函数输出为:
        The sum of x and y.
    """
    return x + y;

# 调用函数，打印输出结果
print(my_function(1.5, 2))

# %%
# 导入包
import numpy as np

from numpy import array # 从包中导入部分模块或函数

# %%
# Python中的变量值，True、False、None要注意首字母大写

# 在Python中定义一个复数
# z = 8 + 8j # 复数，实部为8，虚部为8; z=8+8J
# 另外一种写法: 
#z = complex(8, 8) # 等同于z = complex(real=8, imag=8)
z = complex(imag=8, real=8) # real表示实部，imag表示虚部
print(z)

a = 8.8e3 # 8.8乘以10的3次方
b = 8.8e-3 # 8.8乘以10的-3次方
print(a)
print(b)

# %%
y = 8
int_to_complex = complex(y) # 将整数转换为复数，虚部为0
print(int_to_complex)

# %%
# Python的字符串处理
str1 = 'I am learning Python 101!'
print(str1)

str2 = "Python is fun. Machine learning is fun too."
print(str2)

# 使用加号 + 将多个字符串连接起来
str4 = 'Hey, ' + 'James!'
print(str4) 

# 使用乘号*将一个字符串复制多次
str5 = 'Python is FUN! '  # 字符串最后有一个空格
str6 = str5 * 3
print(str6)  
# 'Python is FUN! Python is FUN! Python is FUN!'

# 字符串中的数字仅仅是字符
str7 = '123'
str8 = str7 * 3
print(str8)  # 输出123123123

str9 = '456'
str10 = str9 + str7 # 加号实现字符串拼接
print(str10)  
print(type(str10))

str10 = '''
This is a multi-line string.
This is the second line.
This is the third line.
'''   # 使用三引号（'''或"""）可以实现多行字符串的输入
print(str10)

# %%
# 字符串的索引和切片处理
greeting_str = 'Hey, James!'
# 打印字符串长度
print(greeting_str)
print('字符串的长度为：')
print(len(greeting_str))

# 打印每个字符和对应的索引
for index, char in enumerate(greeting_str):
    # 使用f-string格式化字符串，以字母"f"开头，并使用花括号{}来插入变量或表达式的值
    """
    通过在字符串中使用花括号和变量名，可以在字符串中插入变量的值。在这种情况下，使用了两个变量 {char} 和{index}
    当代码执行时，{char}会被替换为当前循环迭代的字符，{index}会被替换为对应字符的索引值
    """
    print(f"字符：{char}，索引：{index}")

# 单个字符索引
print(greeting_str[0])
print(greeting_str[1])
print(greeting_str[-1]) # 最后一个字符，等同于greeting_str[len(greeting_str)-1]
print(greeting_str[-2]) # 倒数第二个字符，等同于greeting_str[len(greeting_str)-2]

# 切片
# 取出前3个字符，索引为0、1、2
print(greeting_str[:3])

# 取出索引1、2、3、4、5，不含0，不含6
print(greeting_str[1:6])

# 指定步长2，取出第0、2、4 ...
print(greeting_str[::2])

# 指定步长-1，倒序
print(greeting_str[::-1])
print(greeting_str[::-2]) # 指定步长-2，倒序，取出倒数第2个、倒数第4个、倒数第6个...

# %% [markdown]
## 将数据插入字符串
name = 'James'
height = 181.18

# 使用 + 运算符，需要将数值转换为字符串，否则会报错
str_1 = name + ' has a height of ' + str(height) + ' cm.'
print(str_1)

# 使用 % ，保留了float的三位小数
str_2 = '%s has a height of %.3f cm.' %(name, height) # 按顺序填充
print(str_2)

# 使用 str.format()
str_3 = '{} has a height of {:.3f} cm.'.format(name, height)
print(str_3)

# 使用f-strings，直接引用了定义的变量，:.3f表示保留三位小数
str_4 = f'{name} has a height of {height:.3f} cm.'
print(str_4)

# %%
## 列表索引和切片
# 创建一个混合列表（列表中的各个元素数据类型都不相同，甚至可以嵌套数据）
my_list = [1, 1.0, '1', True, [1, 1.0, '1'], {1}, {1:1.0}]
print('列表长度为')
print(len(my_list))

# 打印每个元素和对应的序号
for index, item in enumerate(my_list):
    type_i = type(item)  # 调用函数获取元素的类型
    print(f"元素：{item}，索引：{index}，类型：{type_i}")

# 列表索引
print(my_list[0])
print(my_list[1])

print(my_list[-1])  # 最后一个元素，等同于my_list[len(my_list)-1]
print(my_list[-2])  # 倒数第二个元素，等同于my_list[len(my_list)-2]

# 列表切片，与字符串的切片处理一致
# 取出前3个元素，索引为0、1、2
print(my_list[:3])

# 取出索引1、2、3，不含0，不含4
print(my_list[1:4])

# 指定步长2，取出第0、2、4、6
print(my_list[::2])

# 指定步长-1，倒序
print(my_list[::-1])

# 提取列表中的列表某个元素，因为my_list[4]是一个列表，所以可以再索引一次
print(my_list[4][1])

# %%
## 列表的常用方法、操作
# 创建一个混合列表
my_list = [1, 1.0, '12ab', True, [1, 1.0, '1'], {1}, {1:1.0}]
print(my_list)

# 修改某个元素，通过索引，对元素的值进行修改
my_list[2] = '123'
print(my_list)

# 在列表指定位置插入元素，注这些操作都是在原列表上生效
my_list.insert(2, 'inserted')
print(my_list)

# 在列表尾部插入元素
my_list.append('tail')
print(my_list)

# 通过索引删除
del my_list[-1]
print(my_list)

# 删除某个元素
my_list.remove('123')
print(my_list)

# 判断一个元素是否在列表中
if '123' in my_list:
    print("Yes")
else:
    print("No")

# 列表翻转
my_list.reverse()
print(my_list)

# 将列表用所有字符连接，连接符为下划线 _
letters = ['J', 'a', 'm', 'e', 's']
word = '_'.join(letters)
print(word)

# %%
## 使用*号对列表拆包、打包
# 定义列表
list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

first, *list_rest = list_0  # 拆包，将列表中的第一个元素赋值给first，将剩余的元素赋值给list_rest
print(list_rest) # [1, 2, 3, 4, 5, 6, 7, 8]

first, second, *list_rest = list_0  # 拆包，将列表中的第一个元素赋值给first，将第二个元素赋值给second，将剩余的元素赋值给list_rest
print(list_rest) # [2, 3, 4, 5, 6, 7, 8]

first, second, *list_rest, last = list_0  # 拆包，将列表中的第一个元素赋值给first，将第二个元素赋值给second，将最后一个元素赋值给last，将剩余的元素赋值给list_rest
print(list_rest) # [2, 3, 4, 5, 6, 7]

first, *list_rest, _ = list_0  # 拆包，将列表中的第一个元素赋值给first，将剩余的元素赋值给list_rest，将最后一个元素丢弃？
print(list_rest) # [1, 2, 3, 4, 5, 6, 7]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
# 合并
combined_list = [*list1, *list2] # 打包，将list1和list2中的元素合并成一个列表
print(combined_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# %%
# *号也可用于对字符串和元组拆包、打包
# 定义字符串
string_0 = 'abcd'
first, *str_rest, last = string_0  # 拆包，将字符串中的第一个元素赋值给first，将剩余的元素赋值给str_rest，将最后一个元素赋值给last
print(str_rest) # ['b', 'c']

# 定义元组
tuple_0 = (1,2,3,4)
first, *tuple_rest, last = tuple_0  # 拆包，将元组中的第一个元素赋值给first，将剩余的元素赋值给tuple_rest，将最后一个元素赋值给last
print(tuple_rest) # [2, 3]

# %%
## 数组的浅复制和深复制
# 如果用 = 直接赋值，是非拷贝方法，结果是产生一个视图 (view)。 这两个列表是等价的，修改其中任何 (原始列表、视图) 一个列表都会影响到另一个列表。
list1 = [1, 2, 3, 4]

# 赋值，视图；两个列表共用一个地址
list2 = list1

# 拷贝，副本 (浅拷贝)
list3 = list1.copy()

list2[0] = 'a'
list2[1] = 'b'
list3[2] = 'c'
list3[3] = 'd'

print(list1)
print(list2)
print(list3)

# %%
## 嵌套列表的深复制VS浅复制
import copy

list1 = [1, 2, 3, [4, 5]]
print('原始list')
print(list1)
print("\n")

# 深复制，适用于嵌套列表
list_deep = copy.deepcopy(list1)   

# 只深复制一层
list2 = list1.copy() 

list3 = list1[:]  # 切片，浅复制

list4 = list(list1) # 列表构造函数，浅复制

list5 = [*list1] # 拆包，浅复制

# 修改元素
list_deep[3][0] = 'deep'
list_deep[2] = 'worked_0'
print('修改深复制的数据元素后，新list如下：')
print(list1) 
print(list_deep)
print("只修改了深复制后的那个数组，原始数组没有修改")

print(list2)  
print(list3)
print(list4)
print(list5)
print("\n")

list2[3][0] = 'abc'
list2[2] = 'worked_1'
print('修改copy浅复制的数据元素后，新list如下：')
print(list1) 
print(list_deep)

print(list2)
print(list3)
print(list4)
print(list5)
print("所有浅复制嵌套内的数组都修改了，深复制嵌套内的数据未修改；无论是深复制还是浅复制，最外层数据均未修改")
print("\n")

list3[3][0] = 'X1'
list3[2] = 'worked_2'
print('修改切片浅复制的数据元素后，新list如下：')
print(list1) 
print(list_deep)

print(list2)  
print(list3)
print(list4)
print(list5)
print("\n")

list4[3][0] = 'X2'
list4[2] = 'worked_3'
print('修改列表构造函数浅复制的数据元素后，新list如下：')
print(list1) 
print(list_deep)

print(list2)  
print(list3)
print(list4)
print(list5)
print("\n")

list5[3][0] = 'X3'
list5[2] = 'worked_4'
print('修改拆包浅复制的数据元素后，新list如下：')
print(list1) 
print(list_deep)

print(list2)  
print(list3)
print(list4)
print(list5)
print("\n")

# %%
## 矩阵与向量
# 用嵌套列表构造矩阵，这是一个3行2列的矩阵
A = [[0,5],
     [3,4],
     [5,0]]

# 取出行向量
print(A[0])  # 取出来是一个一维的列表
print([A[0]]) # 这里取出来有点像是二维的列表，两者的区别是什么？

print(A[1])
print([A[1]])

print(A[2])
print([A[2]])  # 这个取出来算是一个矩阵？

# 取出列向量
print([row[0] for row in A])
print([[row[0]] for row in A]) # 先用row[i]取出列元素，然后再用[]构建列表？

print([row[1] for row in A])
print([[row[1]] for row in A])

# %%
## 鸢尾花数据集
# 导入包
from sklearn.datasets import load_iris
# 使用load_iris函数加载Iris数据集
iris = load_iris()

# 说明：iris 是一个 Bunch 对象（类似字典的对象），不是 numpy 数组
# Bunch 对象本身没有 .shape 属性，.shape 是 numpy 数组的属性
print(f"iris 的类型: {type(iris)}")  # <class 'sklearn.utils.Bunch'>
print(f"iris 包含的属性: {iris.keys()}")  # 查看 iris 对象包含的所有属性
# iris 对象包含: data, target, frame, target_names, DESCR, feature_names, filename, data_module

# Iris数据集的特征存储在iris.data中
X = iris.data
print(f"X (iris.data) 的类型: {type(X)}")  # <class 'numpy.ndarray'>
print(X.shape)  # 查看数据的形状 (150, 4) - 150行，4列
# 注意：只有 numpy 数组才有 .shape 属性，所以必须使用 iris.data.shape 或 X.shape
print(X[:5])  # 查看前5行数据
type(X) # numpy.ndarray
print(X.ndim)   # 二维数组，与150*4代表的不同，150代表这个二维数组的行数，4代表这个二维数组的列数

# Iris数据集的目标（标签）存储在iris.target中
y = iris.target
type(y) # numpy.ndarray
print(y[:5])  # 查看前5行数据

# %%
# 导入包
import seaborn as sns
# 使用seaborn.load_dataset函数加载Iris数据集
iris_df = sns.load_dataset("iris")
# 查看数据集的前5行
iris_df.head()
iris_df.shape # (150, 5) 代表这个数据集有150行，5列，把data和target都算在一起

# type(iris_df) # pandas.core.frame.DataFrame
# %%
