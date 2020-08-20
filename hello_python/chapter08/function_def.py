# 函数是带名字的代码块, 用于完成具体的工作
# 使用关键字def来告诉Python你要定义一个 函数
# 一个最简单的函数
def greet_user():    # 定义函数
    # 显示简单的问候语
    """显示简单的问候语"""    # 这行是文档字符串的注释
    print('Hello!')

greet_user()  # 调用函数

# 向函数传递信息
def greet_user(username):    # 定义函数(重复函数名称, 编译报错, 但实际运行没出错)
    # 显示简单的问候语
    """显示简单的问候语"""    # 这行是文档字符串的注释
    print('Hello, ' + username.title() + '!')

greet_user('Bob')

# 实参和形参
# 形参是函数完成其工作所需的一项信息
# 实参是调用函数时传递给函数的信息
print('\n')
def say_hello(name):  # 定义函数, name为形参
    name = name.title()  # 在函数中改变形参的值
    print('Hello, ' + name + '!')

cindy_name = 'cindy'  # cindy_name为实参
say_hello(cindy_name)
print(cindy_name)  # 调用函数后, 实参的值并没有改变