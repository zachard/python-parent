# 在Python中, 字典是一系列键—值对. 
# 每个键都与一个值相关联, 你可以使用键来访问与之相关联的值. 
# 与键相关联的值可以是数字、字符串、列表乃至字典. 事实上, 可将任何Python对象用作字典中的值.
# 在Python中, 字典用放在花括号{}中的一系列键—值对表示

# 键—值对是两个相关联的值. 指定键时, Python将返回与之相关联的值. 
# 键和值之间用冒号分隔, 而键—值对之间用逗号分隔. 在字典中, 你想存储多少个键—值对都可以. 
# 难道不就是一串json吗? 

# 访问字段中的值: 字典名['键名']
alien_0 = {'color': 'green', 'points': 5}
print('你射杀了' + alien_0['color'] + '的外星人.')
print('获得了' + str(alien_0['points']) + '分!')

# 添加键值对
# 字典是一种动态结构, 可随时在其中添加键—值对. 
# 要添加键—值对, 可依次指定字典名、用方括号括起的键和相关联的值(键值可以随意指定).
# 字典中键值的顺序不一定是添加的顺序
print('\n')
print('初始化的外星人为: ')
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('为外星人添加坐标后, 外星人为: ')
print(alien_0)

# 创建空字典  
# 使用一对空的花括号定义一个空字典
# 使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时, 通常都需要先定义一个空字典
alien_1 = {}  # 创建空字典
print('\n')
print('创建的空字典信息为: ')
print(alien_1)
alien_1['color'] = 'red'  # 为空字典添加键值
alien_1['points'] = 10
print('空字典添加键值后, 结果为: ')
print(alien_1)

# 修改字典中的值
# 要修改字典中的值, 可依次指定字典名、用方括号括起的键以及与该键相关联的新值
# 字典名['键名'] = '新键值'
print('\n')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('当前外星人初始化的X坐标为: ')
print(alien_0['x_position'])

if alien_0['speed'] == 'slow':  # 根据外星人的速度决定外星人移动的距离
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment  # 外星人开始移动了
print('外星人移动之后, X的坐标为: ')
print(alien_0['x_position'])
# alien_0['x_position'] = 'red'  # 可以直接修改键值的数值类型
# print('修改x_position键值的数据类型, 修改后为: ' + alien_0['x_position'])

# 删除键值对
# 使用del语句删除键值对: del 字典名['键名']
# 删除的键—值对永远消失了
print('\n')
alien_0 = {'color': 'green', 'points': 5}
print('初始化的字典为: ')
print(alien_0)
del alien_0['points']  # 删除字典中的键值对
print('删除points键之后的字典为: ')
print(alien_0)
# del alien_0['x_position']  # 当尝试删除字典中不存在的键时会出现KeyError: 'x_position'异常

# 由类似对象组成的字典
print('\n')
favorite_languages = {     # 当字典内容过长时对应的书写格式
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby', 
    'phil': 'phil',
}

print("Sarah's favorite language is " +     # print输出过长时的格式化处理
    favorite_languages['sarah'].title() + 
    '.')

# 判断字典是否为空
print('\n')
empty_dictionary = {}
not_empty_dictionary = {'value': "I'm not empty"}

if empty_dictionary:      # 空字典在条件测试中会返回False
    print('我是一个空的字典')

if not_empty_dictionary:  # 非空字典在条件测试中会返回True
    print('我不是一个空字典')