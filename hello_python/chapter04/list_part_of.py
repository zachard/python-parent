# 初始化列表数据
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('初始化列表数据为: ')
print(players)

# 通过索引创建切片, 使用部分列表
# 要创建切片, 可指定要使用的第一个元素和最后一个元素的索引. 
# 与函数range() 一样, Python在到达你指定的第二个索引前面的元素后停止. 
# 要输出列表中的前三个元素, 需要指定索引0~3, 这将输出分别为0 、1 和2的元素.
print('\n')
print('获取索引为0、1、2的切片, 切片结果为: ')
print(players[0:3])
print('获取索引为1、2、3的切片, 切片结果为: ')
print(players[1:4])
print('如果没有指定第一个索引, 默认从列表的开头开始: ')
print(players[:4])
print('如果没有指定第二个索引, 默认到列表的结尾结束: ')
print(players[2:])
print(players[0:8])  # 这里的索引范围可以超过列表的长度, 超出部分不计
print(players[3:2])  # 第一个索引可以比第二个索引大, 同为正切片出来为空列表
print(players[1:-1]) # 第一个索引可以比第二个索引大, 前正后负切片出来为非空列表
print(players[1:-8]) # 第一个索引可以比第二个索引大, 前正后负切片出来为空列表
print(players[-1:1]) # 第一个索引可以比第二个索引大, 前正后负切片出来为空列表(这里为什么为空, 不该包含-1索引吗?)
print(players[-1:8]) # 第一个索引可以比第二个索引大, 前正后负切片出来为非空列表

# 遍历切片: 切片可以直接在for循环中使用
print('\n')
print('在for循环中遍历索引为0、1、2的元素并打印: ')
for player in players[:3]: 
    print(player)

# 复制列表
# 要复制列表, 可创建一个包含整个列表的切片. 
# 方法是同时省略起始索引和终止索引([:]). 
# 这让Python创建一个始于第一个元素, 终止于最后一个元素的切片, 即复制整个列表.
print('\n')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 通过切片复制列表

print('My favorite foods are: ')
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)  # 两个列表打印的结果一致

my_foods.append('cannoli') # 我新增了cannoli喜欢
friend_foods.append('ice cream') # 朋友新增了ice cream喜欢
print('我喜欢的食物为: ')
print(my_foods)
print('\n朋友喜欢的食物为: ')
print(friend_foods)  # 两个列表打印结果不再一致

# 错误的复制列表方式
print('\n')
my_foods_copy = ['pizza', 'falafel', 'carrot cake']
friend_foods_copy = my_foods_copy  # 直接将副本存储到friend_foods
print('刚开始, 我喜欢的食物是: ')
print(my_foods_copy)
print('刚开始, 朋友喜欢的食物是: ')
print(friend_foods_copy) # 两个列表打印结果一致

my_foods_copy.append('cannoli')  # 我以为我喜欢了食物
friend_foods_copy.append('ice cream')  # 朋友以为自己喜欢了食物
print('后来, 我喜欢的食物是: ')
print(my_foods_copy)
print('后来, 朋友喜欢的食物是: ')
print(friend_foods_copy) # 两个列表打印结果一致