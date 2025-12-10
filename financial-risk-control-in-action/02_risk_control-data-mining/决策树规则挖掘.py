#%% [markdown]
# 熵形容纯度, 熵越大, 则纯度越高
# ID3、C4.5、CART为决策树的三大经典算法
# ID3: 信息增益
# C4.5: 信息增益比
# CART: 基尼系数
# 决策树的分类规则都是互斥且完备的, 即每个样本都被且只能被一条规则覆盖

# 项目背景: 滴滴给司机贷款有很多产品, oil_data_for_tree.xlsx是司机使用油品贷的数据（而不是加油数据）
# 一般贷款的整体坏账率是2%左右, 但最近发现油品贷的这些人坏账badrate明显比其他产品高很多, 差不多5%
# 怀疑是存在欺诈行为, 但是通过反欺诈规则没有检测出来, 同时我们希望模型能做的简单. 目前这些人已经有A卡评级(class_new)了
# 目前分析下来只有class_new=A的人群这个油品贷是挣钱的, 其他等级坏账率可能都到5%, 目标是怎么样让这个油品贷的坏账率降低

#%%
import pandas as pd
import numpy as np

#%%
# 读取文件, 文件中的数据是加油站司机加油的数据
data = pd.read_excel(r'oil_data_for_tree.xlsx')
data.head()
# uid代表是人的唯一标识(同一个人在文件中有多行)
# class_new代表贷款人的A卡评级
# oil_actv_dt表示客户第一次来贷款的日期（针对首次来贷款人做策略）
# create_dt为客户加油订单创建时间
# %%
set(data.class_new) # 查看A卡评级的种类
# 共分为A~F六个等级, 其中A～E均放款, F为拒绝放款

#%%
len(data[data.bad_ind == 1])/data.bad_ind.count() # 查看坏人率badrate，目前不到2%

#%%
# 对数据中变量进行处理，第一类为不需要特殊变化的数据，直接去重
org_lst = ['uid','create_dt','oil_actv_dt','class_new','bad_ind']  # bad_ind表示客户的好坏标识， 0代表好人，1代表坏人
# 第二类为数值型变量，做聚合
agg_lst = ['oil_amount','discount_amount','sale_amount','amount','pay_amount','coupon_amount','payment_coupon_amount']
# 第三类为文本类型，做cnt
dstc_lst = ['channel_code','oil_code','scene','source_app','call_source']

#%%
# 对数据进行重组
df = data[org_lst].copy()   # 对数据进行拷贝, 防止原始数据被修改
df[agg_lst] = data[agg_lst].copy() # data[column]表示获取data数据中的column列的数据, 并赋值给df[column], df数据集中会自动增加相应的列
df[dstc_lst] = data[dstc_lst].copy()


# %%
df.head()  #查看数据，得到了一份与data一模一样的数据
# %%
df.isna().sum()  # 查看数据中是否有空值, 如果为0, 则表示没有空值
# %%
df.describe() # 查看数据的基本统计信息（数量、平均值、最小值、25%(第一四分位数, 有25%的数据小于或等于此值)、50%、75%、最大值、标准差）

# %%
# 构造变量的时候不能直接对历史所有数据做累加，否则随着时间推移，变量分布会有很大的变化
# 讲师讲的是随着时间推移，平均值会变大（但我咋不觉得）。反正就是一般要截取去近6个月的数据
# 对create_dt进行处理，用oil_actv_dt填补create_dt的空值

# 定义一个函数，用于处理create_dt的空值
def time_isna(x,y):
    if str(x) == 'NaT':
        x = y
    else:
        x = x
    return x

# sort_values表示按照uid和create_dt进行排序，ascending = False表示降序
df2 = df.sort_values(['uid','create_dt'],ascending = False) # 排序后创建了新的数据集df2

# apply表示对df2中元素进行逐行遍历操作，用来代替for编辑df，axis = 1表示对行进行操作
# lambda为匿名函数，表示对df遍历时取出的具体某一行数据x，调用time_isna函数
# df是python中DataFrame类型，一般对应的是类似Excel一样的二维表
df2['create_dt'] = df2.apply(lambda x: time_isna(x.create_dt,x.oil_actv_dt),axis = 1)

