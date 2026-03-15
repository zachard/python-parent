#%% [markdown]
### 不均衡学习

#%% [markdown]
#### 数据不平衡

# 在很多真实场景下，数据集往往是不平衡的。也就是说，在数据集中，有一类含有的数据要远远多于其他类的数据（类别分布不平衡）。在贷款场景下，我们主要介绍二分类中的类别不平衡问题。<br/>
# 常识告诉我们一家信用正常客户的数据要远远多于欺诈客户的。<br/>  
# 考虑一个简单的例子，10万正样本（正常客户标签为0）与1000个负样本（欺诈客户标签为1），正负样本比列为100：1，如果直接带入模型中去学习，每一次梯度下降如果使用全量样本，负样本的权重只有不到1/100，即使完全不学习负样本的信息，准确率也有超过99%（因为正常客户就占了99%），所以显然我们绝不能以准确率来衡量模型的效果。但是实践下面，我们其实也知道，即使用KS或者AUC来度量模型的表现，依然没法保证模型能将负样本很好的学习。而我们实际上需要得到一个分类器，既能对于正例有很高的准确率，同时又不会影响到负例的准确率。<br/>
# 类似于上面例子中的数据集，由于整个数据空间中，正例和负例的数据就是不平衡的。因此，这样的不平衡数据集的产生往往是内在的。同时，也有很多其他的因素会造成数据的不平衡，例如，时间，存储等。由于这些原因产生不平衡的数据集往往被称为外在的。除了数据集的内在和外在，我们可能还要注意到数据集的相对不平衡以及绝对不平衡。假设上述例子中的数据集有100000条数据，负例和正例的比例为100:1，只包含1000个正例。明显的，我们不能说1000个数据就是绝对小的，只不过相对于负例来说，它的数量相对较少。因此，这样的数据集被认为是相对不平衡的。<br/>

# 一家公司的正常的客户一般都要远远多于坏客户，因为一个客户的坏账，需要很多个好客户才能覆盖坏账成本；<br/>

# %% [markdown]
#### 解决方法

# * 下探
# * 半监督学习
# * 标签分裂
# * 代价敏感
# * 采样算法

# %% [markdown]
# ### 下探

# 最直接解决风控场景样本不均衡的方法。(最简单粗暴，还有效)<br/>
# 下探的比例：5%-10%，10%比较常见；（看建模需要多少负样本）

#  所谓下探，就是对评分较低被拒绝的人进行放款，牺牲一部分收益，来积累坏样本，供后续模型学习。<br/>
# 这也是所有方法中最直接有效的。但是不是每一家公司都愿意承担这部分坏账。

# 此外我们之前提到过，随着业务开展，后续模型迭代的时候，使用的样本是有偏的，下探同样可以解决这个问题。（因为下探会添加之前未加到模型中的客户，所以定期隔一两个月去下探，就能解决不均衡和样本有偏差的问题）<br/>

# %% [markdown]
#### 半监督学习

# 将被（模型拒绝，不是反欺诈和硬规则拒绝，因为本来被反欺诈和硬规则拒绝的人不会进模型）拒绝客户的数据通过半监督的方法逐渐生成标签（好人/坏人标签），然后带入模型中进行训练。比较典型分方法有拒绝演绎、暴力半监督等等。<br/>
# 实际操作过程中，效果不好；本质上相当于把评分卡中那被拒绝的人拿出来用；<br/>

#### 1）拒绝演绎

# 拒绝演绎或者叫拒绝推断，是一种根据经验对低分客户进行百分比采样的方法。<br/>  
# 比如最低分的客群百分之五十视为坏人，其次百分之四十等等。<br/>   
# 效果没有下探好。但不用额外有任何开销。<br/>  
# 参考资料：群内预习资料中的《信用风险评分卡研究》第十三章。<br/>  

#### 2）暴力半监督

# 比较粗暴的做法是将样本的每一种标签方式进行穷举，带入模型看对模型是否有帮助，效率较低，容易过拟合（可能只是在数据集上表现好，过了一两个月后，表现变差）。 <br/>

#### 3）模型筛选

