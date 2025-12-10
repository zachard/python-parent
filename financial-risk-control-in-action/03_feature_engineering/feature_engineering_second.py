#%% [markdown]
## 特征选择（feature_selection）
# 会先对数据进行了预处理，才会做特征选择。一般的业务中不会对基础特征做筛选
# 因为可能会出现基础特征虽然看着没用，但基础特征的衍生特征有用（除非这个基础特征一定没用才会去掉，比如缺失比例高的变量，看缺失人群和非缺失人群的差别）

### Filter(过滤，直接计算一些特征的指标，然后根据指标的大小对特征进行排序，把靠前的特征取出来)
# - 1. 移除低方差的特征 （Removing features with low variance）
# - 2. 单变量特征选择（Univariate feature selection）

### Wrapper（把特征放进去，然后逐渐的调用特征，看模型的效果，把效果好的特征留下来，即用模型做筛选）
# - 3. 递归特征消除（Recursive Feature Elimination）

### Embedded（嵌入，在模型训练的过程中，对特征进行筛选）
# - 4. 使用SelectFromModel选择特征 （Feature selection using SelectFromModel）
# - 5. 将特征选择过程融入pipeline （Feature selection as part of a pipeline）

# %% [markdown]
# 当数据预处理完成后，我们需要选择有意义的特征输入机器学习的算法和模型进行训练。
# 通常来说，从两个方面考虑来选择特征：
# (1)特征是否发散：如果一个特征不发散，例如方差接近于0，也就是说样本在这个特征上基本上没有差异，这个特征对于样本的区分并没有什么用。（样本在这个特征上的取值基本雷同的，则这个变量可以去掉）
# (2)特征与目标的相关性：与目标相关性高的特征，应当优选选择。除移除低方差法外，本文介绍的其他方法均从相关性考虑。

#%% [markdown]
# 特征选择可以分为3种：（每种方法用一个，比如Filter和Embedded本质是同一种方法，没必要同时用）
# - Filter：过滤法，按照发散性或者相关性对各个特征进行评分，设定阈值或者待选择阈值的个数，选择特征。
# - Wrapper：包装法，根据目标函数（通常是预测效果评分），每次选择若干特征，或者排除若干特征。
# - Embedded：嵌入法，先使用某些机器学习的算法和模型进行训练，得到各个特征的权值系数，根据系数从大到小选择特征。类似于Filter方法，但是是通过训练来确定特征的优劣。

# %% [markdown]
# 特征选择主要有两个目的：
# - 减少特征数量、降维，使模型泛化能力更强，减少过拟合；(对变量做筛选，以及对变量做分箱处理来减少过拟合)  
# - 增强对特征和特征值之间的理解。  

#%% [markdown]
# 拿到数据集，一个特征选择方法，往往很难同时完成这两个目的。通常情况下，选择一种自己最熟悉
# 或者最方便的特征选择方法（往往目的是降维，而忽略了对特征和数据理解的目的）。接下来将结合
# Scikit-learn提供的例子 介绍几种常用的特征选择方法，它们各自的优缺点和问题。

# %%
## Filter
### 1）移除低方差的特征（Removing features with low variance）  
# 假设某特征的特征值只有0和1，并且在所有输入样本中，95%的实例的该特征取值都是1，那就可以认为这个特征作用不大。如果100%都是1，那这个特征就没意义了。
# 当特征值都是离散型变量的时候这种方法（移除低方差的特征）才能用，如果是连续型变量，就需要将连续变量离散化之后才能用。而且实际当中，一般不
# 太会有95%以上都取某个值的特征存在，所以这种方法虽然简单但是不太好用。可以把它作为特征选
# 择的预处理，先去掉那些取值变化小的特征，然后再从接下来提到的的特征选择方法中选择合适的进
# 行进一步的特征选择。

