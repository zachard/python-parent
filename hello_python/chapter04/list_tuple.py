# Python将不能修改的值称为不可变的, 而不可变的列表被称为元组.
# 元组看起来犹如列表, 但使用圆括号而不是方括号来标识. 
# 定义元组后, 就可以使用索引来访问其元素, 就像访问列表元素一样.

# 初始化数据
num_tuple = (100, 140, 240, 300)
print('定义一个不可变的列表(元组): ')
print(num_tuple)

# 用下标访问元组
print('\n')
print(num_tuple[0])
print(num_tuple[1])
print(num_tuple[2])
print(num_tuple[3])
# print(num_tuple[4])  # 出现tuple index out of range元组索引越界异常

# 修改元组中元素的值(元组中的元素是不允许修改的)
# num_tuple[0] = 1000  # 出现 'tuple' object does not support item assignment 异常

# for循环遍历元组中的元素-与列表操作一致
print('\n')
print('通过for循环遍历元组元素, 结果如下: ')
for num in num_tuple: 
    print(num)

# 修改元组变量-将另一个元组赋值给元组变量
num_tuple = (1000, 2000, 4000, 6000)
print('\n')
print('修改后的元组为: ')
print(num_tuple)

# 尝试将一个列表赋值给之前的元组变量
num_tuple = [1000, 2000, 4000, 6000]  # 这也是可行的, Python的变量没有特定类型
print('\n')
print('将列表赋值给原来的元组变量, 结果为: ')
print(num_tuple)

num_tuple = 'Bob'   # 这也是可行的, Python的变量没有特定类型
print('将字符串赋值给原来的元组变量, 结果为: ')
print(num_tuple)