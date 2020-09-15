# 遍历字典的所有键值对
# 要编写用于遍历字典的for循环, 可声明两个变量, 用于存储键—值对中的键和值. 
# 对于这两个变量, 可使用任何名称. 
# 即便遍历字典时, 键—值对的返回顺序也与存储顺序不同.
user_0 = {
    'username': 'efermi', 
    'first': 'enrico',
    'last': 'fermi', 
}
print('初始化数据为: ')
print(user_0)

for key, value in user_0.items(): 
    print('\n键为: ' + key)
    print('值为: ' + value)

print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print('每个人各自喜欢的编程语言信息为: ')
print(favorite_languages)

for name, language in favorite_languages.items(): # 此处声明的接收键和值的变量名称为name、language
    print(name.title() + "'s favorite language is " + 
        language.title() + '.')

# 遍历字典中的所有键  
# 使用keys()方法遍历字典中的所有键
print('\n')
print('所有参与调查者的名称为: ')

for name in favorite_languages.keys(): 
    print(name)

print('\n')
print('默认遍历字典中的键值: ')
for name in favorite_languages:   # 省略了keys()方法, 直接遍历字典也是遍历字典中的键值
    print(name)

# 方法keys()并非只能用于遍历; 实际上, 它返回一个列表, 其中包含字典中的所有键
print('\n')
favorite_languages_keys = favorite_languages.keys()
print('favorite_languages中的所有键为: ')
print(favorite_languages_keys)  # 注意这里的打印结果, 不是直接的列表但是仍然可以用于判断

if 'erin' not in favorite_languages_keys: 
    print('Erin, 你并没有参与调查.')

# 按顺序遍历字典中的所有键
# 要以特定的顺序返回元素, 一种办法是在for循环中对返回的键进行排序
# 可使用函数sorted()来获得按特定顺序排列的键列表的副本--并非为键值添加顺序
# 但是当前版本(3.7.9)键值的顺序似乎就是添加的顺序
print('\n')
print('用sorted方法对键值进行排序: ')
for name in sorted(favorite_languages.keys()): 
    print(name.title() + ", 谢谢你参与投票!")

# 遍历字典中所有值
# 通过values()方法获取字典的值列表, 而不包含任何键值
print('\n')
print('调查中提到的语言包含: ')
for language in favorite_languages.values(): 
    print(language.title())

# 使用set方法去除值列表中的重复项
print('\n')
print('调查中提到的语言去重后包括: ')
for language in set(favorite_languages.values()):  # 使用set去重
    print(language.title())

print('\n')
favorite_languages_values = favorite_languages.values()
print('values获取字典中所有值结果为: ')
print(favorite_languages_values)  # 注意这里打印的结果不是一个列表