# 用训练过的其他模型对无标签样本打标签，然后模型进行训练。很多公司会用当前模型在上面做预测，然后带入模型继续训练。很不推荐这样做，效果一般是很差的。可以考虑无监督算法或者用很旧的样本做训练然后做预测。 <br/>

#### 等等...

#%% [markdown]
#### 标签分裂

# 我们有时候会不止使用传统的逾期或者rollrate来定义好坏（不止是只可以用这种方式来打标签）。而是通过一些聚类手段对数据进行切分，然后分别在自己的样本空间内单独学习。基于模型的比如kmeans，分层聚类等等。基于经验的比如将失联客户（风险高的客户）、欺诈客户拆开，单独建模。<br/>

# %% [markdown]
# 为什么要这样做呢？我们看一个例子。<br/>
# 小明生了慢粒白血病，她的失散多年的哥哥找到有2家比较好的医院，医院A和医院B供小明选择就医。<br/>
# 小明的哥哥多方打听，搜集了这两家医院的统计数据，它们是这样的：<br/>
# 医院A最近接收的1000个病人里，有900个活着，100个死了。<br/>
# 医院B最近接收的1000个病人里，有800个活着，200个死了。<br/>
# 作为对统计学懵懵懂懂的普通人来说，看起来最明智的选择应该是医院A对吧，病人存活率很高有90%啊！总不可能选医院B吧，存活率只有80%啊。<br/>
# 呵呵，如果小明的选择是医院A，那么她就中计了。<br/>
# 就这么说吧，如果医院A最近接收的1000个病人里，有100个病人病情很严重，900个病人病情并不严重。<br/>
# 在这100个病情严重的病人里，有30个活下来了，其他70人死了。所以病重的病人在医院A的存活率是30%。<br/>
# 而在病情不严重的900个病人里，870个活着，30个人死了。所以病情不严重的病人在医院A的存活率是96.7%。<br/>
# 在医院B最近接收的1000个病人里，有400个病情很严重，其中210个人存活，因此病重的病人在医院B的存活率是52.5%。<br/>
# 有600个病人病情不严重，590个人存活，所以病情不严重的病人在医院B的存活率是98.3%。<br/>
# 画成表格，就是这样的——<br/>

# %%
from IPython.display import Image
Image(filename='1.png', width=600)
# 单独拆出来，B的每个分类存活率都比A高，但是整体存活率A比B高；

# %% [markdown]
# 你可以看到，在区分了病情严重和不严重的病人后，不管怎么看，最好的选择都是医院B。但是只看整体的存活率，医院A反而是更好的选择了。所谓远看是汪峰，近看白岩松，就是这个道理。<br/>
# 实际上，我们刚刚看到的例子，就是统计学中著名的黑魔法之一——辛普森悖论（Simpson's paradox）。辛普森悖论就是当你把数据拆开细看的时候，细节和整体趋势完全不同的现象。<br/>

#%%
from IPython.display import Image
Image(filename='2.png', width=600) 
# 左图代表将样本合并在一块的训练效果，右图是代表将样本进行分类后分别训练的效果；对样本进行分别训练，得到的模型效果可能会更好；<br/>

# %% [markdown]
#### 代价敏感学习

# 代价敏感学习则是利用不同类别的样本被误分类而产生不同的代价(将代价转换为某种参数丢回模型，让模型着重考虑这部分)，使用这种方法解决数据不平衡问题。而且有很多研究表明，代价敏感学习和样本不平衡问题有很强的联系，并且使用代价敏感学习的方法解决不平衡学习问题要优于使用随机采样的方法。<br/> 

# 三种做法：<br/>
# 1) 把误分类代价作为数据集的权重，然后采用 Bootstrap 采样方法选择具有最好的数据分布的数据集；业内最常见的代价是一个负样本产生的坏账需要多少个正样本来弥补，然后按照这个比例来平衡数据集（未必会让模型效果变得更好）；<br/>
# 2) 以集成学习的模式来实现代价最小化的技术，这种方法可以选择很多标准的学习算法作为集成学习中的弱分类器；（例如：xgboost里面可以把权重作为参数传到模型损失函数里）<br/>
# 3) 把代价敏感函数或者特征直接合并到分类器的参数中，这样可以更好的拟合代价敏感函数。由于这类技术往往都具有特定的参数，因此这类方法没有统一的框架；(使用起来比较困难，除非没有什么好的变化才考虑使用)<br/>

