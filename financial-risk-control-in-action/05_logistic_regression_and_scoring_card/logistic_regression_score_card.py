#%% [markdown]
# **评分卡**
# - 建立逻辑回归模型(输出是概率，比如0是好人，1是坏人)  
# - 对模型进行评分映射(要搞清楚评分映射是怎么映射的) 
# > 要关心模型究竟如何评价   

#%% [markdown]
# **逻辑回归表达式** 
# $$y=\frac{1}{1+e^{-\theta}}$$
# $$\theta=WX + B$$

# %% [markdown]  
# **实现sigmoid函数**
# $$𝑠𝑖𝑔𝑚𝑜𝑖𝑑(x) = \frac{1}{1 + e^{-x}}$$

# %% [markdown]  
#**sigmoid函数的导数**
# $$\delta𝑠𝑖𝑔𝑚𝑜𝑖𝑑(𝑥)=\delta\frac{1}{1+e^{-x}}=\delta\frac{e^{-x}}{(1+e^{-x})^{2}}=\delta\frac{1}{1+e^{-x}}*\frac{e^{-x}}{1+e^{-x}}=𝑠𝑖𝑔𝑚𝑜𝑖𝑑(𝑥)*\frac{1+e^{-x}-1}{1+e^{-x}}=𝑠𝑖𝑔𝑚𝑜𝑖𝑑(𝑥)*(1-𝑠𝑖𝑔𝑚𝑜𝑖𝑑(𝑥))$$

# %% [markdown]  
# **损失函数(Cross-entropy, 交叉熵损失函数)**  <br>

# `信息熵:` $-PlogP$(P是概率, 小于1, 取反之后就是正数了), 这个值代表的是信息量, 如果值越大代表对当前情况越不确定, 信息不足. 


# $$loss = -\sum{{y_t}log{y_p} + (1 - y_t)log{(1 - y_p)}}$$

# $y_t$: 真实的Y值, 需要进行独热编码

# $y_p$: 预测的Y值

# %% [markdown]  
# **交叉熵求导**
# $$\frac{\delta loss}{\delta Y_p} = -\frac{\delta Y_tlogy_p}{\delta Y_p} = \sum_n^N{-\frac{Y_i}{P_i} + \frac{1 - Y_i}{1 - p_i}}$$

# %% [markdown]  
# **准确率计算** <br>

# `混淆矩阵`
# | T\Pre | Positive | Negative |
# | :---: | :---: | :---: |
# | Positive | TP | FN |
# | Negative | FP | TN |

# %% [markdown]  
# **评估指标** <br>

# `召回率计算`
# $$recall = \frac{TP}{TP + FP}$$

# `精准率计算`
# $$precision = \frac{TP}{TP + FN}$$

# %%  
# 背景：负责行为评分卡，A卡比较重要（因为坏的用户不会进入到B卡和C卡）
# B卡更多不会拒绝，更多的是做一下调额的操作；
# C卡更多的用于催收，一般只影响催收的效率；
import pandas as pd
from sklearn.metrics import roc_auc_score,roc_curve,auc
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import numpy as np
import random
import math


# %%
# obs_mth代表观察月，时间窗口，有五个月的数据
# bad_ind是好坏标签，0表示好人，1表示坏人
# uid是用户唯一标识
# 其余的字段为模型使用的特征；_score表示各种各样的分数（其他征信平台）；
# _info表示自身平台的信息；person_info表示个人信息；financial_info表示金融信息；（用金融模型生成的描述信息）
data = pd.read_csv('Bcard.txt')
data.head()

# %%
#看一下月份分布，我们用最后一个月做为跨时间验证集合，总共包含201806~201811的五个月的数据
data.obs_mth.unique()

# %%
data.shape  # 查看数据集的大小

# %%
# 将2018-11-30的数据作为跨时间验证集合，其余作为训练集
train = data[data.obs_mth != '2018-11-30'].reset_index().copy()
val = data[data.obs_mth == '2018-11-30'].reset_index().copy()

# %%
#这是我们全部的变量，info结尾的是自己做的无监督系统输出的个人表现，score结尾的是收费的外部征信数据
# 这些模型用到的特征都是已完成特征筛选的，并且完成了归一化处理
feature_lst = ['person_info','finance_info','credit_info','act_info','td_score','jxl_score','mj_score','rh_score']