# 对DataFrame中的两列进行相减，会得到一个新的DataFrame，
# 再用apply函数遍历新的DataFrame，并取出days列的值（去除计算出来每列后面的days单位）
# 最后将新生成的DataFrame赋值给df2的dtn列
df2['dtn'] = (df2.oil_actv_dt - df2.create_dt).apply(lambda x :x.days)
# 注意，这里用的是首次申请油品贷的时间，减去加油订单的创建时间，并筛选这个天数小于180天的订单
# 也就是首次申请油品贷申请之后创建的加油订单都需要，因为这个这些订单的dtn是小于0的（但是没有找到小于0的数据）
# 然后按照oil_actv_dt - create_dt计算出来的逻辑，拿的是这个客户首次申请贷款往前推180天的订单？
df = df2[df2['dtn']<180] # 筛选出dtn小于180天的数据
df.head()

#%%
# 对org_list变量求历史贷款天数的最大间隔，并且去重
base = df[org_lst]
base['dtn'] = df['dtn']
# base.head()
# 按照数据进行uid，create_dt进行降序排序
base = base.sort_values(['uid','create_dt'],ascending = False)
# 在排序后，对uid进行去重，保留第一次出现的数据，这样就拿到了历史贷款天数的最大间隔
base = base.drop_duplicates(['uid'],keep = 'first')
base.shape

# %%
# 做变量衍生
gn = pd.DataFrame()  # 创建一个空的DataFrame，有点像Java中默认的类构造器函数
for i in agg_lst:
    # 对数据按照uid进行分组得到每个uid的子分组，对每个子分组应用apply函数，求解该子分组中i列的行(个)数
    # 注：此时传入匿名函数lambada中的df是groupby函数返回的子分组，而不是原始数据集df
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:len(df[i])).reset_index())
    tp.columns = ['uid',i + '_cnt']
    if gn.empty == True:
        gn = tp  #遍历aggr_ls中第一个变量时，gn为空，所以先得到一个包含uid和oil_amount_cnt的DataFrame赋值给gn
    else:
        # 遍历aggr_lst第二个变量开始，gn不为空，所以将第二个开始新的到的tp与gn基于uid进行左连接合并，保留gn中所有列，会丢掉tp中的uid列
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')

    # lambada匿名函数中，增加了np.where函数，当df[i]>0时，返回1，否则返回0，然后求和得到df[i]中大于0的个数
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.where(df[i]>0,1,0).sum()).reset_index())
    tp.columns = ['uid',i + '_num']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nansum函数，对df[i]进行求和，其中NaN值会被转换为0（求和时忽略）
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nansum(df[i])).reset_index())
    tp.columns = ['uid',i + '_tot']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nanmean函数，对df[i]进行求平均，其中NaN会被忽略（计算总和和个数时均忽略）
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanmean(df[i])).reset_index())
    tp.columns = ['uid',i + '_avg']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')

    # lambada匿名函数中，增加了np.nanmax函数，对df[i]进行求最大值，其中NaN会被忽略
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanmax(df[i])).reset_index())
    tp.columns = ['uid',i + '_max']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nanmin函数，对df[i]进行求最小值，其中NaN会被忽略
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanmin(df[i])).reset_index())
    tp.columns = ['uid',i + '_min']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nanvar函数，对df[i]进行求方差，其中NaN会被忽略，NaN值不参与计算
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanvar(df[i])).reset_index())
    tp.columns = ['uid',i + '_var']
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nanmax函数和np.nanmin函数，对df[i]进行求最大值和最小值的差（极差），其中NaN会被忽略（为什么不直接采用numpy.ptp函数？）
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanmax(df[i]) -np.nanmin(df[i]) ).reset_index())
    tp.columns = ['uid',i + '_ptp']  # 原代码是i + '_var'，这里改为了i + '_ptp'，避免值被覆盖
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')
    
    # lambada匿名函数中，增加了np.nanmean函数和np.nanvar函数，对df[i]进行求平均值和（方差与1之间的较大者）的比值，其中NaN会被忽略，NaN值不参与计算
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df:np.nanmean(df[i])/max(np.nanvar(df[i]),1)).reset_index())
    tp.columns = ['uid',i + '_ratio'] # 原代码是i + '_var'，这里改为了i + '_ratio'，避免值被覆盖
    if gn.empty == True:
        gn = tp
    else:
        gn = pd.merge(gn,tp,on = 'uid',how = 'left')

# %%
# 对dstc_lst变量求distinct个数
gc = pd.DataFrame()
for i in dstc_lst:
    # 这里与上面不同，这里采用set函数去重，从而的到无重复的值个数
    tp = pd.DataFrame(df.groupby('uid').apply(lambda df: len(set(df[i]))).reset_index())
    tp.columns = ['uid',i + '_dstc']
    if gc.empty == True:
        gc = tp
    else:
        gc = pd.merge(gc,tp,on = 'uid',how = 'left')


