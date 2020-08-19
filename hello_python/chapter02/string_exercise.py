# 2-3
name = 'Eric'
print('Hello ' + name + ', would you like to learn some Python today ?')
print('\n')

# 2-4
name = 'tom frank'
print(name.lower())  # 小写展示
print(name.upper())  # 大写展示
print(name.title())  # 首字母大写展示
print('\n')

# 2-5
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
print('\n')

# 2-6
famous_person = 'Albert Einstein'
message = '"A person who never made a mistake never tried anything new."'
print(famous_person + ' once said, ' + message)
print('\n')

# 2-7 
name = '\tAlbert Einstein \n'
print('这是人名: ' + name + '...')
print('rstrip后的人名: ' + name.rstrip() + '...')
print('lstrip后的人名' + name.lstrip() + '...')
print('strip后的人名' + name.strip() + '...')
print('replace后的人名' + name.replace(' ', '') + '...')