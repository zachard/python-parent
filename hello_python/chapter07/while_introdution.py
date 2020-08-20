# 简单的while循环
# 从1开始, 打印小于等于5的整数
current_number = 1

while current_number <= 5: 
    print(current_number)
    current_number += 1

# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':  # 不是quit才打印信息
        print(message)

# 使用标志
# 在要求很多条件都满足才继续运行的程序中, 可定义一个变量, 用于判断整个程序是否处于活动状态. 
# 这个变量被称为标志, 充当了程序的交通信号灯. 
# 你可让程序在标志为True时继续运行, 并在任何事件导致标志的值为False时让程序停止运行. 
# 这样, 在while语句中就只需检查一个条件——标志的当前值是否为True, 
# 并将所有测试(是否发生了应将标志设置为False的事件)都放在其他地方, 从而让程序变得更为整洁.  
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
# 要立即退出while循环, 不再运行循环中余下的代码, 也不管条件测试的结果如何, 可使用break语句. 
# break语句用于控制程序流程, 可使用它来控制哪些代码行将执行, 
# 哪些代码行不执行, 从而让程序按你的要求执行你要执行的代码. 

# 在任何Python循环中都可使用break语句
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
    city = input(prompt) 

    if city == 'quit': 
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 在循环中使用continue
# 要返回到循环开头, 并根据条件测试结果决定是否继续执行循环, 可使用continue语句. 
# 它不像break语句那样不再执行余下的代码并退出整个循环. 
# 示例: 打印1-10范围内的奇数
print('\n')
print('1-10内的奇数如下: ')
current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)