# 导入VarianceThreshold类，用于移除低方差的特征
import math
from sklearn.feature_selection import VarianceThreshold
# 创建示例数据集X，包含6个样本，每个样本有3个特征
# 每一行代表一个样本，每一列代表一个特征
# 例如：第一个样本的特征值为[0, 0, 1]，第二个样本的特征值为[0, 1, 0]
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
# 创建VarianceThreshold对象，设置方差阈值
# threshold=(.8 * (1 - .8)) = 0.8 * 0.2 = 0.16
# 这个阈值是基于伯努利分布的方差公式：p * (1 - p)，其中p=0.8表示特征值中某个值（如1）出现的概率
# 如果特征的方差小于0.16，则该特征会被移除（因为方差小意味着特征值变化小，区分度低）
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
# 对数据进行拟合和转换
# fit_transform()方法会：1) 计算每个特征的方差；2) 移除方差小于阈值的特征；3) 返回筛选后的数据
sel.fit_transform(X)

# 在最后的结果中，X最后变成了一个只包含两个特征的数组，因为第一列一特征值为0的概率达到了5/6，所以VarianceThreshold把它移除了

# %% [markdown]
# 插曲：如果特征的行，列非常多，特征选择非常耗时，有什么好的特征选择方法？
# 答：不能做列抽样，可以对行采样。或者可以先用IV值做一些筛选，卡方检验做列筛选

#%%
### 2） 单变量特征选择 （Univariate feature selection）
# 单变量特征选择的原理是分别单独的计算每个变量的某个统计指标，根据该指标来判断哪些变量重要，剔除那些不重要的变量。
# 对于分类问题（y离散），可采用：
# - 卡方检验(推荐的方法，如果特征筛选只用一种方法，建议用这种最简单最快捷的方法)
# - f_classif
# - mutual_info_classif
# - 互信息

# 对于回归问题(y连续)，可采用：
# - 皮尔森相关系数
# - f_regression,
# - mutual_info_regression
# - 最大信息系数

## 这种方法（卡方检验？）比较简单，易于运行，易于理解，通常对于理解数据有较好的效果（但对特征优化、提高泛化能力来说不一定有效）。
# - SelectKBest 移除得分前 k 名以外的所有特征（取top k）
# - SelectPercentile 移除得分在用户指定百分比以后的特征（取top k%）
# - 对每个特征使用通用的单变量统计检验：假正率（false positive rate）SelectFpr， 伪发现率（false discovery rate）SelectFdr， 或族系误差率 SelectFwe.
# - GenericUnivariateSelect 可以设置不同的策略来进行单变量特征选择。同时不同的选择策略也能够使用超参数寻优，从而让我们找到最佳的单变量特征选择策略。

# Notice:
# The methods based on F-test estimate the degree of linear dependency between two random
# variables.（F检验用于评估两个随机变量的线性相关性）On the other hand, mutual information
# methods can capture any kind of statistical dependency, but being nonparametric, they require
# more samples for accurate estimation.（另一方面，互信息的方法可以捕获任何类型的统计依赖关
# 系，但是作为一个非参数方法，估计准确需要更多的样本）

#%% 
### 卡方(Chi2)检验
# 经典的卡方检验是检验定性自变量对定性因变量的相关性。比如，我们可以对样本进行一次chi2 测试来选择最佳的两项特征：
# 导入load_iris函数，用于加载经典的鸢尾花数据集（常用于机器学习示例）
from sklearn.datasets import load_iris
# 导入SelectKBest类，用于选择得分最高的k个特征
from sklearn.feature_selection import SelectKBest
# 导入chi2函数，用于计算卡方统计量（卡方检验用于评估特征与目标变量的相关性）
from sklearn.feature_selection import chi2
# 加载鸢尾花数据集，该数据集包含150个样本，每个样本有4个特征（花萼长度、花萼宽度、花瓣长度、花瓣宽度）
# 目标变量有3个类别（3种鸢尾花：山鸢尾、变色鸢尾、维吉尼亚鸢尾）
iris = load_iris()
# 将数据集拆分为特征矩阵X和目标变量y
# X是特征数据（150行×4列），y是标签数据（150个样本的类别标签，取值为0、1或2）
X, y = iris.data, iris.target
X.shape

