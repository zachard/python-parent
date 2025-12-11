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