# %%
# 对数据进行合并
fn = pd.merge(base,gn,on= 'uid')
fn = pd.merge(fn,gc,on= 'uid') 
fn.shape

#%%
fn = fn.fillna(0) # 将DataFrame二维表中的NaN填充为0
# %%
fn.head(100)
# %%
# 训练决策树模型
# 先删除一些不需要的列，因为后面axis=1所以代表删除列，如果axis=0则代表删除行
x = fn.drop(['uid','oil_actv_dt','create_dt','bad_ind','class_new'],axis = 1)
y = fn.bad_ind.copy()
# sklearn是Python中用于机器学习的库，其中tree模块提供了决策树的实现
from sklearn import tree

# DecisionTreeRegressor是决策树回归模型，用于预测连续值
# max_depth表示决策树的最大深度，min_samples_leaf表示每个叶节点的最小样本数，min_samples_split表示每个内部节点的最小样本数
dtree = tree.DecisionTreeRegressor(max_depth = 2,min_samples_leaf = 500,min_samples_split = 5000)
# 使用fit方法训练决策树模型，x为特征，y为目标变量（怎么理解这个y的目标变量，怎么体现这个目标）
# fit方法用于训练模型，predict方法用于预测模型，score方法用于评估模型
dtree = dtree.fit(x,y)

#绘制决策树，AI生成的代码
# import matplotlib.pyplot as plt
# from sklearn import tree

# plt.figure(figsize=(20,10))
# tree.plot_tree(dtree,filled=True,feature_names=x.columns)
# plt.show()

# %%
# 输出决策树图形，并作出决策树规则，AI生成的代码
import graphviz
dot_data = tree.export_graphviz(dtree, out_file=None, 
                                feature_names=x.columns,  
                                class_names=['good', 'bad'],  
                                filled=True, rounded=True,  
                                special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("decision_tree")  
graph
# %% [markdown]
# 对上述决策树结果的解释
# 第一层，先取到了amount_tot（代表历史加油量），如果此值大于48077.5，则判断为坏人，否则判断为好人
# 第二层，如果amount_tot小于48077.5，则再取到了oil_amount_cnt（代表历史加油次数），如果此值小于3.5，则判断为坏人，否则判断为好人
# 一个问题：这个决策树多跑几次，发现第一层去取amount_tot变量不会改变，但是第二层取oil_amount_cnt变量会被替换为其他变量
# 决策树中的value就是badrate，通过上述两条规则，amount_tot<=48077.5且oil_amount_cnt<=3.5，就可以筛选出1.2%的客户

#%%
sum(fn.bad_ind)/len(fn.bad_ind)  # 新的坏账率为4.65%
# 一般规则是做两三层

#%%
# 生成策略
# loc函数根据条件筛选数据，dff1中的数据为决策树结果中最右侧的分支
dff1 = fn.loc[(fn.amount_tot > 48077.5)&(fn.oil_amount_cnt > 3.5)].copy()
dff1['level'] = 'oil_A'  # 添加一个level列，值为oil_A
# dff2中的数据为决策树结果中中间的分支
dff2 = fn.loc[(fn.amount_tot > 48077.5)&(fn.oil_amount_cnt <= 3.5)].copy()
dff2['level'] = 'oil_B'  # 添加一个level列，值为oil_B
# dff3中的数据为决策树结果中最左侧的分支
dff3 = fn.loc[(fn.amount_tot <= 48077.5)].copy()
dff3['level'] = 'oil_C'  # 添加一个level列，值为oil_C

#%%
print(dff1.shape)
# 将dff1和dff2的数据合并，concat中默认参数是axis=0，默认合并增加行数
dff1 = pd.concat([dff1, dff2])
print(dff1.shape)
# 将dff1和dff3的数据合并，concat中默认参数是axis=0，默认合并增加行数
dff1 = pd.concat([dff1, dff3])
print(dff1.shape)

# %%
# 随机抽取dff1中的行or列数据，这里是取一行数据
dff1.sample()

# %%
# 返回一个包含class_new、level、bad_ind、uid、oil_actv_dt列的DataFrame
# 而['columns']表示返回的一个包含columns的Series
last = dff1[['class_new', 'level', 'bad_ind', 'uid', 'oil_actv_dt']].copy()
# 对oil_actv_dt列进行处理，取前7位字符串（取YYYY-MM）
last['oil_actv_dt'] = last['oil_actv_dt'].apply(lambda x: str(x)[:7]).copy()
last.sample(5)

# %%
# 将last数据保存为final_report.xlsx文件
last.to_excel('final_report.xlsx', index=False)