#%%
# 使用SelectKBest结合chi2卡方检验进行特征选择，选择得分最高的2个特征
# SelectKBest(chi2, k=2)：创建一个特征选择器，使用chi2作为评分函数，选择k=2个最佳特征
# fit_transform(X, y)：对特征矩阵X和目标变量y进行拟合和转换
#   - fit阶段：计算每个特征与目标变量y的卡方统计量，评估特征与目标变量的相关性
#   - transform阶段：根据卡方得分，选择得分最高的2个特征，返回筛选后的特征矩阵
# X_new：筛选后的特征矩阵，只包含与目标变量最相关的2个特征（从原来的4个特征中选出）
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
X_new.shape
# 卡方检验与IV值的异同：跟IV值本质是一样的。

# %%
### Pearson相关系数（Pearson Correlation）
# 皮尔森相关系数是一种最简单的，能帮助理解特征和响应变量之间关系的方法，该方法衡量的是变量
# 之间的线性相关性，结果的取值区间为 -1，1］，-1表示完全的负相关，+1表示完全的正相关，0表示没有线性相关。

# 逻辑回归本身对变量相关性特别敏感，所以会先做特征筛选，把相关性特别强的变量去除，所以会用到这个相关系数

import numpy as np
# 从scipy.stats模块导入pearsonr函数，用于计算Pearson相关系数
# pearsonr返回两个值：相关系数（-1到1之间）和p值（用于检验相关性的显著性）
from scipy.stats import pearsonr
# 设置随机数种子为0，确保每次运行代码时生成的随机数序列相同，便于结果复现
np.random.seed(0)
# 设置样本数量为300，表示要生成300个数据点
size = 300
# 生成一个包含300个随机数的数组x，这些随机数服从均值为0、标准差为1的正态分布
# x作为原始数据，后续会在此基础上添加噪声来演示噪声对相关系数的影响
x = np.random.normal(0, 1, size)
# 计算低噪声情况下的Pearson相关系数
# x + np.random.normal(0, 1, size)：在原始数据x的基础上添加均值为0、标准差为1的噪声
# 由于噪声较小（标准差=1），新数据与原始数据x的相关性应该较高（接近1）
# pearsonr(x, x + noise)会返回一个元组，包含两个值：
#   1. 相关系数（correlation coefficient）：取值范围为[-1, 1]
#      - 1：完全正相关，两个变量同向变化
#      - 0：无线性相关
#      - -1：完全负相关，两个变量反向变化
#      - 接近1或-1表示强相关，接近0表示弱相关
#   2. p值（p-value）：用于检验相关系数的统计显著性
#      - p < 0.05：通常认为相关系数在统计上显著（有95%的置信度认为相关关系不是偶然的）
#      - p >= 0.05：相关系数在统计上不显著（可能是偶然的，不能确定存在真实的相关关系）
#      - p值越小，说明相关系数越可靠，越不可能是随机产生的
print("Lower noise", pearsonr(x, x + np.random.normal(0, 1, size)))
# 计算高噪声情况下的Pearson相关系数
# x + np.random.normal(0, 10, size)：在原始数据x的基础上添加均值为0、标准差为10的噪声
# 由于噪声较大（标准差=10），新数据与原始数据x的相关性应该较低（远离1）
# 这个例子演示了噪声大小对Pearson相关系数的影响：噪声越大，相关系数越小
print("Higher noise", pearsonr(x, x + np.random.normal(0, 10, size)))

# 这个例子中，比较了变量在加入噪音之前和之后的差异。当噪音比较小的时候，相关性很强，P-value很低。
# 注意，使用Pearson相关系数主要是为了看特征之间的相关性，而不是和因变量之间的。

# %%
## Wrapper
### 递归特征消除
# 递归消除特征法使用一个基模型来进行多轮训练，每轮训练后，移除若干权值系数的特征（一些比较小的特征），再基于新的特征集进行下一轮训练。
# 对特征含有权重的预测模型(例如，线性模型对应参数coefficients)，RFE通过递归减少考察的特征集规模来选择特征。首先，预测模型在原始特征上训练，每个特征指定一个权重。之后，那些拥有最小绝对值权重的特征被踢出特征集。如此往复递归，直至剩余的特征数量达到所需的特征数量。

