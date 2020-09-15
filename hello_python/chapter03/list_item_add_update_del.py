# 初始化的列表
motorcycles = ['honda', 'yamaha', 'suzuki']
# print('初始化的列表为: ' + str(motorcycles))  # 这种方式也可行
print('初始化的列表为: ')
print(motorcycles)

# 修改列表中的第一个元素
# 注: 这里是给motorcycles[0] (指定列表的数组下标)赋值, 只改变其中一个元素, 而不是给整个列表motorcycles赋值
motorcycles[0] = 'ducati'
print('修改列表中第一个元素后列表为: ')
print(motorcycles)  # 这里不像字符串变量调用函数后自身值没修改, 列表的内容这里已经被修改了

# 通过append函数将元素添加的列表末尾
motorcycles.append('honda')   # 注: 这是基于上一步中修改的motorcycles列表增加元素
print('在列表末尾增加元素后列表为: ')
print(motorcycles)
# 也可创建一个空列表, 然后通过append函数依次向列表中添加元素

# 通过insert函数在列表任意位置添加新元素, 需要指定新元素的索引和值
motorcycles.insert(2, 'Bob')
print('在列表第三个位置增加一个元素后列表为: ')
print(motorcycles)

# 通过del语句删除列表中的元素, 前提是知道需要删除元素的索引
# 通过del语句删除列表中元素后, 该元素将不能再被访问(因为删除的元素不能被变量接收)
del motorcycles[2]
print('通过del语句删除列表中第三个位置的元素后列表为: ')
print(motorcycles)
print('del语句删除元素后, 列表中第三个位置上的元素为: ' + motorcycles[2])

# 方法pop可删除列表末尾的元素, 并让你能够接着使用它. 
# 术语弹出(pop)源自这样的类比: 列表就像一个栈, 而删除列表末尾的元素相当于弹出栈顶元素.  
poped_motorcycle = motorcycles.pop()
print('通过pop删除列表末尾元素后列表为: ')
print(motorcycles)
print('通过pop删除列表末尾元素, 被删除的元素为: ' + poped_motorcycle.title())
# empty_list = []
# empty_list.pop()  # 不能在空列表中执行pop方法, 程序运行会出现pop from empty list异常

# 通过pop方法删除列表中任意位置的元素, 只需要在括号中指定需要弹出元素的索引即可
poped_index_motorcycle = motorcycles.pop(1)
print('通过pop删除列表中第二个元素后列表为: ')
print(motorcycles)
print('通过pop删除列表中第二个元素, 被删除元素为: ' + poped_index_motorcycle)
# poped_over_motorcycle = motorcycles.pop(100) 
# pop删除元素的下标不能超出列表长度, 否则出现pop index out of range异常

# 如果你要从列表中删除一个元素, 且不再以任何方式使用它, 就使用del语句; 
# 如果你要在删除元素后还能继续使用它, 就使用方法pop().

# 通过remove方法根据值删除元素
# motorcycles.remove('notexist')
# print('通过remove方法删除列表中一个不存在的值, 删除后的列表为: ')
# print(motorcycles)  # remove方法不能删除列表中不存在的值, 会出现not in list异常
motorcycles.remove('ducati')
print('通过remove方法删除列表中一个存在的值, 删除后的列表为: ')
print(motorcycles)

ducati = 'ducati'
motorcycles.append(ducati)
motorcycles.append(ducati)
motorcycles.append(ducati)  # 先把值加回去, 并且是重复的

print('当前状态下, 列表内容为: ')
print(motorcycles)
motorcycles.remove(ducati)  # remove函数也可以传入变量, 实现在列表中删除变量的值
# 这个变量相当于前面pop方法弹出来的接收的元素
print('通过remove删除列表中第一个值为' + ducati + '的元素(列表中存在多个), 删除后的列表为: ')
print(motorcycles)

# 方法remove()只删除第一个指定的值. 如果要删除的值可能在列表中出现多次, 就需要使用循环来判断是否删除了所有这样的值.