# %% [markdown]
### 采样算法

# 今天我们涉及的主要是过采样方法<br/>

# * 朴素随机过采样
# * SMOTE
# * ADASYN

# %% [markdown]
#### 朴素随机过采样

# 把负样本中随机采样一些样本，然后加到负样本中（相当于对采样出来的负样本复制了一遍，进行加权）<br/>
# 朴素随机过采样是一种简单的过采样方法，它通过随机复制少数类样本，使少数类和多数类样本数量相同。这种方法的缺点是可能会导致过拟合，因为模型可能会学习到一些噪声。<br/>
# 日常业务中，正样本都会比较充足，一般对正样本随机采样就能满足；一般对正样本进行下采样；所以一般很少提下采样（因为正样本采用基本用这种方法就行，不会丢失信息，除非下采样的量级特别低）<br/>

#%%
# 一般不推荐使用
from sklearn.datasets import make_classification
from collections import Counter
# 生成不平衡二分类数据：n_samples 样本数，n_features 特征数，n_informative 有效特征数，
# n_redundant/n_repeated 冗余/重复特征数，n_classes 类别数，n_clusters_per_class 每类簇数，
# weights 各类比例（少数类 1%、多数类 99%），class_sep 类间分离度，random_state 随机种子
X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=2,
                           n_clusters_per_class=1,
                           weights=[0.01, 0.99],
                           class_sep=0.8, random_state=0)
Counter(y)

#%%
# RandomOverSampler为随机过采样函数；
from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0) # 1:1进行随机过采样
X_resampled, y_resampled = ros.fit_resample(X, y)
sorted(Counter(y_resampled).items())

# %% [markdown]
#### SMOTE

# SMOTE: 对于少数类样本a, 随机选择一个最近邻的样本b, 然后从a与b的连线上随机选取一个点c作为新的少数类样本；  <br/>
# 但是，SMOTE容易出现过泛化和高方差的问题，而且，容易制造出重叠的数据。<br/>
# SMOTE算法是好的，但是直接使用起来容易过拟合；

#%%
Image(filename='3.jpg', width=800) 

#%% [markdown]
# 为了克服SMOTE的缺点，Adaptive Synthetic Sampling方法被提出，主要包括：Borderline-SMOTE和Adaptive Synthetic Sampling（ADA-SYN）算法。<br/>
# Borderline-SMOTE（实际场景中会用到，本节课程最重要的算法）：对靠近边界的minority样本创造新数据。其与SMOTE的不同是：SMOTE是对每一个minority样本产生综合新样本，而Borderline-SMOTE仅对靠近边界的minority样本创造新数据。如下图，只对A中的部分数据进行操作： <br/>

#%%
# 少量样本可以分为三种：噪声（异常值）、边缘样本、安全样本；<br/>
# 噪声：远离其他样本的样本，通常是异常值；（一般去掉，不进入模型）<br/>
# 边缘样本：靠近边界，容易被误分类的样本；（一般利用这部分数据采样）<br/>
# 安全样本：远离边界，不容易被误分类的样本；（一般不需要处理，直接进入模型）<br/>
Image(filename='5.png', width=800) 

#%%
Image(filename='4.png', width=800) 

#%% [markdown]
# 这个图中展示了该方法的实现过程，我们可以发现和SMOTE方法的不同之处：  <br/>
# SMOTE对于每一个少数类样本都会产生合成样本，但是Borderline-SMOTE只会对邻近边界的少数类样本生成合成数据。<br/>

# Borderline-SMOTE还分两种算法：<br/>
# Borderline SMOTE-2和Borderline SMOTE-1是很类似的，区别是在得到DANGER集合之后，对于DANGER中的每一个样本点xi：<br/>   
# Borderline SMOTE-1：从少数类样本集合P中得到k个最近邻样本，再随机选择样本点和xi作随机的线性插值产生新的少数类样本。（和普通SMOTE算法流程相同,通常使用这种方法）<br/>
# Borderline SMOTE-2：从少数类样本集合P和多数类样本集合N中分别得到k个最近邻样本Pk和Nk。设定一个比例a，在Pk中选出a比例的样本点和x作随机的线性插值产生新的少数类样本，方法同Borderline SMOTE-1；在Nk中选出1-a比例的样本点和x作随机的线性插值产生新的少数类样本，此处的随机数范围选择的是（0.0.5），即使得产生的新的样本点更靠近少数类样本。<br/>

