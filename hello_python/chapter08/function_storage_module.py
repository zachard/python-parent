# 将函数存储在被称为模块的独立文件中, 再将模块导入到主程序中. 
# import语句允许在当前运行的程序文件中使用模块中的代码.  

# 通过将函数存储在独立的文件中, 可隐藏程序代码的细节, 将重点放在程序的高层逻辑上.  
# 这还能让你在众多不同的程序中重用函数. 将函数存储在独立文件中后, 
# 可与其他程序员共享这些文件而不是整个程序.  

# 导入模块
# 如果你使用这种import语句导入了名为module_name.py的整个模块, 
# 就可使用下面的语法来使用其中任何一个函数: module_name.function_name()
import pizza   # 引用包含函数的模块, 模块名即为文件名

pizza.make_pizza(16, 'pepperoni')  # 根据模块来调用函数, 格式为: 模块名.函数名
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  # 不能少了模块名

# 导入特定的函数
# 导入模块中的特定函数，导入方法的语法如下: from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数: from module_name import function_0, function_1, function_2
# 若使用这种语法, 调用函数时就无需使用句点
from pizza import make_pizza

make_pizza(12, '草莓')
make_pizza(16, '孜然', '草莓', '辣椒')

# 使用as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突, 或者函数的名称太长, 可指定简短而独一无二的别名
# 要给函数指定这种特殊外号, 需要在导入它时这样做. 
# 语法: from module_name import function_name as fn
from pizza import make_pizza as mp

mp(9, '蛋清', '蛋黄')
mp(8, '辣椒', '西瓜', '苹果')

# 使用as给模块指定别名
# 还可以给模块指定别名. 通过给模块指定简短的别名, 能够更轻松地调用模块中的函数.  
# 语法: import module_name as mn
import pizza as p

p.make_pizza('5', '鸡蛋', '牛排')
p.make_pizza('100', '黄瓜', '西红柿', '韭菜')

# 导入模块中所有函数
# 使用星号(*)运算符可让Python导入模块中的所有函数
# 语法: from module_name import *

# 使用并非自己编写的大型模块时, 最好不要采用这种导入方法:
# 如果模块中有函数的名称与你的项目中使用的名称相同, 可能导致意想不到的结果:
# Python可能遇到多个名称相同的函数或变量, 进而覆盖函数, 而不是分别导入所有的函数
# 最佳的做法是, 要么只导入你需要使用的函数, 要么导入整个模块并使用句点表示法

print('\n')
print('测试开始, 包中包含与自定义函数同名的函数, 自定义函数在导入包函数之前')
def make_pizza(size):
    print('我要制作一个大小为' + str(size) + '英寸的披萨!')

from pizza import * 

make_pizza(16)  # 调用导入包中的函数, 而非自定义函数
make_pizza(12, 'aaa', 'bbbb', 'cccc')  # 调用导入包中的函数, 而非自定义函数
print('测试结束, 发现导入的包中的函数覆盖了自定义的函数')

print('\n')
print('测试开始, 包中包含与自定义函数同名的函数, 导入包函数在自定义函数之前')

from pizza import * 

def make_pizza(size):
    print('我要制作一个大小为' + str(size) + '英寸的披萨!')

make_pizza(16)  # 调用自定义函数, 而非导入包中的函数
# make_pizza(12, 'aaa', 'bbbb', 'cccc')  # 调用了自定义函数, 而非导入包中的函数, 并且运行异常, 因为参数不匹配
print('测试结束, 发现自定义的函数覆盖了导入的包中的函数')

# 当函数名相同时, 后面的函数会覆盖前面的函数

# 每个函数都应包含简要地阐述其功能的注释, 该注释应紧跟在函数定义后面, 并采用文档字符串格式. 
# 给形参指定默认值时, 等号两边不要有空格
# 对于函数调用中的关键字实参, 也应遵循这种约定
# 如果程序或模块包含多个函数, 可使用两个空行将相邻的函数分开, 这样将更容易知道前一个函数在什么地方结束, 下一个函数从什么地方开始. 