# 注：在做模型的过程中，可能会对模型做WOE处理，如果对模型的每个变量做WOE处理，那么输出的系数不代表模型的主要性；通常做一个线性
# 或者逻辑回归，特征的权重确实是变量的重要性，但做WOE处理后，并不代表重要程度，因为WOE绝对值的大小本身就是特征的重要程度，所以这个（逻辑回归的）系数只是一个表达系数而已

# RFECV 通过交叉验证的方式执行RFE，以此来选择最佳数量的特征：
# 对于一个数量为d的feature的集合，他的所有的子集的个数是2的d次方减1(包含空集)。指定一个外部的学习算法，比如SVM之类的。通过该算法计算所有子集的validation error。选择error最小的那个子集作为所挑选的特征。

# 导入RFE（Recursive Feature Elimination，递归特征消除）类，用于基于模型的特征选择
from sklearn.feature_selection import RFE
# 导入RandomForestClassifier（随机森林分类器），作为RFE的基模型来评估特征重要性
from sklearn.ensemble import RandomForestClassifier
# 导入load_iris函数，用于加载经典的鸢尾花数据集
from sklearn.datasets import load_iris

# 创建一个随机森林分类器对象，作为RFE的基模型（estimator）
# 随机森林会根据特征对模型预测的贡献度来评估特征重要性
rf = RandomForestClassifier()
# 加载鸢尾花数据集，包含150个样本，每个样本有4个特征，目标变量有3个类别
iris=load_iris()
# 将数据集拆分为特征矩阵X和目标变量y
# X是特征数据（150行×4列），y是标签数据（150个样本的类别标签）
X,y=iris.data,iris.target
# 创建RFE对象，使用随机森林作为基模型，选择3个最重要的特征
# estimator=rf：指定使用随机森林作为评估特征重要性的模型
# n_features_to_select=3：指定最终要选择的特征数量为3个（从原来的4个特征中选择3个）
rfe = RFE(estimator=rf, n_features_to_select=3)
# 对数据进行拟合和转换，执行递归特征消除过程
# fit_transform(X, y)会：
#   1. 使用随机森林训练模型，评估每个特征的重要性
#   2. 递归地移除重要性最低的特征，直到剩余3个特征
#   3. 返回筛选后的特征矩阵X_rfe（只包含选中的3个特征）
X_rfe = rfe.fit_transform(X,y)
# 查看筛选后特征矩阵的形状，应该是(150, 3)，即150个样本，3个特征
X_rfe.shape
# %%
# 查看筛选后特征矩阵的前5行数据，用于检查特征选择的结果
# X_rfe[:5,:] 表示取前5行（前5个样本）的所有列（所有选中的特征）
# 这样可以直观地看到经过RFE筛选后，每个样本的特征值是什么样的
X_rfe[:5,:]

# %%
## Embedded
# 使用SelectFromMode选择特征(Feature selection using SelectFromModel)
# 机器学习被引入风控系统很重要的一个体现

# 90年代用评分卡来做特征的模式：先把IV值、卡方、相关系数看一遍，还有XX因子，再画BiVar图，
# 再一层一层的看分箱结果，再调整模型

# 基于L1的特征选择
# 使用L1范数作为惩罚项的线性模型(Linear models)会得到稀疏解：大部分特征对应的系数为0。当你希望减少特征的维度以用于其它分类器时，可以通过 feature_selection.SelectFromModel 来选择不为0的系数。
# 特别指出，常用于此目的的稀疏预测模型有 linear_model.Lasso（回归）， linear_model.LogisticRegression 和 svm.LinearSVC（分类）

# L1可以做特征选择的原因：L1会把特征的权重归因到0，L1假设样本是服从XX分布
# L2是服从高斯分布，不会趋近于0