# %% [markdown]
# ADA-SYN：根据majority和minority的密度分布，动态改变权重，决定要generate多少minority的新数据。<br/>
# 使用效果没有Borderline-SMOTE好 <br/>

#%%
Image(filename='6.png', width=800) 
#%%
Image(filename='7.png', width=800) 

#%% [markdown]
# 基于聚类的随机采样（CBO）<br/>
# 基于聚类的随机采样方法可以用来解决类内不平衡问题，主要利用的聚类的方法。具体的过程如下：  <br/>

# 随机选择K个样本作为K个簇，并且计算K类样本在特征空间的平均值，作为聚类中心；  <br/>
# 对于剩下的每一个样本，计算它和K个聚类中心的欧氏距离，根据欧式聚类将其分配到最近的类簇中；  <br/>
# 更新每个簇的聚类中心，直到所有的样本都用完；  <br/>  

#%%
Image(filename='9.png', width=500) 

# %%
Image(filename='8.png', width=800) 

# %% [markdown]
# 采样方法和集成方法的集成 <br/>
# 目前已经有很多的方法把随机采样和集成学习的方法集成在一起，下面介绍两种这样的方法：<br/>

# * SMOTEBoost  
# * DataBoost-IM  

# #### SMOTEBoost
# SMOTEBoost主要是把SMOTE和AdaBoost.M2集成在一起，SMOTEBoost方法在每次Boost迭代过程中使用合成数据的方法。因此，每一次迭代过程中的分类器都会集中到更多的少数类样本。<br/>

# #### DataBoost-IM
# DataBoost-IM主要是把数据生成技术和AdaBoost.M1方法结合在一起，主要根据不同类之间样本的很难被学习到的比例。具体过程主要是如下：<br/>

# %%
Image(filename='10.png', width=800) 

# %%
from imblearn.over_sampling import SMOTE, ADASYN
X_resampled_smote, y_resampled_smote = SMOTE().fit_resample(X, y)
sorted(Counter(y_resampled_smote).items())

# %%
X_resampled_adasyn, y_resampled_adasyn = ADASYN().fit_resample(X, y)
sorted(Counter(y_resampled_adasyn).items())
# %%

#%% [markdown]
# 相对于基本的SMOTE算法, 关注的是所有的少数类样本, 这些情况可能会导致产生次优的决策函数。  <br/>    
# 因此SMOTE就产生了一些变体，这些方法关注在最优化决策函数边界的一些少数类样本, 然后在最近邻类的相反方向生成样本。<br/>
# SMOTE函数中的kind参数控制了选择哪种变体<br/>
# * regular 
# * borderline1 
# * borderline2 
# * svm 

# %%
from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE
# 新版 imblearn 中 SMOTE 不再支持 kind，Borderline-SMOTE 需使用 BorderlineSMOTE（kind='borderline1' 即默认）
X_resampled, y_resampled = BorderlineSMOTE(kind='borderline-1').fit_resample(X, y)

sorted(Counter(y_resampled).items())
# %% [markdown]
# 接下来我们启用上一节课的例子<br/>

# 使用过采样算法的两条准则：<br/>
# （1）要相信当前负样本可以代表负样本空间；即便当前的负样本数量很少；例如：当有1000个负样本时，可以说这1000个负样本可以代表负样本空间，但是当只有10个负样本时，明显对这10个负样本进行过采样也很难代表负样本空间；（10个负样本不是样本不平衡的问题，而是负样本过少根本无法学习到负样本空间）<br/>
# （2）负样本中的数据要干净；对于预测不准的样本（本来是好人被预测为坏人），将这些样本减小权重，不参与过采样；并且特征也要干净，是经过筛选的（排除噪声很大的特征）<br/>

#%%
import glob
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import roc_auc_score,roc_curve,auc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV as gscv
from sklearn.neighbors import KNeighborsClassifier 
data = pd.read_csv('Acard.txt')
data.head()

