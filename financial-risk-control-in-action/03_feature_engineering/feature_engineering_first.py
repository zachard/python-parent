#%% [markdown]
# 课程答疑：
# （1）实际业务中规则的排序：准入规则->preA模型->反欺诈规则->其他规则->A卡评分规则->B卡评分规则
#     主要的体系是规则体系，模型嵌入在整个规则之中，因为最开始只有规则，没有模型，模型是用来解决精度不够带来的问题（才会把规则替换为模型）
# （2）（准入规则、preA模型、反欺诈规则、风控模型）之间是否会选用相同的特征：
#     一般不会用相同的特征，整个风控体系可以理解为对流入的样本做层层筛选，不会用相同的特征做重复的筛选，否则会导致样本偏移越来越严重
#     每一个被拒绝的人，都是因为某些特征差才被拒绝，随着时间的推移，原本的建模特征虽然表现的很好，但是那些特征筛选掉拒绝的用户仍然处于建模样本中，
#     在特征的分布中已经被改变掉了，目前没有什么好的解决方案（好的方案是下探）

#%%
# 将feature-enginerring-1.png导入进来
from pickle import TRUE
from PIL import Image
image = Image.open('feature-enginerring-1.png')
image.show()

# %%
## 业务建模流程
# （1）将业务抽象为分类or回归问题
# （2）定义标签，得到Y
# （3）选取合适的样本，并匹配出全部的信息作为特征的来源
# （4）特征工程＋模型训练＋模型评价与调优（相互之间可能会有交互）（三者之间重复来做）
# （5）输出模型报告
# （6）上线与监控

#%% [markdown]
## 什么是特征？  
# 在机器学习的背景下，特征是用来解释现象发生的单个特性或一组特性。 当这些特性转换为某种可度量的形式时，它们被称为特征。
# 举个例子，假设你有一个学生列表，这个列表里包含每个学生的姓名、学习小时数、IQ和之前考试的总分数。现在，有一个新学生，你知道他/她的学习小时数和IQ，
# 但他/她的考试分数缺失，你需要估算他/她可能获得的考试分数。
# 在这里，你需要用IQ和study_hours构建一个估算分数缺失值的预测模型。所以，IQ和study_hours就成了这个模型的特征。

#%% [markdown]
## 特征工程可能包含的内容
# * 基础特征构造（可来源于用户画像表）
# * 数据预处理
# * 特征衍生
# * 特征变换
# * 特征筛选
#这是一个完整的特征工程流程，但不是唯一的流程，每个过程都有可能会交换顺序

# 用户画像：把数据库中的一些底表信息进行数据处理，做成一张很大很长的表，包含客户各种各样的信息，利用这张表可以很好的刻画用户的行为
#  例如，对age进行group by就可以得到用户的年龄分组

#%% [markdown]
#### 预览数据

# %%
from matplotlib import axes
import pandas as pd
import numpy as np
df_train = pd.read_csv('train.csv')  # 数据集来源于kaggle
df_train.head()

# %%
# 看数据的行列数
df_train.shape

# %%
# 查看数据的基本信息
df_train.info()
# %%
# 查看数据的基本统计信息
df_train.describe()

#%%
#变量的百分位以及离群点
#事实上不做这种分析也没关系，从最终的模型角度来筛选，会大大减少工作量（实际工作中，不需要关注，因为最后模型变量可能会把这个变量筛选掉了）
# 查看Age变量的箱线图，用于展示一组数值数据的分布情况，直观地展示数据的五个关键统计摘要：
# 最小值 (Minimum)
# 第一四分位数 (Q1, 25% 百分位)
# 中位数 (Median, Q2, 50% 百分位)
# 第三四分位数 (Q3, 75% 百分位)
# 最大值 (Maximum)

import matplotlib.pyplot as plt
df_train.boxplot(column='Age')
plt.show()

