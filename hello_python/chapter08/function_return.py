# 在函数中, 可使用return语句将值返回到调用函数的代码行

# 返回简单值
def get_full_name(first_name, last_name): 
    """返回姓名全名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()  # 将拼接好的全名首字母大写返回

tom_andsen = get_full_name('tom', 'andsen')
print('全名为: ' + tom_andsen)

# 让实参编程可选(道理我都懂, 但是为什么放在返回值这一节来讲?)
# 有时候, 需要让实参变成可选的, 这样使用函数的人就只需在必要时才提供额外的信息. 
# 可使用默认值来让实参变成可选的
print('\n')
def get_formatted_name(first_name, last_name, middle_name = ''): # 并不是所有人都有中间名
    if middle_name:  # 当字符串为空时, Python认定其作为条件表达式返回False
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')  # 没有输入第三个参数, 可选的
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')  # 选择传入第三个参数
print(musician)

# 返回字典
print('\n')
def build_person(first_name, last_name, age=''):  # age为可选参数
    """返回字典包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}

    if age: 
        person['age'] = age
    
    return person   # 函数返回一个字典类型

musician = build_person('jimi', 'hendrix')  # 函数返回的字典使用与定义的字典使用方式一致
print('第一个构建的人物信息为: ')
print('姓: ' + musician['first'] + ', 名: ' + musician['last'])
# 这里不能获取这个对象的age, 因为调用函数没有传age参数, 所有返回的对象没有age对应的key
# print('姓: ' + musician['first'] + ', 名: ' + musician['last'] + 
#     ', 年龄: ' + musician['age'] + '.')

musician = build_person('amy', 'bob', age='35')  # 这个age不能传数值, 只能传字符串
print('第二个构建的人物信息为: ')
print('姓: ' + musician['first'] + ', 名: ' + musician['last'] + 
    ', 年龄: ' + musician['age'] + '.')