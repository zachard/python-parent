# for循环是一种遍历列表的有效方式, 但在for循环中不应修改列表, 否则将导致Python难以跟踪其中的元素. 
# 要在遍历列表的同时对其进行修改, 可使用while循环. 

# 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']  # 待验证用户列表
confirmed_users = [] # 已验证用户列表

# 遍历列表对用户进行验证
while unconfirmed_users:   # 当列表不为空时返回True, 当列表为空时, 返回False
    current_user = unconfirmed_users.pop()   # 取出需要验证的用户
    print('验证用户: ' + current_user.title())
    confirmed_users.append(current_user)  # 将已验证的移到已验证用户列表

print('\n以下用户已经经过验证: ')
for user in confirmed_users: 
    print('\t' + user)

print('\n未完成验证的用户为: ')
print(unconfirmed_users)

# 为什么不能用for代替while
print('\n')
print('采用for循环的方式来实现上述操作: ')
unconfirmed_users = ['alice', 'brian', 'candace']  # 待验证用户列表
confirmed_users = [] # 已验证用户列表

for unconfirmed_user in unconfirmed_users: 
    # current_user = unconfirmed_users.pop()   # for循环中, 不能采用pop来删除元素, 会出现遍历问题
    print('验证用户: ' + unconfirmed_user.title())
    confirmed_users.append(unconfirmed_user)  # 将已验证的移到已验证用户列表
    # unconfirmed_users.remove(unconfirmed_user)  # for循环中, 不能采用remove来删除元素, 会出现遍历问题

print('\n以下用户已经经过验证: ')
for user in confirmed_users: 
    print('\t' + user)

print('\n未完成验证的用户为: ')
print(unconfirmed_users)

# 删除包含特定值的所有列表元素
# 通过while循环不断判断列表中是否存在特定元素, 存在就将它删除
print('\n')
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print('初始化的数据为: ')
print(pets)

cat_name = 'cat'
while cat_name in pets: 
    pets.remove(cat_name)

print('删除名称为' + cat_name + '的宠物后, 宠物列表为: ')
print(pets)

# 使用用户输入来填充字典
responses = {}

polling_active = True
while polling_active: 
    name = input("\nWhat is your name? ")  # 获取用户输入的姓名
    response = input("Which mountain would you like to climb someday? ") # 获取用户想要爬的山
    responses[name] = response  # 将用户的数据存入字典
    repeat = input('Would you like to let another person respond? (yes/ no) ')

    if repeat == 'no':  # 判断调查是否结束
        polling_active = False

print('\n---Poll Result---')  # 打印调查结果
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')