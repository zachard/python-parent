# 存储数据
# 模块json让你能够将简单的Python数据结构转储到文件中, 并在程序再次运行时加载该文件中的数据. 
# 你还可以使用json在Python程序之间分享数据. 

# 使用json.dump()和json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]  # 定义一个列表, 其实这也是一个json数值数组

filename = 'numbers.json'  # 要将json写进去的文件路径
with open(filename, 'w') as f_obj:  # 打开一个文件对象
    json.dump(numbers, f_obj)  # 第一形参为需要存储的数据, 第二个形参为用于存储数据的文件对象

# 在文件中会写入[2, 3, 5, 7, 11, 13]

# 再用json.load()将内容读取出来(与写入文件之前的内容一致)
with open(filename) as f_obj: 
    numbers_from_file = json.load(f_obj)   # 只有一个形参, 为文件对象

print('打印numbers.json文件中的内容如下: ')
print(numbers_from_file)

# 尝试将字典作为json写入文件
print('\n')
user_info = {'first_name': 'amy', 'last_name': 'bob'}
filename = 'user.json'
with open(filename, 'w') as f_obj:  # 字典其实也是一个json格式的数据, 也可以通过json.dump写进文件
    json.dump(user_info, f_obj)  # 写入文件后, json的键和值都是双引号, 标准的json格式

# 再用json.load()把文件内容读取出来(与写入文件之前的内容一致)
with open(filename) as f_obj: 
    user_info_from_file = json.load(f_obj)

print('打印user.json文件中的内容如下: ')
print(user_info_from_file)

# 尝试将字符串作为json写入文件
print('\n')
message = 'I do not like programming.'
filename = 'string.json'
with open(filename, 'w') as f_obj:  # 内容写入文件了, 但是不是json格式, 只是一个单纯的字符串内容
    json.dump(message, f_obj)

# 再用json.load()读取文件中的内容(与写入文件之前的内容一致)
with open(filename) as f_obj:
    message_from_file = json.load(f_obj)

print('打印string.json中的内容如下: ')
print(message_from_file)