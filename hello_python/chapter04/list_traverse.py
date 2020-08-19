# 初始化数据
magicians = ['alice', 'david', 'carolina']
print('初始化数据为: ')
print(magicians)

# 通过for循环来遍历列表
print('\n')
print('通过for循环遍历列表, 打印元素: ')
for magician in magicians:
    print(magician)

# 在for循环中执行更多操作
print('\n')
print('在for循环中打印更多的信息: ')
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

# 在for循环中, 想包含多少行代码都可以 
# 每个缩进的代码行都是循环的一部分, 且将针对列表中的每个值都执行一次
# 尝试了一下, 这里的缩进必需是缩进四个空格, 多一个或者少一个都不行
# 除非没有缩进(前面没空格), 那么这行代码就不在for循环中了, 只会在for循环结束后执行一次
print('\n')
print('在for循环中包含多行代码, 每行代码都循环执行: ')
for magician in magicians:
    print(magician.title() + ', that was a great trick!')  # 缩进了, 是for循环一部分
    # 在for循环的两行代码之间, 隔一个空行也没关系
    print("I can't wait to see your next trick, " + magician.title() + '.\n') # 缩进了, 是for循环一部分
print('Thank you, everyone. That was a great magic show!') # 没有缩进, 不是for循环一部分

# Python中的缩进很重要, 是判断缩进代码块的依据
print('\n')
#print('常见的缩进错误: ')
# for magician in magicians:
# print(magician)       # 程序运行出现expected an indented block异常, 表示没有缩进

# for magician in magicians:
#    #缩进一个空行, 也不行, 程序出现expected an indented block异常
# print(magician)       # 程序运行出现expected an indented block异常, 表示没有缩进

# 判断for中变量的作用范围
print('\n')
print('for循环中变量的作用范围: ')
for magician in magicians:
    print(magician.title() + ', that was a great trick!')  # 缩进了, 是for循环一部分
print("I can't wait to see your next trick, " + magician.title() + '.\n') # 没缩进, 不是for循环一部分
# 最后一行print语句不会报错, 而且magician会输出magicians列表中最后一个值
# 说明magician这个变量不仅仅作用在前面的for循环中