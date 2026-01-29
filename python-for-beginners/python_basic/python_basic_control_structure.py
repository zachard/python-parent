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
# 使用zip迭代器，将两个列表合并成一个列表
names = ['Alice', 'Bob', 'Charlie']
scores = [80, 90, 75]

# 两个元组进行组合，返回的结果如下：
# Alice 80
# Bob 90
# Charlie 75
for name, score in zip(names, scores):
    print(name, score)

# 如果可迭代对象的长度不相等, zip()函数会以长度最短的可迭代对象为准进行迭代
names = ['Alice', 'Bob', 'Charlie']
scores = [80, 90]
# 返回的结果如下：
# Alice 80
# Bob 90
for name, score in zip(names, scores):
    print(name, score)

# 如果需要使用长度最长的可迭代对象，可以使用 itertools.zip_longest() 函数
from itertools import zip_longest
# 返回的结果如下：
# Alice 80
# Bob 90
# Charlie None
for name, score in zip_longest(names, scores):
    print(name, score)

# 使用zip()计算向量内积
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 0])

dot_product = np.dot(a,b)
# 1*6 + 2*7 + 3*8 + 4*9 + 5*0 = 6 + 14 + 24 + 36 + 0 = 80

# 打印内积
print("向量内积为：", dot_product)

# %%
# 自定义函数 
def custom_meshgrid(x, y):

    num_x = len(x); num_y = len(y)
    X = []; Y = []
    # 外层for循环
    for i in range(num_y):
        X_row = []; Y_row = []
        # 内层for循环
        for j in range(num_x):
            X_row.append(x[j])
            Y_row.append(y[i])
        # 生成二维数组
        X.append(X_row); Y.append(Y_row)
    
    return X, Y

# %%
# 使用自定义函数生成二维数组
x = [0, 1, 2, 3, 4, 5] # 横坐标列表
y = [0, 1, 2, 3]       # 纵坐标列表
X, Y = custom_meshgrid(x, y)
print(X)
print(Y)

# %% [markdown]
### 矩阵乘法： 三层for循环
# 矩阵A的第一行元素和矩阵B第一列对应元素分别相乘,再相加,结果为矩阵C的第一行、第一列元素
# $c_{1,1}$</br>
# 矩阵A的第一行元素和矩阵B第二列对应元素分别相乘,再相加,结果为矩阵C的第一行、第二列元素
# $c_{1,2}$</br>

# %%
# 定义矩阵 A 和 B
A = [[1, 2, 10, 20],
     [3, 4, 30, 40],
     [5, 6, 50, 60]]
        
B = [[4, 2],
     [3, 1],
     [40, 20],
     [30, 10]]

# 定义全 0 矩阵 C 用来存放结果
# 矩阵的行数为第一个矩阵的行，矩阵的列为第二个矩阵的列 (第二个矩阵的列数等于第一个矩阵的行数)
C = [[0, 0],
     [0, 0],
     [0, 0]]

# 遍历 A 的行
for i in range(len(A)): # len(A) 给出 A 的行数
    
    # 遍历 B 的列
    for j in range(len(B[0])):  
    # len(B[0]) 给出 B 的列数
        
        # 这一层相当于消去 k 所在的维度，即压缩
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
            # 完成对应元素相乘，再求和
        # c_{1,1} = 1*4 + 2*3 + 10*40 + 20*30 = 4 + 6 + 400 + 600 = 1010
        # c_{1,2} = 1*2 + 2*1 + 10*20 + 20*10 = 2 + 2 + 200 + 200 = 404
        # c_{2,1} = 3*4 + 4*3 + 30*40 + 40*30 = 12 + 12 + 1200 + 1200 = 2424
        # c_{2,2} = 3*2 + 4*1 + 30*20 + 40*10 = 6 + 4 + 600 + 400 = 1010
        # c_{3,1} = 5*4 + 6*3 + 50*40 + 60*30 = 20 + 18 + 2000 + 1800 = 3838
        # c_{3,2} = 5*2 + 6*1 + 50*20 + 60*10 = 10 + 6 + 1000 + 600 = 1616
# 输出结果
for row in C:
    print(row)

# %%
