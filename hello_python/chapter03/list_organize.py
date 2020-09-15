# 初始化列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('初始化列表为: ')
print(cars)

# 通过sort方法对列表进行永久性排序, 排序后再也无法恢复到原来的顺序
cars.sort()  # 注意: 这里并没用 cars = cars.sort() 来接收排序结果
print('通过sort对列表进行永久性排序, 排序后的列表结果为: ')
print(cars)

# 通过向sort传递reverse参数进行永久反向排序
cars.sort(reverse=True)
print('通过向sort方法传递reverse参数对列表进行永久反向排序, 排序后列表结果为: ')
print(cars)
my_new_cars = ['bmw', 'audi', 'toyota', 'subaru']
my_new_cars.sort(reverse=True)
print('通过向sort方法传递reverse参数对列表进行永久反向排序, 排序后列表结果为: ')
print(my_new_cars)
# 由上述结果可知, ['audi', 'bmw', 'subaru', 'toyota']列表和['bmw', 'audi', 'toyota', 'subaru']
# 调用sort(reverse=True)得到的结果是一样的, 猜测sort(reverse=True)的操作是先sort()再reverse

# 通过sorted方法对列表排序, 不改变原列表的顺序
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('初始化列表为: ')
print(cars)
print('通过sorted对列表进行排序, 排序后的列表为: ')
print(sorted(cars))
print('通过sorted对列表进行反向排序, 排序后的列表为: ')
print(sorted(cars, reverse=True))  # reverse用于sorted方法对列表进行反向排序
print('原列表为: ')
print(cars)

# 通过reverse反转永久性反转列表, 虽然是永久性的, 但是仍然可以通过reverse反转回来
print('\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('初始化列表为: ')
print(cars)
cars.reverse()  # 只将列表进行反转, 不对列表进行排序
print('通过reverse反转列表, 反转的结果为: ')
print(cars)
cars.reverse()
print('再次反转, 将列表反转为原来的顺序, 结果为: ')
print(cars)

# 通过len方法获取列表长度
print('cars当前列表长度为: ')
print(len(cars))