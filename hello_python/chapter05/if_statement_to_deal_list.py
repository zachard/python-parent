# 在for循环中用if检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print('客户点了这些披萨配料: ')
print(requested_toppings)

for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers':  # 检查特殊元素
        print('对不起, green peppers没有了!')
    else:
        print('已经将' + requested_topping + '添加好了!')

print('\n您的披萨做好!')

# if判断列表是否为空
# 在if语句中将列表名用在条件表达式中时, Python将在列表至少包含一个元素时返回True, 
# 并在列表为空时返回False. 
print('\n')
requested_toppings = []

if requested_toppings: 
    for requested_topping in requested_toppings: 
        print('已经将' + requested_topping + '添加好了!')
    print('\n您的披萨做好了!')
else: 
    print('您确定需要一份不加任何配料的披萨吗?')

# 使用多个列表
print('\n')
# 如果这个列表是固定的, 可以使用元组来存储
available_toppings = ['mushrooms', 'olives', 'green peppers', 
    'pepperoni', 'pineapple', 'extra cheese']  # 注意多行换行是如何实现的
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings: 
    if requested_topping not in available_toppings: 
        print('对不起, 我们没有' + requested_topping + '这种披萨配料!')
    else: 
        print('已经将' + requested_topping + '添加好了!')

print('\n您的披萨做好了!')