# %%
data.obs_mth.unique()

# %%
train = data[data.obs_mth != '2018-11-30'].reset_index().copy()
evl = data[data.obs_mth == '2018-11-30'].reset_index().copy()

# %%
#这是我们全部的变量，info结尾的是自己做的无监督系统输出的个人表现，score结尾的是收费的外部征信数据
feature_lst = ['person_info','finance_info','credit_info','act_info']
x = train[feature_lst]
y = train['bad_ind']

val_x =  evl[feature_lst]
val_y = evl['bad_ind']

lr_model = LogisticRegression(C=0.1) # 没有进行加权
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

# %%
x = train[feature_lst]
y = train['bad_ind']

evl_x =  evl[feature_lst]
evl_y = evl['bad_ind']

# 进行加权，训练集和跨时间验证集的KS均会提升
# 如果只有训练集或者跨时间验证集的KS提升，另外一个数据集的KS没有提升，那么这个加权的方法还有待考究
lr_model = LogisticRegression(C=0.1,class_weight='balanced')
lr_model.fit(x,y)

y_pred = lr_model.predict_proba(x)[:,1]
fpr_lr_train,tpr_lr_train,_ = roc_curve(y,y_pred)
train_ks = abs(fpr_lr_train - tpr_lr_train).max()
print('train_ks : ',train_ks)

y_pred = lr_model.predict_proba(evl_x)[:,1]
fpr_lr,tpr_lr,_ = roc_curve(evl_y,y_pred)
evl_ks = abs(fpr_lr - tpr_lr).max()
print('evl_ks : ',evl_ks)

from matplotlib import pyplot as plt
plt.plot(fpr_lr_train,tpr_lr_train,label = 'train LR')
plt.plot(fpr_lr,tpr_lr,label = 'evl LR')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC Curve')
plt.legend(loc = 'best')
plt.show()

# %% [markdown]
# 接下来通过样本插值的方法，让模型的KS逼近LightGBM模型的KS； <br/> 
# 也就是通过加权产生新样本，然后重新训练模型，对四个变量的系数进行微调，同时在线上部署一个逻辑回归的评分卡，在系数微调后，达到的效果跟上线一个集成算法的效果是一致的 <br/>

# 接下来先用lgb做预测，然后做前融合。 <br/>
# 相比于不修改损失函数的xgb，lgb的优势只是比较快。 <br/>

# 这里的思想类似于对训练样本做异常点检测， <br/>
# 只不过不是根据数据内部分布差异，而是使用精准度更高的集成模型， <br/>
# 将难以辨认的样本，视为噪音。 <br/>
# 可以理解为大神都做不对的题目，就别给普通学员学了，可能会适得其反。 <br/>

# 首先做网格调参，给lgb找一组较好的参数 <br/>

# %%
train_x,test_x,train_y,test_y = train_test_split(x,y,random_state=0,test_size=0.4)

params = {
            'boosting_type':'gbdt',
            'objective':'binary',
            'metric':'auc',
            'nthread':4,
            'learning_rate':0.1,
            'num_leaves':30,
            'max_depth':5,
            'subsample':0.8,
            'colsample_bytree':0.8,
        }

data_train = lgb.Dataset(train_x,train_y)

# 4.0+ early_stopping_rounds 改为通过 callbacks 传入
cv_results = lgb.cv(
    params,
    data_train,
    num_boost_round=1000,
    nfold=5,
    stratified=False,
    shuffle=True,
    metrics='auc',
    seed=0,
    callbacks=[lgb.early_stopping(stopping_rounds=100)],
)
# 4.0+ cv 返回的 key 为 'valid auc-mean'，旧版为 'auc-mean'
auc_mean_key = 'valid auc-mean' if 'valid auc-mean' in cv_results else 'auc-mean'
print('best n_estimators:', len(cv_results[auc_mean_key]))
print('best cv score:', pd.Series(cv_results[auc_mean_key]).max())
# 最终结果显示29棵树的效果比较好；<br/>

