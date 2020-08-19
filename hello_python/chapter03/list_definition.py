# 列表由一系列按特定顺序排列的元素组成, 你可以创建包含字母表中所有字母、数字0~9
# 或所有家庭成员姓名的列表; 也可以将任何东西加入列表中, 其中的元素之间可以没有
# 任何关系. 鉴于列表通常包含多个元素, 
# 给列表指定一个表示复数的名称(如letters 、digits 或names )是个不错的主意

# 在Python中, 用方括号([])来表示列表, 并用逗号来分隔其中的元素.  

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素: 
# 列表是有序集合, 因此要访问列表的任何元素, 只需将该元素的位置或索引告诉Python即可.
# Python访问列表的位置也是从0开始的
print('第一辆自行车为: ' + bicycles[0])
print('第一辆自行车为: ' + bicycles[0].title()) # 获取到的字符串可以调用字符串函数
print('列表访问下标为负数时: ' + bicycles[-2])  # 表示从反方向遍历列表
print('列表访问下标为负数时: ' + bicycles[-4])  # 程序报错 index out of range 反方向也不能超过数组长度
print('下标超过列表长度时: ' + bicycles[5])  # 程序报错 index out of range