#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.matplotlib_fname()
import missingno as msno #选安装msno
import seaborn as sns 
import math 
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier,_tree
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')
from sklearn.tree import _tree
from sklearn.metrics import roc_curve

data = pd.read_csv('LoanStats_2017Q2.csv',skiprows = 1)
data.head()
data.info()
# 使用 missingno 矩阵图可视化数据集中缺失值的分布与模式
msno.matrix(data)


# %%
check_null = data.isnull().sum().sort_values(ascending = False)/len(data)
check_null[check_null>0]  # 查看缺失比例大于0的变量

# %%
# 删除缺失比例0.5以上的变量
data = data.dropna(thresh = len(data)*0.5,axis = 1)
data = data.dropna(thresh = 0.5*len(data.columns),axis = 0)
# 检查是否有变量值是常数 pd.Series.nunique(self, dropna=True) 返回不同元素的数量,默认包括na
data = data.loc[:,data.apply(pd.Series.nunique) != 1]
# 检查是否有重复变量
len(set(list(data.columns))) == data.shape[1]
data.shape

# %%
target = data['loan_status'].value_counts() #目标变量，还款情况分布
print(target)
df_target = pd.DataFrame({'key':target.index[0:],'number':target.values[0:]})
plt.rc('font', family='SimHei', size=13)
fig = plt.figure(figsize = (16,12)) 
plt.pie(df_target.number,labels = df_target.key,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点） 
plt.title(u"贷款情况") 
plt.show()

# 单变量分布，贷款金额
sns.set_theme()
sns.histplot(data.loan_amnt, kde=True)
plt.ylabel('rate')
plt.title('loan_amount distribution')
plt.show()
# 单变量分布，贷款等级
a = data.grade.value_counts(1)
sns.set_theme()
plt.rc('font', family='SimHei', size=13)
sns.barplot(x=a.index, y=a.values)
plt.ylabel(u'人数')
plt.title(u'贷款等级')
plt.show()
# 单变量分布，工作年限
year = data.emp_length.value_counts()
sns.set_theme()
plt.rc('font', family='SimHei', size=13)
sns.barplot(x=year.index, y=year.values)
plt.xticks(rotation=90)
plt.ylabel(u'人数')
plt.title(u'工作年限情况')
plt.show()

# 双变量关系，贷款等级与贷款利率的关系
sns.set_theme()
plt.rc('font', family='SimHei', size=13)
data['int_rate'] = data['int_rate'].astype('str').str.strip("%").astype('float')
sns.boxplot(x = data.grade , y = data.int_rate,data = data)
plt.title(u'贷款等级与贷款利率的关系')
plt.show()
# 双变量关系，贷款等级与贷款金额关系
sns.set_theme()
plt.rc('font', family='SimHei', size=13)
sns.boxplot(x = data.grade , y = data.loan_amnt)
plt.title(u'贷款等级与贷款金额关系')
plt.show()

# 空值统计
object_col = data.select_dtypes(include = ['object']).columns
data[object_col].isnull().sum().sort_values(ascending = False)

# %%
# 数据格式转换
# =============================================================================
# data['int_rate'] = data['int_rate'].astype('str').str.strip("%").astype('float')
# data['revol_util'] = data['revol_util'].astype('str').str.strip("%").astype('float')
# data['issue_d'] = pd.to_datetime(data['issue_d'])
# data['earliest_cr_line'] = pd.to_datetime(data['earliest_cr_line'])
# =============================================================================
data.emp_title.value_counts()

data.loan_status.value_counts()
d = {'Current':0,
     'Fully Paid':0,
     'Charged Off':1,   # 这个定义为坏客户
     'Late (31-120 days)':1,
     'Late (16-30 days)':1,
     'In Grace Period':1,
    'Default':1}
df = data.copy(deep = True)
df.loan_status = df.loan_status.map(d)
df = df[df['loan_status'].notnull()]  #去除无还款信息的数据
df['loan_status'].value_counts(normalize=True) #样本平衡度

# %%
# 删除缺失率超过 50% 的自变量
miss_large_col = \
    [k for k,v in dict(df.isnull().sum()/df.shape[0]).items() if v>=0.5]
df = df.drop(miss_large_col,axis=1)

(df.isnull().sum() / df.shape[0]).sort_values(ascending=False)
df = df.drop(['mths_since_last_delinq'], axis=1) #mths_since_last_delinq这一列缺失率有0.48

# 数值集中度
tmp_list = []
for x in df.drop(['loan_status'],axis=1).columns:
    if df[x].value_counts(normalize=True).iloc[0] >=0.95:
        tmp_list.append((x, df[x].value_counts(normalize=True).iloc[0]))
tmp_list
not_col=[]
for x in df.drop(['loan_status'],axis=1).columns:
    if df[x].value_counts(normalize=True).iloc[0] >=0.95:
        not_col.append(x)
df = df.drop(not_col,axis=1)
print(df.shape[1]) #剩余88列特征池字段

# %%
# 格式转化、unique值处理
object_col = list(df.select_dtypes(include=['O']).columns)
df.loc[:,object_col].describe().T

df = df.drop(['emp_title', 'zip_code', 'sub_grade', 'addr_state'], axis=1)#去除意义不明显的字段
df['revol_util'] = df['revol_util']\
    .map(lambda x: float(x.split('%')[0])/100 if not pd.isnull(x) else x)
df['int_rate'] = df['int_rate']\
    .map(lambda x: float(x)/100 if not pd.isnull(x) else x)

df['emp_length'].unique()
d = {'10+ years':10, '< 1 year':0, '7 years':7,'2 years':2, '1 year':1,
       '3 years':3, '9 years':9, '8 years':8, '5 years':5, '6 years':6, '4 years':4}
df['emp_length'] = df['emp_length'].map(d)
# 日期相减
df['earliest_cr_line'] = pd.to_datetime('Jul-2018') - pd.to_datetime(df['earliest_cr_line'])
df['earliest_cr_line'] = df['earliest_cr_line'].map(lambda x:x.days)

df['last_pymnt_d'] = pd.to_datetime('Jul-2018') - pd.to_datetime(df['last_pymnt_d'])
df['last_pymnt_d'] = df['last_pymnt_d'].map(lambda x:x.days)

df['next_pymnt_d'] = pd.to_datetime('Jul-2018') - pd.to_datetime(df['next_pymnt_d'])
df['next_pymnt_d'] = df['next_pymnt_d'].map(lambda x:x.days)

df['last_credit_pull_d'] = pd.to_datetime('Jul-2018') - pd.to_datetime(df['last_credit_pull_d'])
df['last_credit_pull_d'] = df['last_credit_pull_d'].map(lambda x:x.days)

object_col = list(df.select_dtypes(include=['O']).columns) 
df.loc[:,object_col].describe().T

# %%
# 对剩余列进行检查
for ob in object_col: 
    print(ob, dict(df[ob].value_counts(normalize=True))) 
#home_ownership中`{'MORTGAGE': 0.50, 'RENT': 0.39, 'ANY': 4.7415387241467604e-05, 'OWN': 0.11, 'NONE': 1.896615489658704e-05}` ‘ANY’和NONE占比太少，用最多的MORTGAGE替换
df.loc[df.home_ownership.isin(['ANY', 'NONE']), 'home_ownership'] = 'MORTGAGE'

#依次查看每个object列关于是否逾期的分组条形图
for i in object_col:
     pvt=pd.pivot_table(df[['loan_status',i]],index=i,columns="loan_status",aggfunc=len)
     pvt.plot(kind="bar")
     
# 缺失值处理
rate = dict(df.isnull().sum()/df.shape[0]) 
#rate

cate_col = list(df.select_dtypes(include=['O']).columns) #4类别变量
num_col = [x for x in df.columns if x not in cate_col and x!='loan_status'] #57
d1 = [k for k,v in rate.items() if k in num_col and v>=0.05]
for i in d1:   df[i] = df[i].fillna(-999) #如果缺失值比例超过0.05，用-999代替作为一个特征值
d2 = [x for x in num_col if x not in d1] #比例没有超过0.05，用中位数填充
for i in d2:   df[i] = df[i].fillna(df[i].median())
df.loc[:,cate_col].isnull().sum() #类别类型无缺失，如果有可以用新的值或者占比最多的值填充

# %%
# 对类别变量进行WOE编码
def binning_cate(df,col,target):
     total = df[target].count()
     bad = df[target].sum()
     good = total-bad
     group = df.groupby([col],as_index=True)
     bin_df = pd.DataFrame()
     bin_df['total'] = group[target].count()
     bin_df['totalrate'] = bin_df['total']/total
     bin_df['bad'] = group[target].sum()
     bin_df['badrate'] = bin_df['bad']/bin_df['total']
     bin_df['good'] = bin_df['total'] - bin_df['bad']
     bin_df['goodrate'] = bin_df['good']/bin_df['total']
     bin_df['badattr'] = bin_df['bad']/bad
     bin_df['goodattr'] = (bin_df['total']-bin_df['bad'])/good
     bin_df['woe'] = np.log(bin_df['badattr']/bin_df['goodattr'])
     bin_df['bin_iv'] = (bin_df['badattr']-bin_df['goodattr'])*bin_df['woe']
     bin_df['iv'] = bin_df['bin_iv'].sum()
     return bin_df
cate_bin_df_list = []
cate_dict={}
for col in cate_col:#类别变量
     bin_df = binning_cate(df, col, 'loan_status')
     cate_bin_df_list.append(bin_df)
     cate_dict.setdefault(col,{})
     cate_dict[col]['bin_df']=bin_df
     #cate_dict[col]['cut'] = split_list
cate_iv_df = pd.DataFrame({'col':cate_col, 'iv':[x['iv'].iloc[0] for x in cate_bin_df_list]}).sort_values('iv',ascending=False).reset_index(drop=True) 
cate_iv_df #purpose出现inf。样本分布不平衡
df['purpose'].value_counts() 
df = df.loc[df.purpose != 'wedding'] #去掉wedding，重新计算整体iv
df['purpose'].value_counts()
cate_bin_df_list = [] 
for col in cate_col:#类别变量
     bin_df = binning_cate(df, col, 'loan_status')
     cate_bin_df_list.append(bin_df)
cate_iv_df = pd.DataFrame({'col':cate_col, 'iv':[x['iv'].iloc[0] for x in cate_bin_df_list]}).sort_values('iv',ascending=False).reset_index(drop=True) 

# 对数值变量分箱， 使用单变量决策树方法 
def tree_split(df,col,target,max_bin,min_binpct,nan_value):
     missing_rate = df[df[col]==nan_value].shape[0]/df.shape[0]
     if missing_rate < 0.05:
         x = np.array(df[col]).reshape(-1,1)
         y = np.array(df[target])
         tree = DecisionTreeClassifier(max_leaf_nodes=max_bin,min_samples_leaf=min_binpct)
         tree.fit(x,y)
         threshold = tree.tree_.threshold
         threshold = threshold[threshold!=_tree.TREE_UNDEFINED]
         split_list = sorted(threshold.tolist())
     else:
         x = np.array(df[df[col]!=nan_value][col]).reshape(-1,1)
         y = np.array(df[df[col]!=nan_value][target])
         tree = DecisionTreeClassifier(max_leaf_nodes=max_bin-1,min_samples_leaf=min_binpct)
         tree.fit(x,y)
         threshold = tree.tree_.threshold
         threshold = threshold[threshold!=_tree.TREE_UNDEFINED]
         split_list = sorted(threshold.tolist())
         split_list.insert(0,nan_value)
     return split_list
 
# 数值型特征的分箱，计算woe，IV 
def binning_num(df,col,target,cut):
    total = df[target].count()
    bad = df[target].sum()
    good = total-bad
    
    bucket = pd.cut(df[col],cut)
    group = df.groupby(bucket)
    bin_df = pd.DataFrame()
    
    bin_df['total'] = group[target].count()
    bin_df['totalrate'] = bin_df['total']/total
    bin_df['bad'] = group[target].sum()
    bin_df['badrate'] = bin_df['bad']/bin_df['total']
    bin_df['good'] = bin_df['total'] - bin_df['bad']
    bin_df['goodrate'] = bin_df['good']/bin_df['total']
    bin_df['badattr'] = bin_df['bad']/bad
    bin_df['goodattr'] = (bin_df['total']-bin_df['bad'])/good
    bin_df['woe'] = np.log(bin_df['badattr']/bin_df['goodattr'])
    bin_df['bin_iv'] = (bin_df['badattr']-bin_df['goodattr'])*bin_df['woe']
    bin_df['iv'] = bin_df['bin_iv'].sum()    
    return bin_df

num_dict={}
for col in num_col:
     split_list = tree_split(df,col,'loan_status',5,0.05,-999) #箱数控制在5箱，占比至少5%
     split_list.insert(0,float('-inf'))
     split_list.append(float('inf'))
     bin_df = binning_num(df,col,'loan_status',split_list)
     num_dict.setdefault(col,{})
     num_dict[col]['bin_df']=bin_df
     num_dict[col]['cut'] = split_list
num_iv_df = pd.DataFrame({'col':num_col,'iv':[num_dict[x]['bin_df']['iv'].iloc[0] for x in num_col]})\
.sort_values('iv',ascending=False).reset_index(drop=True)
num_iv_df.head()

# 阈值设定为0.03，将大于0.03的变量筛选出来,最后得到32个数值变量、2个类别变量
iv_select_num_col = list(num_iv_df[(num_iv_df.iv>0.03)&(num_iv_df.iv<0.5)]['col']) 
select_num_dict = {k:v for k,v in num_dict.items() if k in iv_select_num_col} 
len(iv_select_num_col)
iv_select_cate_col = list(cate_iv_df[(cate_iv_df.iv>0.03)&(cate_iv_df.iv<0.5)]['col'])
len(iv_select_cate_col)
iv_select_df = pd.concat([num_iv_df[(num_iv_df.iv>0.03)&(num_iv_df.iv<0.5)],cate_iv_df[(cate_iv_df.iv>0.03)&(cate_iv_df.iv<0.5)]],axis=0)\
               .sort_values('iv',ascending=False).reset_index(drop=True) 
df2 = df.loc[:,iv_select_num_col+iv_select_cate_col+['loan_status']] 
df2.shape

# 将原始变量转化为WOE变量,34个自变量，1个因变量
for col in iv_select_num_col:
    woe_list = list(select_num_dict[col]['bin_df']['woe'])
    cut = select_num_dict[col]['cut']
    df2[col+'_woe'] = pd.cut(df2[col], bins=cut, labels=woe_list)
for col in iv_select_cate_col:
    woe_dict = dict([x for x in cate_bin_df_list if x.index.name==col][0]['woe'])
    df2[col+'_woe'] = df2[col].map(woe_dict)
df2.head()

df2_woe = df2.loc[:, [x for x in df2.columns if x.find('woe')>0]+['loan_status']]
df2_woe.head()
for col in df2_woe.columns:
    df2_woe[col] = df2_woe[col].astype('float64')
    
# 根据相关系数去除多重共线性(0.7)
def forward_corr_delete(data,col_list):
    corr_list=[]
    corr_list.append(col_list[0])
    delete_col=[]
    for col in col_list[1:]:
        corr_list.append(col)
        corr = data.loc[:,corr_list].corr()
        corr_tup = [(k,v) for k,v in zip(corr[col].index,corr[col].values)]
        corr_value = [v for k,v in corr_tup if k!=col]
        if len([x for x in corr_value if abs(x)>=0.7])>0:
            delete_col.append(col)
    select_corr_col=[x for x in col_list if x not in delete_col]
    return select_corr_col

corr_col = [x+'_woe' for x in iv_select_df.col]
select_corr_col = forward_corr_delete(df2_woe,corr_col)
len(select_corr_col)
df2_woe2 = df2_woe.loc[:,select_corr_col+['loan_status']]
df2_woe2.head()

corr_df = df2_woe2.loc[:,select_corr_col].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr_df,annot=True,cmap='rainbow',vmax=1,vmin=-1,mask=np.abs(corr_df)<=0)

