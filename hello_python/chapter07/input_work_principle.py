# 函数input()让程序暂停运行, 等待用户输入一些文本. 
# 获取用户输入后, Python将其存储在 一个变量中, 以方便你使用.

# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# 编写清晰的程序
# 有时候, input提示可能超过一行. 
# 例如, 你可能需要指出获取特定输入的原因. 
# 在这种情况下, 可将提示存储在一个变量中, 再将该变量传递给函数input()
# 使用input函数时, Python会将用户输入解读为字符串.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "  # 注意这里的+=书写方式

name = input(prompt)
print('Hello, ' + name + '!')

# 使用input来获取数值输入
print('\n')
# age = input('How old are you? ')

# if age > 18:  # 这里会出现字符串与数字不能比较的异常, 所以input获取的输入是字符串
#     print('你已满18周岁, 请投票!')
# else: 
#     print('你未满18周岁, 不能投票!')

age = input('How old are you? ')
age = int(age)  # 获取到字符串后, 将其转换为数值

if age > 18:  # 顺利通过
    print('你已满18周岁, 请投票!')
else: 
    print('你未满18周岁, 不能投票!')

# 求模运算符
# 处理数值信息时, 求模运算符(%)是一个很有用的工具, 它将两个数相除并返回余数.
# 求模运算符不会指出一个数是另一个数的多少倍, 而只指出余数是多少.
print('\n')
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else: 
    print('\nThe number ' + str(number) + ' is odd.')