
# 每条if语句的核心都是一个值为True或False的表达式, 这种表达式被称为条件测试.
# 如果条件测试的值为True, Python就执行紧跟在if语句后面的代码;
# 如果为False, Python就忽略这些代码. 

# 条件测试-检查是否相等
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')

# 条件测试-检查是否相等时区分大小写
# 两个大小写不同的值会被视为不相等
print('\n')
car = 'audi'
print('当前车品牌是否为audi: ')
print(car == 'audi')
print('当前车品牌是否为Audi: ')
print(car == 'Audi')
# 可采用lower()函数忽略大小写
car = 'Audi'
print('当前车品牌小写是否为audi: ')
print(car.lower() == 'audi')

# 条件测试-检查是否不相等
# 要判断两个值是否不等, 可结合使用惊叹号和等号(!=)
print('\n')
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('这不是我想要的!')

# 比较数字
print('\n')
age = 18
print('当前年龄为: ' + str(age))
print('当前年龄是否等于18: ')
print(age == 18)
print('当前年龄是否不为20: ')
print(age != 20)
print('当前年龄是否小于20: ')
print(age < 20)
print('当前年龄是否小于等于18: ')
print(age <= 18)
print('当前年龄是否大于14: ')
print(age > 14)
print('当前年龄是否大于等于16: ')
print(age >= 16)

# 检查多个条件-使用and检查多个条件为True
print('\n')
age_tom = 20
age_bob = 16
print('当前情况下, tom和bob的年龄是否都大于等于18岁: ')
print((age_tom >= 18) and (age_bob >= 18))
age_tom = age_tom + 2
age_bob = age_bob + 2
print('两年后, tom和bob的年龄是否都大于等于18岁: ')
print((age_tom >= 18) and (age_bob >= 18))

# 检查多个条件-使用or检查是否有一个条件为True
print('\n')
age_amy = 14
age_cindy = 16
print('当前情况下, Amy和Cindy中是否有人大于等于18岁: ')
print((age_amy >= 18) or (age_cindy >= 18))
age_amy = age_amy + 2
age_cindy = age_cindy + 2
print('两年后, Amy和Cindy中是否有人大于等于18岁: ')
print((age_amy >= 18) or (age_cindy >= 18))

# 检查特定值是否包含在列表中
# 要判断特定的值是否已包含在列表中, 可使用关键字in. 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('\n')
print('用户点的披萨有: ')
print(requested_toppings)
print('用户是否点了mushrooms披萨: ')
print('mushrooms' in requested_toppings)
print('用户是否点了pepperoni披萨: ')
print('pepperoni' in requested_toppings)

# 检查特定值是否不包含在列表中--可使用关键字not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print('\n')
print('用户' + user + '是否可以发言: ')
print(user not in banned_users)
if user not in banned_users: 
    print(user + ': 您好, 请发表你的看法!')

# 布尔表达式
# 与条件表达式一样, 布尔表达式的结果要么为True, 要么为False
# 布尔值通常用于记录条件
game_active = True
can_edit = False
print('\n')
if game_active: 
    print('游戏正在运行!')

if not can_edit:     # 布尔值取反, 采用not
    print('当前状态下不可编辑')