# %%
# 将模型变量和Y变量分别存储，训练集和验证集均如此
x = train[feature_lst]
y = train['bad_ind']

val_x =  val[feature_lst]
val_y = val['bad_ind']

# 建立逻辑回归模型，并对模型进行训练
# class_weight: 类别权重，用于处理类别不平衡问题，可以传入一个字典，键为类别，值为权重（可以把负样本的权证增大，因为负样本一般比较少）
# random_state: 随机种子，用于控制随机性，保证结果可重复
lr_model = LogisticRegression(C=0.1)  # C 为正则化强度的倒数，越小正则越强
lr_model.fit(x, y)  # 用训练集特征 x 与标签 y 拟合模型

# %% [markdown]  
# `混淆矩阵`

# | T\Pre | Positive | Negative |
# | :---: | :---: | :---: |
# | Positive | TP | FN |
# | Negative | FP | TN |

#### 模型评价
# - KS值（业内认为最主流评价模型的指标）
# - ROC曲线 <br/>

# <br/>描绘的是不同的截断点时，并以FPR和TPR为横纵坐标轴，描述随着截断点的变小，TPR随着FPR的变化。   
# <br/>纵轴：TPR=正例分对的概率 = TP/(TP+FN)，其实就是查全率   
# <br/>横轴：FPR=负例分错的概率 = FP/(FP+TN)  
# <br/>
# <br/>作图步骤：
# <br/>根据学习器的预测结果（注意，是正例的概率值，非0/1变量）对样本进行排序（从大到小）-----这就是截断点依次选取的顺序
# <br/>按顺序选取截断点，并计算TPR和FPR---也可以只选取n个截断点，分别在1/n，2/n，3/n等位置
# <br/>连接所有的点（TPR，FPR）即为ROC图  

#### KS值

# <br/>作图步骤：

# <br/>根据学习器的预测结果（注意，是正例的概率值，非0/1变量）对样本进行排序（从大到小）-----这就是截断点依次选取的顺序  
# <br/>按顺序选取截断点，并计算TPR和FPR ---也可以只选取n个截断点，分别在1/n，2/n，3/n等位置  
# <br/>横轴为样本的占比百分比（最大100%），纵轴分别为TPR和FPR，可以得到KS曲线  
# <br/>TPR和FPR曲线分隔最开的位置就是最好的”截断点“，最大间隔距离就是KS值，通常>0.2即可认为模型有比较好偶的预测准确性  

# **KS值和ROC值的相同点和不同点**  
# <br/>相同点：本质上是完全一样的，经过公式上的证明；只是画的时候坐标轴不一样；
# <br/>但实际过程中，需要来看两个值的曲线；模型可能在某个分箱表现特别好，但是在别的分箱表现差（曲线会隆起，整体模型看起来效果好，但实际上KS很高）  

# %%
# 训练集：取预测为正类（坏样本）的概率，用于绘制 ROC
y_pred = lr_model.predict_proba(x)[:, 1]
fpr_lr_train, tpr_lr_train, _ = roc_curve(y, y_pred)  # 计算 FPR、TPR，用于 ROC 曲线
train_ks = abs(fpr_lr_train - tpr_lr_train).max()  # KS = 同一阈值下 |FPR - TPR| 的最大值
print('train_ks : ', train_ks)

y_pred = lr_model.predict_proba(val_x)[:,1]
fpr_lr,tpr_lr,_ = roc_curve(val_y,y_pred)
val_ks = abs(fpr_lr - tpr_lr).max()
print('val_ks : ',val_ks)

from matplotlib import pyplot as plt
plt.plot(fpr_lr_train,tpr_lr_train,label = 'train LR')
plt.plot(fpr_lr,tpr_lr,label = 'evl LR')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC Curve')
plt.legend(loc = 'best')
plt.show()
# 跨时间验证集比训练集的KS小4%，并且从曲线可以看出，跨时间验证集的ROC曲线表现没有训练集的ROC曲线表现好
# 模型验证的时候，跨时间验证集的KS与训练集的KS相差5%以内就还算OK
# 这个模型训练出来KS为0.41，作为A卡模型差强人意

