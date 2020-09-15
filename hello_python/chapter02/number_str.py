# 此段程序会报错, 因为age是一个int类型, 不能使用+来字符串拼接
age = 23 
# message = 'Happy ' + age + 'rd Birthday!'
# print(message)
# print('Happy ' + 23 + 'rd Birthday!')  # 这也是不允许的

print('\n')
# 正确的处理方式是: 通过str()函数将int类型的值转换为字符串类型
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)