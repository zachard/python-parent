favorite_languages = ' I like python '   # 创建一个前后带空格的变量favorite_languages
print("\n")
favorite_languages               # 没有使用print函数, 单写变量是无法将变量内容打印出来的
print('前面有空格' + favorite_languages + '后面有空格')
print("\n")
# rstrip()函数去除字符串结尾的空格, \t \n等造成的效果也会删除
print('前面有空格' + favorite_languages.rstrip() + '后面没空格')
print('前面有空格' + favorite_languages  + '后面有空格')        # 原变量内容并未改变

print("\n")
print('前面有空格' + favorite_languages + '后面有空格')
# lstrip()函数去除字符串开头的空格, \t \n等造成的效果也会删除
print('前面没空格' + favorite_languages.lstrip() + '后面有空格')
print('前面有空格' + favorite_languages + '后面有空格')  # 原变量内容并未改变

print('\n')
print('前面有空格' + favorite_languages + '后面有空格')
# strip()函数去除前后的空格(中间的空格不去除), \t \n等造成的效果也会删除
print('前面没空格' + favorite_languages.strip() + '后面没空格')
print('前面有空格' + favorite_languages + '后面有空格')  # 原变量内容并未改变

print('\n')
print('前面有空格' + favorite_languages + '后面有空格')
# replace()函数去除所有空格, \t \n等造成的效果不会删除
print('前面没空格' + favorite_languages.replace(' ', '') + '后面没空格')
print('前面有空格' + favorite_languages + '后面有空格')  # 原变量内容并未改变