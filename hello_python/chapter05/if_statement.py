# 简单的if语句
# 最简单的if语句只有一个测试和一个操作
# 在if语句中, 缩进的作用与for循环中相同. 
# 如果测试通过了, 将执行if语句后面所有缩进的代码行, 否则将忽略它们.  

# if-else语句
# if-else语句块类似于简单的if语句, 但其中的else语句让你能够指定条件测试未通过时要执行的操作.
age = 19
print('当前你的年龄为: ' + str(age))
if age > 18: 
    print('你年满18岁了, 可以投票!')
    print('你有进行投票注册吗?')
else:
    print('对不起, 你还太年轻了, 不能参与投票.')
    print('等你年满18周岁再来吧!')

# if-elif-else语句
# Python只执行if-elif-else结构中的一个代码块, 它依次检查每个条件测试, 直到遇到通过了的条件测试. 
# 测试通过后, Python将执行紧跟在它后面的代码, 并跳过余下的测试.  
age = 12
print('\n')
print('您当前年龄为: ' + str(age))

if age < 4: 
    print('您好, 请进!')
elif age < 18:
    print('您好, 请投币, 5元!')
else: 
    print('您好, 请投币, 10元!')

# 使用多个elif语句
age = 66
print('\n')
print('您当前的年龄为: ' + str(age))

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif 18 <= age < 65:   # 注意条件测试表达式可以这样写: 大于小于同时用
    price = 10
else: 
    price = 5

print('您好, 请支付: ' + str(price) + '元!')

# 省略else代码块
# Python并不要求if-elif结构后面必须有else代码块. 
# 在有些情况下, else代码块很有用; 而在其他一些情况下, 使用一条elif语句来处理特定的情形更清晰 

# 非常重要的提醒
# else是一条包罗万象的语句, 只要不满足任何if或elif中的条件测试, 其中的代码就会执行, 
# 这可能会引入无效甚至恶意的数据. 
# 如果知道最终要测试的条件, 应考虑使用一个elif代码块来代替else代码块
age = 66
print('\n')
print('您当前的年龄为: ' + str(age))

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 66:  # 这里改用elif限定了else的条件, 防止其他遗漏错误情况转入else
    price = 5

print('您好, 请支付: ' + str(price) + '元!')

# 测试多个条件
# 有时候必须检查你关心的所有条件. 在这种情况下, 应使用一系列不包含elif和else代码块的简单if语句. 
# 在可能有多个条件为True, 且你需要在每个条件为True时都采取相应措施时, 适合使用这种方法
print('\n')
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: 
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings: 
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:  # 每个if判断语句都是相互独立判断的, 不受其他if结果影响
    print('Adding extra cheese.')

print('\nFinished making your pizza!')