# 导入SelectFromModel类，用于基于模型的特征选择（Embedded方法）
# SelectFromModel可以根据模型的系数（权重）来选择特征，只保留系数不为0的特征
from sklearn.feature_selection import SelectFromModel
# 导入LinearSVC（线性支持向量分类器），作为基模型来评估特征重要性
# LinearSVC使用L1正则化时会产生稀疏解，即大部分特征的系数为0
from sklearn.svm import LinearSVC
# 创建并训练LinearSVC模型，使用L1正则化进行特征选择
# C=0.01：正则化强度的倒数，C越小，正则化越强，更多特征的系数会变为0
# penalty="l1"：使用L1正则化（Lasso），会产生稀疏解，将不重要特征的系数压缩为0
# dual=False：使用原始形式求解（当样本数>特征数时，原始形式更高效）
# fit(X, y)：在数据X和标签y上训练模型，训练后模型会学习到每个特征的系数（权重）
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X,y)
# 创建SelectFromModel对象，基于已训练的LinearSVC模型进行特征选择
# lsvc：使用已训练的LinearSVC模型作为评估特征重要性的基模型
# prefit=True：表示模型已经训练好了，不需要再次调用fit方法
# SelectFromModel会选择系数（权重）不为0的特征，系数为0的特征会被移除
model = SelectFromModel(lsvc, prefit=True)
# 对原始特征矩阵X进行转换，只保留系数不为0的特征
# transform(X)：根据模型的系数，筛选出重要特征（系数不为0的特征），返回筛选后的特征矩阵
X_embed = model.transform(X)
# 查看筛选后特征矩阵的形状，可以看到特征数量减少了（只保留了系数不为0的特征）
X_embed.shape

# %%
X_embed[:5,:]

# %% [markdown]
### 工作中常用的特征工程有哪些方法呢？
## 业务中的模型会遇到什么问题:
# - 模型效果不好：比如，做完模型特征筛选，进行模型训练，发现训练集上的模型KS只有20；模型训练不好一般是数据出了问题
# - 训练集效果好，跨时间测试效果不好：比如，需要更新模型的时候，会取过去一整年的模型数据来做模型，同时也会留出一部分未来的数据作为跨时间的数据进行模型测试，训练集的模型效果不错，但是跨时间集上的模型效果验证不行；一般验证集的KS不要比训练集的KS低5%
# - 跨时间测试效果也好，上线之后效果不好（一定是变量逻辑出问题，特征出现穿越，线下和线上的变量不一致）
# - 上线之后效果还好，几周之后分数分布开始下滑（肯定是模型的效果不行，有一两个变量跨时间测试不好）
# - 一两个月内都比较稳定，突然分数分布骤降（关注外部环境，政策的变化，其他公司暴雷）
# - 没有明显问题，但模型每个月逐步失效(无解，模型做完之后不可能一成不变)  

# 以上问题是建模的核心，个人觉得比高大上的算法重要得多，可以针对这些问题多深入思考原因。然后我们来考虑一下业务所需要的变量是什么。
# - 变量必须对模型有贡献，也就是说必须能对客群加以区分
# - 逻辑回归要求变量之间线性无关
# - 逻辑回归评分卡也希望变量呈现单调趋势 （有一部分也是业务原因，但从模型角度来看，单调变量未必一定比有转折的变量好）
# - 客群在每个变量上的分布稳定，分布迁移无可避免，但不能波动太大

# 划分等级时，一般是按照跨时间测试集来做的。跨时间验证集不能太小，容易出现偶然性。一般是四分之一的人用来做跨时间验证。
# 模型在训练和验证完成后，会将训练集和验证集的数据放到一起，重新训练一个模型。

# Question：逻辑回归为什么要求变量之间线性无关？
# Answer：逻辑回归的公式f(x) = sigmoid(w0 + w1*x1 + w2*x2 + ... + wn*xn)，
# 向量的点乘是一个相似度。

# %%
import pandas as pd
import numpy as np
import math
df_train = pd.read_csv('train.csv')
df_train.head()

# %%
## 变量重要性
# - IV值
# - 卡方检验
# - 模型筛选
# 这里我们使用IV值或者模型筛(XGBoost)选多一点（一般一种方法就行，差别不大）

# IV其实就是WOE前面加上一项
# - Pyi = yi/yt
# - Pni = ni/nt
# - WOEi = ln(Pyi/Pni)；WOE绝对值越大，代表特征越重要
# IVi = (Pyi - Pni) * WOEi
# IV = sum(IVi); 将每个区间的iv加起来得到总的iv值