# %%
#模型效果不佳，所以再做特征筛选
# 计算每个特征的VIF值，VIF值越大，说明特征之间的相关性越强，需要进行特征筛选
from statsmodels.stats.outliers_influence import variance_inflation_factor
X = np.array(x)
for i in range(X.shape[1]):
    print(variance_inflation_factor(X,i))
# variance一般大于10，需要进行特征筛选，不超过10一般都问题不大
# variance小于5的特征都还蛮好

# %%
import lightgbm as lgb
from sklearn.model_selection import train_test_split
# random_state=0: 随机种子，用于控制随机性，保证结果可重复
# test_size=0.2: 测试集比例，20%
# 未使用跨时间验证集数据，仅使用训练集数据，将原训练集数据划分为训练集和测试，数据比例为8:2
train_x,test_x,train_y,test_y = train_test_split(x,y,random_state=0,test_size=0.2)
def lgb_test(train_x, train_y, test_x, test_y):
    # LightGBM 二分类器参数说明：
    # boosting_type: 提升类型，gbdt 为梯度提升决策树
    # objective: 二分类任务
    # metric: 评估指标，AUC
    # learning_rate: 学习率
    # n_estimators: 树的数量（迭代轮数）
    # max_depth: 树的最大深度
    # num_leaves: 叶子节点数，控制模型复杂度
    # max_bin: 特征离散化时的最大分箱数
    # min_data_in_leaf: 叶子节点最少样本数，用于正则化
    # bagging_fraction: 每次迭代的样本采样比例
    # bagging_freq: 每多少次迭代进行一次 bagging
    # feature_fraction: 每次迭代的特征采样比例
    clf = lgb.LGBMClassifier(boosting_type='gbdt',
                             objective='binary',
                             metric='auc',
                             learning_rate=0.1,
                             n_estimators=24,
                             max_depth=5,
                             num_leaves=20,
                             max_bin=45,
                             min_data_in_leaf=6,
                             bagging_fraction=0.6,
                             bagging_freq=0,
                             feature_fraction=0.8,
                             )
    clf.fit(train_x,train_y,eval_set = [(train_x,train_y),(test_x,test_y)],eval_metric = 'auc')
    return clf,clf.best_score_['valid_1']['auc'],

lgb_model , lgb_auc  = lgb_test(train_x,train_y,test_x,test_y)
# 输出特征名字与特征重要性，并根据重要性排序
feature_importance = pd.DataFrame({'name':lgb_model.booster_.feature_name(),
                                   'importance':lgb_model.feature_importances_}).sort_values(by=['importance'],ascending=False)
feature_importance
# 从variance和feature_importance的结果来看，每个特征的重要性差别不大，没有哪个变量应该被剔除

# %%
# 然后对特征进行逐一剔除训练模型看效果（这里未体现），最终决定只保留4个特征
feature_lst = ['person_info','finance_info','credit_info','act_info']
# 之后只用选择的四个特征，重复了上述逻辑回归的过程；
x = train[feature_lst]
y = train['bad_ind']

val_x =  val[feature_lst]
val_y = val['bad_ind']

lr_model = LogisticRegression(C=0.1,class_weight='balanced')
lr_model.fit(x,y)
y_pred = lr_model.predict_proba(x)[:,1]
fpr_lr_train,tpr_lr_train,_ = roc_curve(y,y_pred)
train_ks = abs(fpr_lr_train - tpr_lr_train).max()
print('train_ks : ',train_ks)

y_pred = lr_model.predict_proba(val_x)[:,1]
fpr_lr,tpr_lr,_ = roc_curve(val_y,y_pred)
val_ks = abs(fpr_lr - tpr_lr).max()
print('val_ks : ',val_ks)
from matplotlib import pyplot as plt
plt.plot(fpr_lr_train,tpr_lr_train,label = 'train LR')
plt.plot(fpr_lr,tpr_lr,label = 'evl LR')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC Curve')
plt.legend(loc = 'best')
plt.show()
# 只保留4个特征的情况下，其实模型效果差不多，训练集的KS为0.4488；
# 跨时间验证集的KS为0.4196；差的不多，并且跨时间验证集KS也大于40%，ROC曲线看的模型低分段区分能力更强，高分段区分能力一般
# 可以看出这几个特征（去掉的）的影响还是很大，可以看一下这些变量的BinVar，是不是严格单调；