# %%
# Seaborn库是一个基于Matplotlib的数据可视化库。它的主要用途是提供一个高级接口，用于绘制有吸引力且信息丰富的统计图形；Seaborn让数据可视化变得更简单、更美观
import seaborn as sns
# 设置Seaborn的主题颜色方案，使用内置的颜色代码
sns.set_theme(color_codes=True)
# 设置随机数种子，确保结果可重现
# map(ord, "distributions")：将字符串"distributions"中每个字符转换为对应的ASCII码值，返回一个迭代器
# sum(...)：将所有ASCII码值相加，得到一个固定的数值
# np.random.seed(...)：使用这个数值作为随机数生成器的种子，确保每次运行代码时生成的随机数序列相同
# 这样做的目的是使KDE（核密度估计）曲线等涉及随机性的计算结果保持一致
# 注意：字符串"distributions"的选择是任意的，可以使用任何字符串（如"my_seed"、"123"等），
# 只要在同一个项目中保持一致即可。选择有意义的字符串有助于代码的可读性和记忆
np.random.seed(sum(map(ord, "distributions")))

# 绘制Age变量的直方图，kde=True表示绘制核密度估计曲线，bins=20表示将数据分为20个区间
sns.histplot(df_train.Age, kde=True, bins=20)
# 绘制Age变量的rugplot，rugplot是一种小细条，用于表示数据点的分布情况
sns.rugplot(df_train.Age)
plt.show()

# %%
#判断一下Y有几类
df_train.label.unique()  # 这里的Y是两类？

# %%
# 绘制Bar3D图，用于展示三维柱状图，实际业务上没什么用
from pyecharts.charts import Bar3D
from pyecharts import options as opts

bar3d = Bar3D()
# 这里设置的是一个x轴，代表的每天的24小时
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
]
# 这里设置的是一个y轴，代表的每周的7天
y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
]
# 虚拟的三位柱状图中对应的x，y，z的数据，每一个代表一项数值，data数组中总共包含6*28=168项数值
# x_axis * y_axis = 7 * 24 = 168中情况，这里的第一个数据[0, 0, 5]代表的是周六的0点有5个人申请，以此类推
# 所以这里的这个数值是一个虚拟的数据，不是从train.csv中获取的数据
data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add(
    series_name="",
    # 创建一个新的data列表，遍历原data中的每一项数据d，将d[0]和d[1]的位置互换
    # 其中这里就是把原data列表中的[x, y, z]数据，转换为[y, x, z]数据
    # 因为从原data数据结果中可以看出d[0]只有0～6的值，对应的应该是y_axis，d[1]只有0～23的值，对应的应该是x_axis
    data=[[d[1], d[0], d[2]] for d in data],
    xaxis3d_opts=opts.Axis3DOpts(type_="category", data=x_axis),
    yaxis3d_opts=opts.Axis3DOpts(type_="category", data=y_axis),
    zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    grid3d_opts=opts.Grid3DOpts(
        width=200, # 设置3D图形的宽度
        depth=80,  # 设置3D图形的深度
        rotate_speed=90,  # 设置3D图形的旋转速度
        is_rotate=True,  # 设置3D图形的旋转状态（是否自动旋转）
    ),
)
bar3d.set_global_opts(
    title_opts=opts.TitleOpts(title="2018年申请人数分布"),
    visualmap_opts=opts.VisualMapOpts(
        max_=20,  # 设置视觉映射的最大值
        range_color=range_color, # 设置视觉映射的颜色范围
    ),
)
bar3d.render_notebook()

# %% [markdown]
#### 1. 数据预处理：缺失值
# - pandas fillna：使用指定值填充缺失值
# - sklearn impute：使用指定方法填充缺失值

# 注：有些缺失值需要做处理，因为这些数据之所以缺失值是因为数据采集的时候出现了错误，
# 但是有些缺失值代表一种状态，这种情况下不会对缺失值做填充，而是给一个单独的值标识出来
# 信贷行业中，其实一般都不做缺失值填充，因为信贷行业这种缺失值一般不是数据采集错误，而是代表一种状态


#%%
df_train['Age'].sample(10)
# %%
# 对Age的缺失值用平均值填充（如果缺失与否本身是一个重要的特征，则不要填充）
df_train['Age'].fillna(df_train['Age'].mean())