# 选多少特征跟数据量大小有关系，比如说有100w数据量的样本，则变量不能超过1000个；
a = 0.4
b = 0.6
iv = (a - b) * math.log(a/b)
# %%
# 或者继承模型输出特征重要性
#lightGBM中的特征重要性
# feature = pd.DataFrame(
#             {'name' : model.booster_.feature_name(),
#             'importance' : model.feature_importances_
#           }).sort_values(by =  ['importance'],ascending = False)

#%%
# 计算分箱、WOE、IV值
import numpy as np
import pandas as pd
from scipy import stats

def mono_bin(Y,X,n=20):
    # 函数功能：对特征X进行等频分箱，确保分箱后的badrate具有单调性，并计算WOE和IV值
    # 参数说明：
    #   Y: 目标变量（标签），0表示好样本，1表示坏样本
    #   X: 需要分箱的特征变量
    #   n: 初始分箱数量，默认20
    # 返回值：包含分箱信息、WOE和IV值的DataFrame
    
    # 初始化Spearman相关系数r为0
    r=0
    # 计算坏样本数量：Y中值为1的样本数（假设1表示坏样本，0表示好样本）
    # 注意：变量名虽然叫good，但实际存储的是坏样本数
    good = Y.sum()
    # 计算好样本数量：总样本数减去坏样本数
    # 注意：变量名虽然叫bad，但实际存储的是好样本数
    bad = Y.count()-good
    # 循环寻找满足单调性要求的分箱数量
    # 当Spearman相关系数的绝对值小于1时，继续减少分箱数量
    # 目标：找到使分箱后的badrate呈现单调性的分箱数量
    while np.abs(r)< 1:
        # 创建包含特征X、目标变量Y和分箱结果的DataFrame
        # pd.qcut(X,n)：对X进行等频分箱，分成n个区间，每个区间包含大致相同数量的样本
        d1=pd.DataFrame({"X":X,"Y":Y,"Bucket":pd.qcut(X,n)})
        # 按分箱（Bucket）进行分组，as_index=True表示将Bucket作为索引
        d2=d1.groupby('Bucket',as_index=True)
        # 计算Spearman相关系数，评估分箱后X的均值与Y的均值之间的单调性
        # r: 相关系数，范围[-1,1]，绝对值越接近1表示单调性越强
        # p: p值，用于检验相关性的显著性
        r,p=stats.spearmanr(d2.mean().X,d2.mean().Y)
        # 如果单调性不够（|r|<1），减少分箱数量，继续尝试
        n=n-1
    # 创建结果DataFrame，初始化为每个分箱X的最小值
    d3=pd.DataFrame(d2.X.min(),columns=['min'])
    # 计算每个分箱中X的最小值
    d3['min']=d2.min().X
    # 计算每个分箱中X的最大值
    d3['max']=d2.max().X
    # 计算每个分箱中坏样本（Y=1）的总数
    d3['sum']=d2.sum().Y
    # 计算每个分箱中的总样本数
    d3['total']=d2.count().Y
    # 计算每个分箱的坏样本率（badrate）：坏样本数/总样本数
    d3['rate']=d2.mean().Y
    # 计算每个分箱的WOE（Weight of Evidence，证据权重）值
    # WOE = ln((分箱坏样本率/(1-分箱坏样本率)) / (总体坏样本率/(1-总体坏样本率)))
    # WOE绝对值越大，表示该分箱与总体差异越大，特征区分能力越强
    d3['woe']=np.log((d3['rate']/(1-d3['rate']))/(good/bad))
    # 计算每个分箱的IV（Information Value，信息价值）值
    # IV = (分箱坏样本率/(1-分箱坏样本率) - 总体坏样本率/(1-总体坏样本率)) * WOE
    # IV值用于衡量特征对目标变量的预测能力，IV值越大，特征越重要
    d3['iv']=(d3['rate']/(1-d3['rate']) - (good/bad)) * np.log((d3['rate']/(1-d3['rate']))/(good/bad))
    # 按最小值（min）列对结果进行排序，确保分箱按从小到大顺序排列
    # reset_index(drop=True)：重置索引，drop=True表示不保留原索引
    d4=(d3.sort_values(by='min')).reset_index(drop=True)
    # 打印分隔线，用于美化输出
    print("="*60)
    # 打印分箱结果，包含每个分箱的min、max、sum、total、rate、woe、iv等信息
    print(d4)
    # 返回排序后的分箱结果DataFrame
    return d4

