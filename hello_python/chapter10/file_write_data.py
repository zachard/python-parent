# 写入文件

filename = 'programming.txt'

# 调用open()时提供了两个实参. 
# 第一个实参也是要打开的文件的名称; 
# 第二个实参('w')告诉Python, 我们要以写入模式打开这个文件. 
# 打开文件时, 可指定读取模式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+'). 
# 如果你省略了模式实参, Python将以默认的只读模式打开文件. 

# 如果你要写入的文件不存在, 函数open()将自动创建它. 
# 然而, 以写入('w')模式打开文件时千万要小心, 
# 因为如果指定的文件已经存在, Python将在返回文件对象前清空该文件. 

# Python只能将字符串写入文本文件. 
# 要将数值数据存储到文本文件中, 必须先使用函数str()将其转换为字符串格式. 
with open(filename, 'w') as file_object:   # 写入文件时, 这个路径对应的文件可以不存在, 程序会创建
    file_object.write('I do not like programming.')

# 写入多行
filename = 'programming.txt'

with open(filename, 'w') as file_object:   # 写入文件时, 这个路径对应的文件可以不存在, 程序会创建
    file_object.write('I do not like programming.')  # 程序运行到这里, 文件并没有两行I do not like programming. 说明在open(filename, 'w')时清空了之前的文件
    file_object.write('I love creating new games.\n')  # 这里输出的两句话在同一行, 因为没有在结尾添加换行符.

    file_object.write('我要独占一行.\n')  # 结尾添加换行符, 会独占一行
    file_object.write('我也要独占一行.\n') # 要让每个字符串都单独占一行, 需要在write()语句中包含换行符

# 附加到文件
# 如果你要给文件添加内容, 而不是覆盖原有的内容, 可以附加模式打开文件. 
# 你以附加模式打开文件时, Python不会在返回文件对象前清空文件, 而你写入到文件的行都将添加到文件末尾. 
# 如果指定的文件不存在, Python将为你创建一个空文件. 
filename = 'programming.txt'

with open(filename, 'a') as file_object:   # 以附加的方式写入文件, 文件之前内容不会被清除
    file_object.write('我是以附加的方式写入文件的.\n')  # 附加到文件的后面
    file_object.write('我也是以附加的方式写入文件的.\n')