# 根据方差膨胀因子去除共线性(VIF<=10)
def vif_delete(df,list_corr):
    col_list = list_corr.copy()
    vifs_matrix = np.matrix(df[col_list])
    vifs_list = [variance_inflation_factor(vifs_matrix,i)for i in range(vifs_matrix.shape[1])]
    vif_high = [x for x,y in zip(col_list,vifs_list) if y>10]
    if len(vif_high)>0:
        for col in reversed(vif_high):
            col_list.remove(col)
            vif_matrix=np.matrix(df[col_list])
            vifs = [variance_inflation_factor(vif_matrix,i)for i in range(vif_matrix.shape[1])]
            if len([x for x in vifs if x>10])==0:
                break
    return col_list

vif_select_col = vif_delete(df2_woe2,select_corr_col)
len(vif_select_col)

# 根据p值进行显著性检验，前向逐步回归
def forward_pvalue_delete(x,y):
    col_list = x.columns.tolist()
    pvalues_col=[]
    for col in col_list:
        pvalues_col.append(col)
        x_const = sm.add_constant(x.loc[:,pvalues_col])
        sm_lr = sm.Logit(y,x_const)
        sm_lr = sm_lr.fit()
        pvalue = sm_lr.pvalues[col]
        if pvalue>=0.5:
            pvalues_col.remove(col)
    return pvalues_col