#%% [markdown]
# XGBoost如何保持模型的稳定性？
# 首先变量要保证是稳定的，其次要尝试做一些分箱，并保证分箱不要影响精度；

# %% [markdown]
# 模型报告  

#%% 
# 系数，每个特征的权重
print('变量名单：',feature_lst)
print('系数：',lr_model.coef_)
print('截距：',lr_model.intercept_)
# 截距：模型的偏置项，用于调整模型的预测结果

#%%
#生成报告（报告是在跨时间验证集上看的）
model = lr_model
row_num, col_num = 0, 0
bins = 20  # 对用户进行分箱，把跨时间验证集分为20箱
Y_predict = [s[1] for s in model.predict_proba(val_x)]
Y = val_y
nrows = Y.shape[0]
# 这个lis的结果只会有0和1两种取值
lis = [(Y_predict[i], Y[i]) for i in range(nrows)]
ks_lis = sorted(lis, key=lambda x: x[0], reverse=True) # 进行排列，越往后，人的风险越好
bin_num = int(nrows/bins+1)
# 因为y只有两种取值，1是坏人，0是好人，这里y>0.5这个条件可以改成y>0.1也可以，只是用来做区分
bad = sum([1 for (p, y) in ks_lis if y > 0.5])
good = sum([1 for (p, y) in ks_lis if y <= 0.5])
bad_cnt, good_cnt = 0, 0
# 报告中主要想看的几个数组；
KS = []
BAD = []
GOOD = []
BAD_CNT = []  # 到第几箱的坏样本累积个数；比如第一箱坏人是3个，第二箱是4个，那么到第二箱坏人累积的个数就是7个
GOOD_CNT = []
BAD_PCTG = [] # 到第几箱的坏样本累积占比；比如第一箱坏人是3个，第二箱是4个，那么到第二箱坏人的累积占比就是7/总坏人数
BADRATE = []
dct_report = {}
for j in range(bins):
    ds = ks_lis[j*bin_num: min((j+1)*bin_num, nrows)]
    bad1 = sum([1 for (p, y) in ds if y > 0.5])
    good1 = sum([1 for (p, y) in ds if y <= 0.5])
    bad_cnt += bad1
    good_cnt += good1
    bad_pctg = round(bad_cnt/sum(val_y),3)
    badrate = round(bad1/(bad1+good1),3)
    ks = round(math.fabs((bad_cnt / bad) - (good_cnt / good)),3)
    KS.append(ks)
    BAD.append(bad1)
    GOOD.append(good1)
    BAD_CNT.append(bad_cnt)
    GOOD_CNT.append(good_cnt)
    BAD_PCTG.append(bad_pctg)
    BADRATE.append(badrate)
    dct_report['KS'] = KS
    dct_report['BAD'] = BAD
    dct_report['GOOD'] = GOOD
    dct_report['BAD_CNT'] = BAD_CNT
    dct_report['GOOD_CNT'] = GOOD_CNT
    dct_report['BAD_PCTG'] = BAD_PCTG
    dct_report['BADRATE'] = BADRATE
val_repot = pd.DataFrame(dct_report)
val_repot
# 这个报告主要是看过滤，在箱号为10（第11箱）的时候，其实模型已经把87.5%的人捕捉到了
# 前4箱捕捉了57.3%的坏人；以及badrate是不是随着箱数的增加在减少（badrate应该保持单调递减，没有单调递减可能要考虑合并分箱）

#%% [markdown]
# 这些也是我们需要在贷后进行监控的（每月观察一次）
# 贷后的监控：分数分布，模型PSI，变量PSI，低分原因，捕获率，模型KS

# 通过率降低，可能说明模型正在失效
# 如果模型上线后捕捉率越来越高，那需要看一下分数的分布，模型可能正在失效了