# %%
def  lgb_test(train_x,train_y,test_x,test_y):
    clf =lgb.LGBMClassifier(boosting_type = 'gbdt',
                           objective = 'binary',
                           metric = 'auc',
                           learning_rate = 0.1,
                           n_estimators = 29,  # 29棵树的效果比较好；设置为上一步结果中的树深度
                           max_depth = 4,
                           num_leaves = 25,
                           max_bin = 40,
                           min_data_in_leaf = 5,
                           bagging_fraction = 0.6,
                           bagging_freq = 0,
                           feature_fraction = 0.8,
                           )
    clf.fit(train_x,train_y,eval_set = [(train_x,train_y),(test_x,test_y)],eval_metric = 'auc')
    return clf,clf.best_score_['valid_1']['auc'],
lgb_model , lgb_auc  = lgb_test(train_x,train_y,test_x,test_y)
feature_importance = pd.DataFrame({'name':lgb_model.booster_.feature_name(),
                                   'importance':lgb_model.feature_importances_}).sort_values(by=['importance'],ascending=False)

pred = lgb_model.predict_proba(train_x)[:,1]
fpr_lgb,tpr_lgb,_ = roc_curve(train_y,pred)
print(abs(fpr_lgb - tpr_lgb).max())
    
pred = lgb_model.predict_proba(test_x)[:,1]
fpr_lgb,tpr_lgb,_ = roc_curve(test_y,pred)
print(abs(fpr_lgb - tpr_lgb).max())

pred = lgb_model.predict_proba(evl_x)[:,1]
fpr_lgb,tpr_lgb,_ = roc_curve(evl_y,pred)
print(abs(fpr_lgb - tpr_lgb).max())

# %% [markdown]
# 粗略调参的lgb比lr无显著提升，下面进行权重调整。 <br/>
# 前后各取部分错分样本，减小权重，其余样本为1。 <br/>
# 虽然后面还会给予新的权重，但是这部分权重永远只有正常样本的固定比例。 <br/>

# %%
sample = x[feature_lst]
sample['bad_ind'] = y
# 先按照坏人概率的预测值进行排序；排在最前面的认为是坏人
sample['pred'] = lgb_model.predict_proba(x)[:,1]
sample = sample.sort_values(by=['pred'],ascending=False).reset_index()

sample['rank'] = np.array(sample.index)/75522

def weight(x,y):
    if x == 0 and y < 0.1:
        return 0.1  # 坏人中，前10%中原本为好人，但被判定为坏人的人，权重为0.1
    elif x == 1 and y > 0.7:
        return 0.1  # 好人中，后30%中原本为坏人，但被判定为好人的人，权重为0.1
    else:
        return 1

# 错分的人权重为0.1
sample['weight'] = sample.apply(lambda x: weight(x.bad_ind,x['rank']),axis = 1)

def lr_wt_predict(train_x,train_y,evl_x,evl_y,weight):
    lr_model = LogisticRegression(C=0.1,class_weight='balanced')
    lr_model.fit(train_x,train_y,sample_weight = weight )
    
    y_pred = lr_model.predict_proba(train_x)[:,1]
    fpr_lr,tpr_lr,_ = roc_curve(train_y,y_pred)
    train_ks = abs(fpr_lr - tpr_lr).max()
    print('train_ks : ',train_ks)
    
    y_pred = lr_model.predict_proba(evl_x)[:,1]
    fpr_lr,tpr_lr,_ = roc_curve(evl_y,y_pred)
    evl_ks = abs(fpr_lr - tpr_lr).max()
    print('evl_ks : ',evl_ks)
    
# 提升了一些模型的KS
lr_wt_predict(sample[feature_lst],sample['bad_ind'],evl_x,evl_y,sample['weight'])

# %% [markdown]
# 此时的lr，相比于最开始的lr，提升了1个百分点。<br/>

# 这里省略了一些其他的探索，由于其他算法实验效果不理想，最终选取lgb作为筛选样本的工具。<br/>

# 接下来考虑基于差值思想的过采样方法，增加一部分虚拟的负样本。<br/>
# 这里需要注意，之前权重减小的样本是不应该用来做过采样的。<br/>
# 所以将训练数据先拆分成两部分(对训练集进行改变，而不改变跨时间验证集)。weight=1的做过采样，其余的不变。<br/>

#%%
osvp_sample = sample[sample.weight == 1].drop(['pred','index','weight'],axis = 1)
osnu_sample = sample[sample.weight < 1].drop(['pred','index',],axis = 1)