# %%
# 另外一种填充缺失值的方法
from sklearn.impute import SimpleImputer
# 创建SimpleImputer对象
# missing_values=np.nan：指定要处理的缺失值类型，np.nan表示处理NaN（Not a Number）值
# strategy='mean'：指定填充策略，'mean'表示使用平均值填充缺失值
# 其他可选策略：'median'（中位数）、'most_frequent'（众数）、'constant'（常数，需要配合fill_value参数）
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# fit_transform()方法：先拟合（fit）数据计算统计量（如平均值），然后转换（transform）数据填充缺失值
# df_train[['Age']]：使用双括号返回DataFrame格式，单括号df_train['Age']返回Series格式
# SimpleImputer需要DataFrame格式的输入，所以使用双括号
df_train['Age'] = imputer.fit_transform(df_train[['Age']])
df_train.head(10)

# %% [markdown]
#### 数值型
## 数值缩放

#%%
# 取对数等变换
# 取log对数主要是改变数据的分布，对长尾的尾部有一定的缓解
# 取log对数的含义：求解“底数需要自乘多少次才能得到这个数”。
log_age = df_train['Age'].apply(lambda x:np.log(x))
# loc函数，:表示对所有行执行操作，增加一个log_age列，赋值为log_age
df_train.loc[:,'log_age'] = log_age
df_train.head(10)

# %%
# 幅度缩放，最大最小值缩放到[0,1]区间内
from sklearn.preprocessing import MinMaxScaler
mm_scaler = MinMaxScaler()
# 把Fare列的数据进行缩放，缩放到[0,1]区间内（不改变形状）
fare_trans = mm_scaler.fit_transform(df_train[['Fare']])

# %%
# 幅度缩放，将每一列的数据标准化为正态分布的
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
# 把Fare列的数据进行标准化，标准化为正态分布的（这个会改变分布形状）
fare_std_trans = std_scaler.fit_transform(df_train[['Fare']])

# %%
#中位数或者四分位数去中心化数据，对异常值不考虑，只取中间的这一部分数据
from sklearn.preprocessing import robust_scale
fare_robust_trans = robust_scale(df_train[['Fare','Age']])

# %%
#将同一行数据规范化,前面的MinMaxScaler统一变为1以内也可以达到这样的效果
# 例如：年龄的数据范围是0～100岁，而收入的数据可能是1～100w，
# 两者数据相差太大，放在同一个模型中训练会有问题，故而进行处理
from sklearn.preprocessing import Normalizer
normalizer = Normalizer()
fare_normal_trans = normalizer.fit_transform(df_train[['Age','Fare']])
fare_normal_trans

# %% [markdown]
## 统计值

#%% 
# 最大最小值
max_age = df_train['Age'].max()
min_age = df_train["Age"].min()

#%%
# 分位数,极值处理，我们最粗暴的方法就是将前后1%的值抹去，实际操作中，可能取5%或者95%
# Age列中，有1%的数据小于age_quarter_01，有99%的数据小于age_quarter_99
age_quarter_01 = df_train['Age'].quantile(0.01)
print(age_quarter_01)
age_quarter_99 = df_train['Age'].quantile(0.99)
print(age_quarter_99)

#%% [markdown]
# 树模型是否要做归一化？（面试常问的问题）
# XGBOOST和CART树不需要做归一化，树模型分化的时候主要靠数值大小，一个变量从0～100的值范围
# 变为0～1的值范围，也不能改变谁比谁大的事实，所以归一化也没有太大的意思

# %%
# 四则运算，对多个变量或常量进行加减乘除得到新的变量
df_train.loc[:,'family_size'] = df_train['SibSp']+df_train['Parch']+1
df_train.head()

# %%
## 四则运算
df_train.loc[:,'tmp'] = df_train['Age']*df_train['Pclass'] + 4*df_train['family_size']
df_train.head()

# %%
# 对特征变量做加减乘除，然后给到一堆不太可解释的变量，对模型的帮助其实不是很大（无法解释）
from sklearn.preprocessing import PolynomialFeatures
# 创建多项式特征生成器，degree=2表示生成2次多项式特征（包括原始特征、平方项和交互项）
# 以这里'SibSp','Parch'为例，会生成'SibSp','Parch','SibSp^2','Parch^2','SibSp*Parch'五项特征
poly = PolynomialFeatures(degree=2)
df_train[['SibSp','Parch']].head()
# %%
poly_fea = poly.fit_transform(df_train[['SibSp','Parch']])
poly_fea