#%%
from pyecharts.charts import *
from pyecharts import options as opts
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
np.set_printoptions(suppress=True)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
line = (

    Line()
    .add_xaxis(list(val_repot.index))
    .add_yaxis(
        "分组坏人占比",
        list(val_repot.BADRATE),
        yaxis_index=0,
        color="red",
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="行为评分卡模型表现"),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="累计坏人占比",
            type_="value",
            min_=0,
            max_=0.5,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="red")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        )

    )
    .add_xaxis(list(val_repot.index))
    .add_yaxis(
        "KS",
        list(val_repot['KS']),
        yaxis_index=1,
        color="blue",
        label_opts=opts.LabelOpts(is_show=False),
    )
)
line.render_notebook()
# 从图中可以看出，KS随着分箱线升高再降低，差不多在第6箱KS达到峰值；
# 分箱越往后，坏人占比越少，但存在凸起，说明模型效果不好；
# KS的值在越前的分箱越好，因为在越前可以更快的拒绝更多的人；原来可能6箱才拒绝10%的人，现在可能4箱就拒绝10%的人了；

# %% [markdown]
# 逻辑回归方程
# $$\ln\frac{P}{1-P} = w_{1}*x_{1} + w_{2}*x_{2} + ... + w_{n}*x_{n} + b$$  

# <br/>基础分650分；
# <br/>好的概率是坏的概率的2倍(2的1次方)时，加50分；
# <br/>好的概率是坏的概率的4倍(2的2次方)时，加100分；
# <br/>好的概率是坏的概率的8倍(2的3次方)时，加150分；
# <br/>...
# <br/>以此类推，得到分数换算公式：
# $$score = 650 + 50*\log_2\frac{P}{1-P}$$

# %%
#['person_info','finance_info','credit_info','act_info']
#算分数onekey 
def score(person_info,finance_info,credit_info,act_info):
    # 用特征工程处理过模型所需的变量，乘以对应变量的系数；得到xbeta
    xbeta = person_info * ( 3.49460978) + finance_info * ( 11.40051582 ) + credit_info * (2.45541981) + act_info * ( -1.68676079) --0.34484897 
    score = 650-34* (xbeta)/math.log(2) # 650为基础分，34为PDO，math.log(2)为对数底数
    return score
val['score'] = val.apply(lambda x : score(x.person_info,x.finance_info,x.credit_info,x.act_info) ,axis=1)

fpr_lr,tpr_lr,_ = roc_curve(val_y,val['score'])
val_ks = abs(fpr_lr - tpr_lr).max()
print('val_ks : ',val_ks)

#对应评级区间；根据模型输出的评分划分评级；分数越高评级越高
# 如果模型出现调整，对于同一个客户，希望客户的分数在模型调整前后，不会出现很大的变化（比如从790分突然降到500分）
# 并且要保证每个评级的人数分布在模型调整前后分布一样，比如：D评级会拒绝10%的人，模型调整完，D评级还是需要大致拒绝10%的人
# 所以需要根据当前用户分数和评级的人数分布，调整模型计算公式中的基础分（650分）和PDO（32）
def level(score):
    level = 0
    if score <= 600:
        level = "D"
    elif score <= 640 and score > 600 : 
        level = "C"
    elif score <= 680 and score > 640:
        level = "B"
    elif  score > 680 :
        level = "A"
    return level
val['level'] = val.score.map(lambda x : level(x) )

val.level.groupby(val.level).count()/len(val)

# 参数调整的过程：
# 在基础分为650分，PDO为32的情况下，A评级的人数占比为11.4%，B评级的人数占比为27.2%，C评级的人数占比为41.8%，D评级的人数占比为19.4%；分数占比还算是合理；
# 如果想将一部分人从B评级升级到A评级，需要调整基础分和PDO（从32调整为34）；
# 调整后，A评级的人数占比为14.4%，B评级的人数占比为24.0%，C评级的人数占比为39.1%，D评级的人数占比为22.4%；
# B评级确实有人员迁移到A评级；但是D评级的人数占比也增加了，可能是从C评级下移到D评级；
# 参数调整后，模型的KS应该跟调整前完全一样，如果不一样，说明有步骤出错了

# %%
# 看客群的分数分布；主要集中600～700分之间（因为基础分是650分，所以这也是合理，然后4个特征中，有一个特征的系数是负数）
# 特征做完WOE后，系数应该是正数，但是这里没做WOE
import seaborn as sns
sns.histplot(val.score, kde=True)

val = val.sort_values('score',ascending=True).reset_index(drop=True)
df2=val.bad_ind.groupby(val['level']).sum()
df3=val.bad_ind.groupby(val['level']).count()
print(df2/df3)

# %%