train_x_osvp = osvp_sample[feature_lst]
train_y_osvp = osvp_sample['bad_ind']

# %%
# 下面做基于borderline1的smote算法做过采样
def lr_predict(train_x,train_y,evl_x,evl_y):
    lr_model = LogisticRegression(C=0.1,class_weight='balanced')
    lr_model.fit(train_x,train_y)
    
    y_pred = lr_model.predict_proba(train_x)[:,1]
    fpr_lr,tpr_lr,_ = roc_curve(train_y,y_pred)
    train_ks = abs(fpr_lr - tpr_lr).max()
    print('train_ks : ',train_ks)
    
    y_pred = lr_model.predict_proba(evl_x)[:,1]
    fpr_lr,tpr_lr,_ = roc_curve(evl_y,y_pred)
    evl_ks = abs(fpr_lr - tpr_lr).max()
    print('evl_ks : ',evl_ks)
    return train_ks,evl_ks

from imblearn.over_sampling import SMOTE, RandomOverSampler, ADASYN, BorderlineSMOTE
# 新版 SMOTE 无 kind 参数，Borderline-SMOTE 使用 BorderlineSMOTE，kind 为 'borderline-1' 或 'borderline-2'
# k_neighbors: 用于确定SMOTE算法中的邻居数量
# m_neighbors: 用于确定Borderline-SMOTE算法中的邻居数量
# n_jobs: 用于并行计算的CPU核心数
# random_state: 用于设置随机种子，保证结果可重复
# kind: 用于指定Borderline-SMOTE的类型，'borderline-1' 或 'borderline-2'
# ratio: 用于指定过采样比例，'auto' 表示根据数据集自动确定比例
# svm_estimator: 用于指定SVM分类器，'auto' 表示自动选择SVM分类器
# out_step: 用于指定过采样步长，'deprecated' 表示不使用该参数
# 
smote = BorderlineSMOTE(k_neighbors=15, kind='borderline-1', m_neighbors=4, random_state=0)
rex,rey = smote.fit_resample(train_x_osvp,train_y_osvp)
print('badpctn:',rey.sum()/len(rey))  # 当前负样本站总样本的比例；可以看到正负样本的比例为1:1
df_rex = pd.DataFrame(rex)
df_rex.columns =feature_lst
df_rex['weight'] = 1
df_rex['bad_ind'] = rey
df_aff_ovsp = pd.concat([df_rex, osnu_sample], axis=0)
lr_predict(df_aff_ovsp[feature_lst],df_aff_ovsp['bad_ind'],evl_x,evl_y)

#%% [markdown]
# 下面尝试使用KNN做前融合，<br/>
# 主要思想是knn和逻辑回归对样本的分布先验是相同的，<br/>
# 虽然是弱分类器，<br/>
# 识别出的异常值应该对模型影响更大。<br/>
# 
# 首先寻找最优k值 <br/>

# %%
lr_model = LogisticRegression(C=0.1,class_weight='balanced')
lr_model.fit(df_aff_ovsp[feature_lst],df_aff_ovsp['bad_ind'] )
    
y_pred = lr_model.predict_proba(df_aff_ovsp[feature_lst])[:,1]
fpr_lr_train,tpr_lr_train,_ = roc_curve(df_aff_ovsp['bad_ind'],y_pred)
train_ks = abs(fpr_lr_train - tpr_lr_train).max()
print('train_ks : ',train_ks)
    
y_pred = lr_model.predict_proba(evl_x)[:,1]
fpr_lr,tpr_lr,_ = roc_curve(evl_y,y_pred)
evl_ks = abs(fpr_lr - tpr_lr).max()
print('evl_ks : ',evl_ks)

from matplotlib import pyplot as plt
plt.plot(fpr_lr_train,tpr_lr_train,label = 'train LR')
plt.plot(fpr_lr,tpr_lr,label = 'evl LR')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC Curve')
plt.legend(loc = 'best')
plt.show()
# 可以看到，最终跨时间验证集上，是有3.5个百分点的提升的。而训练集上提升了5个百分点，较为符合预期，过拟合的风险不是很大。<br/>