# %%
## 离散化/分箱/分桶

#%%
# 等距和等频的区别：比如年龄是1～100岁
# 要切成10箱，那么就是1～10岁，10～20岁，每10个年龄为一箱；
# 这种情况下1～10岁里面没有人，10～20岁也几乎没人（不符合信贷准入条件），导致分箱后分布不均，后续做分析时将失去意义
# 等频分箱则是需要进行切分，并切希望切分出来分箱的人数是差不多的
# 分箱一般做2～5个，实际过程中，一个变量做5～6个分箱后，还很难得有单调递增的情况了，实际上还是要尽量保证分箱后的人数均衡

# 但是在使用一个评分（比如芝麻分）来做策略的时候，一般是想看要拒绝多少人，所以一般不是等频或者等距来分割的；更多的是会用这个分数来做评分等级

#等距切分，对变量做等距切分，一般不会用到，更多的是用等频切分
# pd.cut()函数将连续数值型变量Fare按照等距方式切分为20个区间（bins），返回每个值所属的区间标签
# 参数20表示将Fare的值域范围等分为20个区间，每个区间的宽度相等
df_train.loc[:, 'fare_cut'] = pd.cut(df_train['Fare'], 20)
df_train.head()
# %%
# 等距切分后的分箱结果
df_train['fare_cut'].unique()

# %%
# 等频切分
df_train.loc[:,'fare_qcut'] = pd.qcut(df_train['Fare'], 10)
df_train.head()

# 信贷评分卡的BiVar（变量的可视化分析）是什么：逻辑回归和评分卡是希望变量成单调性的，比如将年龄进行划分分箱后，看每个分箱的badrate是否单调
# BiVar图表示随着变量的变化，badrate（也可能是其他指标）出现的概率

#%%
df_train = df_train.sort_values('Fare')
# %%
alist = list(set(df_train['fare_qcut']))
badrate = {}
for x in alist:
    
    # 筛选出fare_qcut等于x的行
    a = df_train[df_train.fare_qcut == x]
    
    bad = a[a.label == 1]['label'].count()
    good = a[a.label == 0]['label'].count()
    
    badrate[x] = bad/(bad+good) # 这个badrate有点像是一个map集合，x为key，是所有fare_qcut的集合；存储的是具体每个fare_qcut的badrate值
f = zip(badrate.keys(),badrate.values())
f = sorted(f,key = lambda x : x[1],reverse = True )
badrate = pd.DataFrame(f)
badrate.columns = pd.Series(['cut','badrate'])
badrate = badrate.sort_values('cut')
print(badrate.head())
badrate.plot('cut','badrate')
plt.show()  # 显示图形，在非Jupyter notebook环境中需要显式调用plt.show()才能显示图形
# 这里做出来的图并不是一个平滑的单调递增的图形，在实际业务中，可以对该变量进行再分箱
# （本示例中就是分箱更大，把上升后下降的部分包含在一个分箱里），变成一个单调递增的平滑曲线

# %%
#OneHot encoding/独热向量编码（实际不会做独热向量编码，而是根据前面找几个badrate高的分箱，对这几个badrate高的分箱做独热向量编码）
# 什么时候使用独热向量编码：当变量是类别型变量时，例如：性别、学历、职业等
# category类型
df_train.info()

#%% 
set(df_train['Embarked'])
# 可以看到Embarked有三个值：S、C、Q，和空值
# %%
# 许多机器学习算法无法直接处理文本或类别形式的非数值数据（例如，颜色、性别、城市名称）。
# pd.get_dummies() 通过为每个类别创建一个新的二进制（0或1）列，将这些分类数据转换为数值格式
embarked_oht = pd.get_dummies(df_train[['Embarked']])
embarked_oht.head()
# 结果将Embarked列转换为三个新的列：Embarked_S、Embarked_C、Embarked_Q
# 每个列的值为0或1，表示该样本是否属于该类别
# 例如：Embarked_S为1，表示该样本属于S类别，Embarked_C为1，表示该样本属于C类别，Embarked_Q为1，表示该样本属于Q类别
# 例如：Embarked_S为0，表示该样本不属于S类别，Embarked_C为0，表示该样本不属于C类别，Embarked_Q为0，表示该样本不属于Q类别
# 这里对于df_train而言中的具体一行数据，Embarked_S、Embarked_C、Embarked_Q这三列的值只有一个是1，其他都是0

