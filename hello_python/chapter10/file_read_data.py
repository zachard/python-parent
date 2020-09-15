# 从文件中读取数据

# 函数open()返回一个表示文件的对象. 
# 在这里, open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象;
# Python将这个对象存储在我们将在后面使用的变量file_object中

# 关键字with在不再需要访问文件后将其关闭. 
# 在这个程序中, 注意到我们调用了open(), 但没有调用close(); 
# 你也可以调用open()和close()来打开和关闭文件, 
# 但这样做时, 如果程序存在bug, 导致close()语句未执行, 文件将不会关闭. 

# 并非在任何情况下都能轻松确定关闭文件的恰当时机, 
# 但通过使用前面所示的结构, 可让Python去确定: 
# 你只管打开文件, 并在需要时使用它, Python自会在合适的时候自动将其关闭.  

# 方法read()(前述程序的第2行)读取这个文件的全部内容, 
# 并将其作为一个长长的字符串存储在变量contents中. 

# 当你将类似pi_digits.txt这样的简单文件名传递给函数open()时, 
# Python将在当前执行的文件(即.py程序文件)所在的目录中查找文件.  
with open('pi_digits.txt') as file_object: 
    contents = file_object.read()
    # print(contents)
    print(contents.rstrip())

# 文件路径
# 可使用相对文件路径来打开该文件夹中的文件
# 在Linux和OS X中, 你可以这样编写代码: with open('text_files/filename.txt') as file_object:
# 在 Windows系统中, 在文件路径中使用反斜杠(\)而不是斜杠(/): with open('text_files\filename.txt') as file_object:
# 在相对路径行不通时, 可使用绝对路径. 
# 绝对路径通常比相对路径更长, 因此将其存储在一个变量中, 再将该变量传递给open()会有所帮助

# 在Linux和OS X中, 绝对路径类似于下面这样
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:
# 而在Windows系统中, 它们类似于下面这样:
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:

# 逐行读取
filename = 'pi_digits.txt'

print('\n')
print('开始逐行读取')
with open(filename) as file_object: 
    for line in file_object:    # 直接用for循环file_object对象, 即可获取文件中的每一行
        # print(line)
        print(line.rstrip())   # 去除每行结尾的换行符

# 创建一个包含文件各行内容的列表
# 使用关键字with时, open()返回的文件对象只在with代码块内可用. 
# 如果要在with代码块外访问文件的内容, 可在with代码块内将文件的各行存储在一个列表中, 
# 并在with代码块外使用该列表: 你可以立即处理文件的各个部分, 也可推迟到程序后面再处理. 
filename = 'pi_digits.txt'

print('\n')
print('将文件中每行内容存储到列表: ')
with open(filename) as file_object: 
    lines = file_object.readlines()   # readlines函数直接返回一个列表[], 而readline函数只读取文件的第一行

for line in lines:    # 遍历列表, 在with代码块外使用
    print(line.rstrip())

# 使用文件的内容
# 读取文本文件时, Python将其中的所有文本都解读为字符串. 
# 如果你读取的是数字, 并要将其作为数值使用, 就必须使用函数int()将其转换为整数, 
# 或使用函数float()将其转 换为浮点数. 
filename = 'pi_30_digits.txt'

print('\n')
print('使用文件中的内容: ')
with open(filename) as file_object: 
    lines = file_object.readlines()   # readlines函数直接返回一个列表[], 而readline函数只读取文件的第一行

pi_string = ''
for line in lines:    # 遍历列表, 在with代码块外使用
    pi_string += line.strip()   # 去除字符串两边的内容

print('圆周率为: ' + pi_string)
print('圆周率的长度为: ' + str(len(pi_string)))

# 包含一百万位的大型文件
# 程序运行速度还是很快的
# 其实这里也不算大文件, 文件大小也就1M而已
filename = 'pi_million_digits.txt'

print('\n')
print('读取百万位的大型文件: ')
with open(filename) as file_object: 
    lines = file_object.readlines()   # readlines函数直接返回一个列表[], 而readline函数只读取文件的第一行

pi_string = ''
for line in lines:    # 遍历列表, 在with代码块外使用
    pi_string += line.strip()   # 去除字符串两边的内容

print('圆周率为: ' + pi_string[:52])  # 字符串可以看作是数组, 也可以对其进行切片
print('圆周率的长度为: ' + str(len(pi_string)))

# 圆周率中包含你的生日吗? 
filename = 'pi_million_digits.txt'

print('\n')
print('看看圆周率中是否包含你的生日: ')
with open(filename) as file_object: 
    lines = file_object.readlines()   # readlines函数直接返回一个列表[], 而readline函数只读取文件的第一行

pi_string = ''
for line in lines:    # 遍历列表, 在with代码块外使用
    pi_string += line.strip()   # 去除字符串两边的内容

birthday = input('请以MMddyy的格式输入你的生日: ')

if birthday in pi_string:   # 字符串也是数组, 可以直接用in判断
    print('圆周率包含你的生日!')
else: 
    print('圆周率不包含你的生日!')