mono_bin(df_train['label'], df_train['Age'], n=20)

# %%
## 2）共线性
# - 相关系数COR
# - 方差膨胀因子VIF

# 在做很多基于空间划分思想的模型的时候，我们必须关注变量之间的相关性。
# 单独看两个变量的时候我们会使用皮尔逊相关系数。
# 只选择数值型列计算相关系数，排除字符串类型的列（如姓名等）
# select_dtypes(include=[np.number]) 只选择数值型列（int和float类型）
df_train.select_dtypes(include=[np.number]).corr()

# %%
# 使用seaborn绘制变量间的散点图矩阵（pairplot），用于可视化数值型变量之间的相关性
import seaborn as sns
# 设置seaborn的主题和颜色方案，使用更新的API（set_theme替代已弃用的set）
sns.set_theme(color_codes=True)
# 设置随机数种子，确保结果可重现
np.random.seed(sum(map(ord, "distributions")))
# 只对数值型列绘制pairplot，排除字符串类型的列（如姓名等）
# pairplot会显示所有数值型变量两两之间的散点图和分布图，帮助识别变量间的相关性和分布特征
sns.pairplot(df_train.select_dtypes(include=[np.number]))

# 在多元回归中，我们可以通过计算方差膨胀系数VIF来检验回归模型是否存在严重的多重共线性问题。 定义：VIF = 1/(1-R^2)
# 其中,R为自变量 对其余自变量作回归分析的负相关系数。方差膨胀系数是容忍度的倒数。
# 方差膨胀系数VIF越大，说明自变量之间存在共线性的可能性越大。一般来讲，如果方差膨胀因子超过10，则回归模型存在严重的多重共线性。
# 又根据Hair(1995)的共线性诊断标准，当自变量的容忍度大于0.1，方差膨胀系数小于10的范围是可以接受的，表明白变量之间没有共线性问题存在

#%%
# 计算方差膨胀因子（VIF）来检验多重共线性
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
# 创建示例数据：4个样本，5个特征
# 注意：data的每一行代表一个样本，每一列代表一个特征
data = [[1, 2, 3, 4, 5],
        [2, 4, 6, 8, 9],
        [1, 1, 1, 1, 1],
        [2, 1, 6, 4, 7]]
# 将数据转换为numpy数组，并进行转置
# 转置后，每一行代表一个特征，每一列代表一个样本（这是variance_inflation_factor函数要求的格式）
X = np.array(data).T
# 计算第一个特征（索引0）的方差膨胀因子
# variance_inflation_factor(X, i) 计算第i个特征的VIF值
# VIF值越大，说明该特征与其他特征之间的共线性越严重
variance_inflation_factor(X, 0)

# %%
## 3）单调性
# - bivar图（无法避免，不管用什么风控模型，都需要掌握）

# 等频切分
df_train.loc[:,'fare_qcut'] = pd.qcut(df_train['Fare'], 10)
df_train.head()
df_train = df_train.sort_values('Fare')
alist = list(set(df_train['fare_qcut']))
badrate = {}
for x in alist:
    
    a = df_train[df_train.fare_qcut == x]
    
    bad = a[a.label == 1]['label'].count()
    good = a[a.label == 0]['label'].count()
    
    badrate[x] = bad/(bad+good)
f = zip(badrate.keys(),badrate.values())
f = sorted(f,key = lambda x : x[1],reverse = True )
badrate = pd.DataFrame(f)
badrate.columns = pd.Series(['cut','badrate'])
badrate = badrate.sort_values('cut')
print(badrate)
badrate.plot('cut','badrate')

# %%
# 对上述的bin进行重新分箱
def binn(x):
    if x < 10.5:   # 10.5以下为0，10.5-39.688为1，39.688以上为2
        return 0
    elif x < 39.688:
        return 1
    else:
        return 2