#%%
fare_qcut_oht = pd.get_dummies(df_train[['fare_qcut']])
fare_qcut_oht.head()

# %% [markdown]
#### 时间型
## 日期处理

#%%
car_sales = pd.read_csv('car_data.csv')
car_sales.head()
# %%
car_sales.info()
# %%
car_sales.describe()
# %%
car_sales['date_t'].dtype
# %%
# 将date_t列由字符型转换为日期类型，并赋值为date新列
car_sales.loc[:,'date'] = pd.to_datetime(car_sales['date_t'])
car_sales.info()
# %%
car_sales.head() # 表面上看值没有变，但是值的类型发生变化了

# %%
# 取出几月份
# dt是一个特殊的 Pandas 访问器，仅当该列的数据类型为 datetime 时可用，用于访问日期/时间特有的属性。
car_sales.loc[:,'month'] = car_sales['date'].dt.month
car_sales.head()
# %%
# 取出来是几号
car_sales.loc[:,'dom'] = car_sales['date'].dt.day
# %%
# 取出一年当中的第几天
car_sales.loc[:,'doy'] = car_sales['date'].dt.dayofyear
# %%
# 取出星期几
car_sales.loc[:,'dow'] = car_sales['date'].dt.dayofweek
# %%
car_sales.head()

#%% [markdown]
#### 文本型

#%%
from pyecharts.charts import WordCloud
from pyecharts import options as opts

name = [
 '梅老师', '金融', '风控', '实战', '人长得帅' ,
 '机器学习', '深度学习', '异常检测', '知识图谱', '社交网络', '图算法',
 '迁移学习', '不均衡学习', '反欺诈', '数据挖掘', '评分卡',
 '集成算法', '模型融合','python', '学员聪明']
