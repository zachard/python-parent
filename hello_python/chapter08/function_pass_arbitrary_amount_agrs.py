# Python允许函数从调用语句中搜集任意数量的实参

# 形参名*toppings中的星号让Python创建一个名为toppings的空元组, 
# 并将收到的所有值都封装到这个元组中.  
def make_pizza(*toppings): 
    """打印客户点的配料"""
    print(toppings)

make_pizza('pepperoni')  # 从函数调用打印结果来看, 参数是以元组形式传入的
make_pizza('mushrooms', 'green peppers', 'extra cheese') 

# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参, 必须在函数定义中将接纳任意数量实参的形参放在最后. 
# Python先匹配位置实参和关键字实参, 再将余下的实参都收集到最后一个形参中.  
# toppings前面必需有*来表示接收的是任意数量的实参, 且这个参数必需放在函数定义的最后
print('\n')
def make_pizza_with_size(size, *toppings):  # size作为非任意数量实参, 必需放在*toppings任意数量实参之前
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print('-' + topping)
    print(toppings)

make_pizza_with_size(16, 'pepperoni')
make_pizza_with_size(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
# 有时候, 需要接受任意数量的实参, 但预先不知道传递给函数的会是什么样的信息. 
# 在这种情况下, 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少. 
# **开头的表示任意数量的关键字实参, 关键字实参也必需方后面
print('\n')
def build_profile(first, last, **user_info):
    """创建一个字典, 包含用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

# location='princeton'为第一个关键字实参, field='physics'为第二个关键字实参
# 它们都存储在**user_info字典之中
user_profile = build_profile('albert', 'einstein', 
    location='princeton', field='physics')
print('创建的用户信息为: ')
print(user_profile)

# 同时使用任意数量实参、任意数量的关键字实参
print('\n')
def amount_key_agrs(number, *toppings, **user_info):  # 函数定义没有问题
    print('输入的位置实参为: ')
    print(number)
    print('输入的任意数量实参为: ')
    print(toppings)
    print('输入的任意数量关键字实参为: ')
    print(user_info)

amount_key_agrs(16, 'aaaa', 'bbbb', 'cccc')   # 调用未出现异常
# amount_key_agrs(16, 'name' = 'amy', 'sex' = 'W')  # 调用出现异常, 任意数量关键字实参不能传入任意数量实参
# amount_key_agrs(16, 'aaaa', 'bbbb', 'cccc', 'name' = 'amy', 'sex' = 'W') # 调用出现异常, 任意数量关键字实参不能传入任意数量实参