# 将数据集分为特征集X和标签集Y
x = df2_woe2.drop(['loan_status'],axis=1)
y = df2_woe2['loan_status']
# 做显著性筛选
pvalues_col = forward_pvalue_delete(x,y)
df2_woe3 = df2_woe2.loc[:, pvalues_col+['loan_status']]


# 简单建模，超参数使用默认
x2 = df2_woe3.drop(['loan_status'],axis=1)
y2 = df2_woe3['loan_status']
x_train,x_test,y_train,y_test = train_test_split(x2,y2,test_size=0.2,random_state=2021)
lr_model = LogisticRegression().fit(x_train,y_train)
coe_dict = {k:v for k,v in zip(x_train.columns,lr_model.coef_[0])}
#绘制roc曲线
def plot_roc(y_label,y_pred):
    tpr,fpr,threshold = metrics.roc_curve(y_label,y_pred)
    AUC = metrics.roc_auc_score(y_label,y_pred)
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(tpr,fpr,color='blue',label='AUC=%.3f'%AUC)
    ax.plot([0,1],[0,1],'r--')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_title('ROC')
    ax.legend(loc='best')
    return plt.show(ax)
#绘制KS曲线 
def plot_model_ks(y_label,y_pred):
    pred_list = list(y_pred)
    label_list = list(y_label)
    total_bad = sum(label_list)
    total_good = len(label_list)-total_bad
    items = sorted(zip(pred_list,label_list),key=lambda x :x[0])
    step = (max(pred_list)-min(pred_list))/200

    pred_bin = []
    good_rate = []
    bad_rate = []
    ks_list = []
    for i in range(1,201):
        idx = min(pred_list)+i*step
        pred_bin .append(idx)
        label_bin = [x[1] for x in items if x[0]<idx]
        bad_num = sum(label_bin)
        good_num = len(label_bin)-bad_num
        goodrate = good_num/total_good
        badrate =  bad_num/total_bad
        ks = abs(goodrate-badrate)
        good_rate.append(goodrate)
        bad_rate.append(badrate)
        ks_list.append(ks)
    fig = plt.figure(figsize=(6,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(pred_bin,good_rate,color='green',label='good_rate')
    ax.plot(pred_bin,bad_rate,color='red',label='bad_rate')
    ax.plot(pred_bin,ks_list,color='blue',label='good-bad')
    ax.set_title('KS:{:.3f}'.format(max(ks_list)))
    ax.legend(loc='best')
    return plt.show(ax)

y_pred = lr_model.predict_proba(x_test)[:,1]
plot_roc(y_test,y_pred) #
plot_model_ks(y_test,y_pred)
fpr,tpr,thre=roc_curve(y_test, y_pred)
ks=max(tpr-fpr)

# %%
# =============================================================================
# #利用交叉验证和网格搜索
# from sklearn.model_selection import GridSearchCV  #网格搜索
# from sklearn.linear_model import LogisticRegression # 逻辑回归
# from sklearn.model_selection import train_test_split # 测试集与训练集划分
# #构建网格参数组合
# param_test1={"C":[0.01,0.1,1.0,10.0,20.0,30.0,100.0,200.0,300.0,1000.0], #正则化系数
#             "penalty":["l1","l2"], #正则化参数
#             "max_iter":[100,200,300,400,500]} #算法收敛的最大迭代次数
# gsearch1=GridSearchCV(LogisticRegression(),param_grid=param_test1,cv=10)
# gsearch1.fit(x_train,y_train)  #训练模型
# gsearch1.best_params_, gsearch1.best_score_ 
# =============================================================================

# 使用SMOTE算法解决类别不平衡
from imblearn.over_sampling import SMOTE # 导入SMOTE算法模块,安装imblearn
# 处理不平衡数据
smo = SMOTE(random_state=42)    # 处理过采样的方法
x_train2, y_train2 = smo.fit_resample(x_train, y_train)
print('SMOTE平衡正负样本')
n_sample = y_train2.shape[0]
n_pos_sample = y_train2[y_train2 == 0].shape[0]
n_neg_sample = y_train2[y_train2 == 1].shape[0]
print('样本个数：{}; 正样本占{:.2%}; 负样本占{:.2%}'.format(n_sample,
                                                   n_pos_sample / n_sample,
                                                   n_neg_sample / n_sample))

lr_model_smo = LogisticRegression().fit(x_train2,y_train2)
y_pred_smo = lr_model_smo.predict_proba(x_test)[:,1]
plot_roc(y_test,y_pred_smo)
plot_model_ks(y_test, y_pred_smo)


# %%
# 刻度评分卡制作
#def cal_scale(score,odds,PDO,model):
#    B = PDO/np.log(2)
#    A = score+B*np.log(odds)
#    base_score = A-B*model.intercept_[0]
#    return A,B,base_score
#A,B,base_score = cal_scale(400,999/1,20,lr_model)

# 带概率校准的刻度评分卡制作
badratereal = 0.0217
badratesampled = 0.1

def cal_scale(score,odds,PDO,model):
    B = PDO/np.log(2)
    A = score+B*(np.log(odds) - np.log(badratesampled/badratereal))
    base_score = A-B*model.intercept_[0]
    return A,B,base_score
A,B,base_score = cal_scale(400,999/1,20,lr_model)

x_test_score = x_test.copy()
for col in x_test_score.columns:
    col_coe = coe_dict[col]
    x_test_score[col.replace('woe','score')]=x_test_score[col].map(lambda x:round(x*-B*col_coe))
x_test_score['score'] = round(base_score)
for col in [x for x in x_test_score.columns if x.find('_score')>=0]:
    x_test_score['score']+=x_test_score[col]
x_test_score['label']=list(y_test)

sns.kdeplot(x_test_score['score'],shade=True)
sns.kdeplot(x_test_score[x_test_score['label']==1].score,shade=True,label='bad')
sns.kdeplot(x_test_score[x_test_score['label']==0].score,shade=True,label='good')

# 模型上线 PSI指标计算
def cal_psi(exp, act):
    exp_df = exp.copy()
    act_df = act.copy()
    cut_ll = exp.quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    cut_ll = list(cut_ll.values.reshape(1,-1)[0])
    cut_ll.insert(0, float('-inf'))
    cut_ll.append(float('inf'))
    
    exp_df['cut'] = pd.cut(exp_df['score'], cut_ll)
    exp_group = exp_df.groupby(['cut'])
    
    act_df['cut'] = pd.cut(act_df['score'], cut_ll)
    act_group = act_df.groupby(['cut'])

    exp_cnt = exp_group['score'].count()
    act_cnt = act_group['score'].count()
    
    res_df = pd.concat([exp_cnt, act_cnt], join='outer', axis=1)
    res_df.columns = ['expected', 'actual']
    res_df['expected'] = res_df['expected']/res_df['expected'].sum()
    res_df['actual'] = res_df['actual']/res_df['actual'].sum()
    res_df['sub'] = res_df['actual'] - res_df['expected']
    res_df['chu'] = res_df['actual'] / res_df['expected']
    res_df['log'] = np.log(res_df['chu'])
    res_df['mul'] = res_df['sub'] * res_df['log']
    res_df['final'] = res_df['mul'].sum()    
    return res_df['final'].loc[0]

x_train_score = x_train.copy()
for col in x_train_score.columns:
    col_coe = coe_dict[col]
    x_train_score[col.replace('woe','score')]=x_train_score[col].map(lambda x:round(x*-B*col_coe))
x_train_score['score'] = round(base_score)
for col in [x for x in x_train_score.columns if x.find('_score')>=0]:
    x_train_score['score']+=x_train_score[col]
x_train_score['label']=list(y_train)

cal_psi(x_train_score[['score']], x_test_score[['score']])

file= "ScoreData.csv"

with open(file,"w")as fdata:
    fdata.write("base_score,{}\n".format(round(base_score)))
for i,col in enumerate(x_train.columns):
    print(i,col,type(i),type(col))
    if col.replace('_woe','') in cate_col:
        score= round(cate_dict[col.replace('_woe','')]['bin_df']['woe']*(-B*coe_dict[col]))
    if col.replace('_woe','') in num_col:
        score= round(num_dict[col.replace('_woe','')]['bin_df']['woe']*(-B*coe_dict[col]))
    score.name= "Score"
    score.index.name= col.replace('_woe','')
    score.to_csv(file,header=True,mode="a")
# %%
