# 有时候, 需要将一系列字典存储在列表中, 或将列表作为值存储在字典中, 这称为嵌套. 
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典

# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
aline_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, aline_2]

print('初始化的外星人列表信息为: ')
for alien in aliens:
    print(alien)

print('\n')
print('批量生产外星人开始...')
aliens = []

for aline_number in range(0, 30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print('量产的前五个外星人信息为: ')
for alien in aliens[:5]: 
    print(alien)
print('...')

print('本次总共量产了' + str(len(aliens)) + '个外星人.')
print('量产外星人结束.')

print('\n')
print('三分钟过去了, 前三个外星人要升级了...')
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

print('升级之后前五个外星人为: ')
for alien in aliens[:5]:
    print(alien)

# 在字典中存储列表
# 每当需要在字典中将一个键关联到多个值时, 都可以在字典中嵌套一个列表.
print('\n')
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # 在字典中存储的列表
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 
    'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)

# print(pizza['toppings'])  # 这里直接打印出来是一个Python的列表

# 字典中嵌套元组
print('\n')
favorite_languages = {
    'jen': ('python', 'ruby'),
    'sarah': ('c'), 
    'edward': ('ruby', 'go'),
    'phil': ('python', 'haskell'),
}

print('在字典中也可以嵌套元组: ')
for name, languages in favorite_languages.items(): 
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())

# 在字典中存储字典
# 可在字典中嵌套字典, 但这样做时, 代码可能很快复杂起来
print('\n')
users = {
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton',
    }, 

    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
    }
}

print('在字典中嵌套字典, 打印相应的信息如下: ')

for user, user_info in users.items(): 
    print('\n' + user + '的具体信息如下: ')
    print('\t姓: ' + user_info['first'])
    print('\t名: ' + user_info['last'])
    print('\t住址: ' + user_info['location'])

# 注: 列表和字典的嵌套层级不应太多. 如果嵌套层级比前面的示例多得多, 很可能有更简单的解决问题的方案