df_train['fare_cut_new'] = df_train['Fare'].map(lambda x : binn(x))
df_train.sample(100)

# %%
# 重新绘制Binvar图（单调性）
df_train = df_train.sort_values('Fare')
alist = list(set(df_train['fare_cut_new']))
badrate = {}
for x in alist:
    
    a = df_train[df_train.fare_cut_new == x]
    
    bad = a[a.label == 1]['label'].count()
    good = a[a.label == 0]['label'].count()
    
    badrate[x] = bad/(bad+good)
f = zip(badrate.keys(),badrate.values())
f = sorted(f,key = lambda x : x[1],reverse = True )
badrate = pd.DataFrame(f)
badrate.columns = pd.Series(['cut','badrate'])
badrate = badrate.sort_values('cut')
print(badrate)
badrate.plot('cut','badrate')

# %%
# 4）稳定性
# - PSI
# - 跨时间交叉检验

## 跨时间交叉检验
# 就是将样本按照月份切割，一次作为训练集和测试集来训练模型，取进入模型的变量之间的交集，
# 但是要小心共线特征

# 解决方法
# - 不需要每次都进入模型，大部分都在即可
# - 先去除共线性（这也是为什么集成模型我们也会去除共线性）

## 群体稳定性指标（population stability index）
# 公式：PSI = sum((实际占比 - 预期占比) * ln(实际占比 / 预期占比))

# 计算PSI（Population Stability Index，群体稳定性指标）的函数
# PSI用于衡量两个分布的差异程度，常用于评估特征或模型在不同时间段或不同样本上的稳定性
def psi(actual, expected):
    # 函数参数说明：
    #   actual: 实际分布，通常是一个列表或数组，表示当前时间段各分箱的样本数（或占比）
    #   expected: 预期分布（基准分布），通常是一个列表或数组，表示基准时间段各分箱的样本数（或占比）
    #   注意：actual和expected的长度必须相同，对应相同数量的分箱
    
    # 计算实际分布和预期分布的总计数（各分箱样本数的总和）
    # actual_cnt: 实际分布的总样本数
    # expected_cnt: 预期分布的总样本数
    actual_cnt, expected_cnt = sum(actual), sum(expected)
    # 检查边界情况：如果实际或预期的总计数为0，则无法计算PSI，返回None
    # 这种情况可能发生在数据为空或某个分布完全没有样本时
    if actual_cnt * expected_cnt == 0:
        return None
    # 初始化PSI值为0，用于累加每个分箱的PSI贡献
    PSI = 0
    # 遍历每个分箱（actual和expected的长度相同，对应相同数量的分箱）
    for i in range(len(actual)):
        # 计算第i个分箱在实际分布中的占比：该分箱的样本数 / 实际分布的总样本数
        actual_ratio = actual[i] / actual_cnt
        # 计算第i个分箱在预期分布中的占比：该分箱的样本数 / 预期分布的总样本数
        # 添加1e-10（一个极小的正数）避免除以0的情况，确保计算稳定性
        expected_ratio = expected[i] / expected_cnt + 1e-10 # 避免除以0
        # 计算第i个分箱对PSI的贡献，并累加到总PSI值中
        # PSI公式：PSI = sum((实际占比 - 预期占比) * ln(实际占比 / 预期占比))
        # 这个公式衡量了每个分箱的分布差异，差异越大，PSI值越大
        PSI += (actual_ratio - expected_ratio) * np.log(actual_ratio / expected_ratio)
    # 返回计算得到的PSI值
    # PSI值解释：
    #   PSI < 0.1: 分布非常稳定，差异很小
    #   0.1 <= PSI < 0.25: 分布相对稳定，有轻微差异
    #   PSI >= 0.25: 分布不稳定，差异较大，需要关注
    return PSI

# 注意分箱的数量将会影响着变量的PSI值
# PSI并不至可以对模型求，对变量也一样，只需要对跨时间分箱的数据分别求PSI即可

# %%
psi(df_train['label'], df_train['Age'])
# %%
