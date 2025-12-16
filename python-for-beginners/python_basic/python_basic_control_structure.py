# %%
# python的for循环后面可以接else语句
for x in range(10):
    print(x)
else: # for循环结束后会执行
    print("For loop finished")

# %%
# for循环后的else语句可能会被break语句中断
for x in range(10):
    if x >= 8:
        break
    else:
        print(x)
else: 
    print("For loop finished")

# %%
# pass语句：什么也不做，它只是一个空语句占位符。在需要有语句的地方，但是暂时不想编写任何
# 语句时，可以使用 pass 语句。类似于Java中的//TODO 注释
for i in range(6):
    pass  # 什么都不做，空语句
    print(i)

#%%[markdown]
#### 计算向量内积
# 内积的含义：将两个向量的对应分量相乘，然后将乘积相加，从而得到它们的内积；<br>
# 向量内积的结果是一个标量，也就是一个值，而不是向量。<br>
# $\mathbf {a} \cdot \mathbf {b} = a_{1}b_{1} + a_{2}b_{2} + ... + a_{n}b_{n}$
# %%
# 定义向量a和b
a = [1, 2, 3, 4, 5]     # 定义一个五维向量
b = [6, 7, 8, 9, 0]

# 初始化内积为0
dot_product = 0

# 使用for循环计算内积
for i in range(len(a)):
    dot_product += a[i] * b[i]
    # 1*6 + 2*7 + 3*8 + 4*9 + 5*0 

# 打印内积
print("向量内积为：", dot_product)

# %%
# enumerate迭代器
fruits = ['apple', 'banana', 'cherry']
# 从0开始编号
for index, fruit in enumerate(fruits): 
# 返回顺序固定，第一个元素是索引，第二个元素是水果，与变量名无关，这里变量名可以替换为a, b
    print(f"索引：{index}，水果：{fruit}")

# 从1开始编号
for index, fruit in enumerate(fruits,1):
    print(f"索引：{index}，水果：{fruit}")

# %%