value = [
 10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
# 将name和value组合成数据对列表，格式为[(name, value), ...]
data = list(zip(name, value))
# 创建WordCloud对象
wordcloud = WordCloud(init_opts=opts.InitOpts(width="800px", height="600px"))
# 添加数据，word_size_range参数控制词的大小范围
wordcloud.add("", data, word_size_range=[30, 80])
# 设置全局选项
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
# 在Jupyter notebook中渲染显示
wordcloud.render_notebook()

# %%
#词袋模型（实际业务中也不是很好用）
# CountVectorizer是scikit-learn库中的一个文本特征提取器，用于将文本转换为特征向量。
# 主要功能包括：分词，建立词表，转换为向量矩阵
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()  # 创建一个CountVectorizer分词对象
corpus = [
    'This is a very good class',
    'students are very very very good',
    'This is the third sentence',
    'Is this the last doc',
    'PS teacher Mei is very very handsome'
]  # 模拟一个大段的文本数据

#%% 
# fit_transform()方法执行两个步骤：
# 1. fit：学习语料库中的所有词汇，建立词汇表（vocabulary），统计每个词在整个语料库中的信息
# 2. transform：将每个文档转换为基于词汇表的特征向量
# 返回结果X是一个稀疏矩阵（sparse matrix），形状为(文档数, 词汇表大小)
# 矩阵中的每个元素表示某个词在某个文档中出现的次数（词频）
# 例如：X[i, j] 表示第i个文档中第j个词（在词汇表中的位置）出现的次数
X = vectorizer.fit_transform(corpus)
# %%
# get_feature_names_out()方法返回词汇表中所有特征词（单词）的数组
# 返回的数组顺序与特征向量矩阵X的列顺序一一对应
# 例如：如果get_feature_names_out()[0]='are'，那么X矩阵的第0列就表示'are'这个词在各个文档中的出现次数
# 此方法是scikit-learn 1.0+版本中推荐使用的方法，替代了已弃用的get_feature_names()方法
vectorizer.get_feature_names_out()

# %%
X.toarray()

# %%
# 创建CountVectorizer对象，设置ngram_range参数为(1,3)
# ngram_range参数控制提取的n-gram范围：
# - (1,3) 表示提取1-gram（单个词）、2-gram（两个连续词）和3-gram（三个连续词）
# - 例如："very good"会被提取为2-gram，"very very good"会被提取为3-gram
# - 默认情况下ngram_range=(1,1)，只提取单个词（1-gram）
# 使用n-gram可以捕获词与词之间的顺序关系和上下文信息，提高文本特征的表征能力
vec = CountVectorizer(ngram_range=(1,3))
X_ngram = vec.fit_transform(corpus)
vec.get_feature_names_out()

# %%
X_ngram.toarray()

# %%
#### TD-IDF
# TF-IDF（Term Frequency-Inverse Document Frequency）是一种用于信息检索与数据挖掘的常用加权技术
# TF-IDF值 = TF（词频） × IDF（逆文档频率）
# - TF（词频）：某个词在文档中出现的频率，词出现次数越多，TF值越大
# - IDF（逆文档频率）：衡量词的普遍重要性，包含该词的文档越少，IDF值越大
# TF-IDF的主要思想：如果某个词在一篇文档中出现的频率高，但在整个语料库中出现的频率低，则认为该词具有很好的类别区分能力

# 导入TfidfVectorizer类，用于将文本转换为TF-IDF特征向量
from sklearn.feature_extraction.text import TfidfVectorizer
# 创建TfidfVectorizer对象，使用默认参数
# 默认参数会进行：小写转换、去除标点符号、分词、计算TF-IDF值
tfidf_vec = TfidfVectorizer()
# fit_transform()方法执行两个步骤：
# 1. fit：学习语料库中的所有词汇，建立词汇表，并计算每个词的IDF值
# 2. transform：将每个文档转换为基于TF-IDF值的特征向量
# 返回结果tfidf_X是一个稀疏矩阵，形状为(文档数, 词汇表大小)
# 矩阵中的每个元素表示某个词在某个文档中的TF-IDF值（不再是简单的词频）
tfidf_X = tfidf_vec.fit_transform(corpus)
# 获取词汇表中所有特征词的数组，返回顺序与特征向量矩阵tfidf_X的列顺序一一对应
# 注意：使用get_feature_names_out()替代已弃用的get_feature_names()方法
tfidf_vec.get_feature_names_out()
# %%
tfidf_X.toarray()

# %%
## 组合特征
# 借助条件去判断获取组合特征（其实就是将多个条件组合，判断是否满足这多个条件）
df_train.loc[:,'alone'] = (df_train['SibSp']==0)&(df_train['Parch']==0)
df_train.head()

# %%
# 作业：实现一个词云图
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
corpus = [
    'This is a very good class',
    'students are very very very good',
    'This is the third sentence',
    'Is this the last doc',
    'teacher Mei is very very handsome'
]
X = vectorizer.fit_transform(corpus)
from pyecharts.charts import WordCloud
from pyecharts import options as opts
wordcloud = WordCloud(init_opts=opts.InitOpts(width="800px", height="600px"))
#这里是需要做的
# 计算每个词在所有文档中的总出现次数（词频），形成词云图的value数组
# 使用稀疏矩阵的sum方法直接计算，避免转换为密集数组，提高效率
# np.asarray().ravel() 将结果转换为1维数组，比 toarray().sum() 更高效
value = np.asarray(X.sum(axis=0)).ravel()
# 将numpy数组转换为Python原生整数列表，确保pyecharts能正确处理(这一步不可少)
value = value.astype(int).tolist()
# 将特征名称和值组合成数据对列表，格式为[(name, value), ...]
data = list(zip(vectorizer.get_feature_names_out(), value))
#计算完value后即可得到词云图
wordcloud.add("", data, word_size_range=[20, 100])
# 设置全局选项
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
# 渲染词云图
# 在Jupyter notebook中渲染显示（如果在Jupyter环境中）
wordcloud.render_notebook()