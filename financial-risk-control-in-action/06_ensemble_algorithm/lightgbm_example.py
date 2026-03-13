#%% [markdown]
### LightGBM

#%% [markdown]
##### 1.读取csv数据并指定参数建模

#%%
# coding: utf-8
import json
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error


# 加载数据集合
print('Load data...')
df_train = pd.read_csv('./data/regression.train.txt', header=None, sep='\t')
df_test = pd.read_csv('./data/regression.test.txt', header=None, sep='\t')

# 设定训练集和测试集
y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

# 构建lgb中的Dataset格式，和xgboost中的DMatrix是对应的
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

# 敲定好一组参数
params = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'l2',  # 回归任务用 l2/rmse，不要用 auc（二分类指标）
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
}

print('开始训练...')
# 训练
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=20,
    valid_sets=[lgb_eval],
    callbacks=[lgb.early_stopping(stopping_rounds=5)],
)

# 保存模型
print('保存模型...')
# 保存模型到文件中
gbm.save_model('model.txt')

print('开始预测...')
# 预测
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
# 评估
print('预估结果的rmse为:')
print(mean_squared_error(y_test, y_pred) ** 0.5)

# %% [markdown]
##### 2.添加样本权重训练

#%%
# coding: utf-8
import json
import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

# 加载数据集
print('加载数据...')
df_train = pd.read_csv('./data/binary.train', header=None, sep='\t')
df_test = pd.read_csv('./data/binary.test', header=None, sep='\t')
W_train = pd.read_csv('./data/binary.train.weight', header=None)[0]
W_test = pd.read_csv('./data/binary.test.weight', header=None)[0]

y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

num_train, num_feature = X_train.shape
feature_name = ['feature_' + str(col) for col in range(num_feature)]

# 加载数据的同时加载权重，特征名与类别特征在 Dataset 中指定
lgb_train = lgb.Dataset(X_train, y_train,
                        weight=W_train, feature_name=feature_name,
                        categorical_feature=[21], free_raw_data=False)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train,
                       weight=W_test, free_raw_data=False)

# 设定参数
params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'binary_logloss',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}

print('开始训练...')
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    valid_sets=[lgb_train],  # 评估训练集，需传入列表
)

# %% [markdown]
##### 3.模型的载入与预测 

#%%
# 查看特征名称
print('完成10轮训练...')
print('第7个特征为:')
print(repr(lgb_train.feature_name[6]))

# 存储模型
gbm.save_model('./model/lgb_model.txt')

# 特征名称
print('特征名称:')
print(gbm.feature_name())

# 特征重要度
print('特征重要度:')
print(list(gbm.feature_importance()))

# 加载模型
print('加载模型用于预测')
bst = lgb.Booster(model_file='./model/lgb_model.txt')
# 预测
y_pred = bst.predict(X_test)
# 在测试集评估效果
print('在测试集上的rmse为:')
print(mean_squared_error(y_test, y_pred) ** 0.5)

#%% [markdown]
##### 4.接着之前的模型继续训练

# %%
# 继续训练
# 从./model/model.txt中加载模型初始化
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model='./model/lgb_model.txt',
    valid_sets=[lgb_eval],
)

print('以旧模型为初始化，完成第 10-20 轮训练...')

# 在训练的过程中调整超参数
# 比如这里调整的是学习率
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=[lgb_eval],
    callbacks=[lgb.reset_parameter(learning_rate=lambda i: 0.05 * (0.99 ** i))],
)

print('逐步调整学习率完成第 20-30 轮训练...')

# 调整其他超参数
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=[lgb_eval],
    callbacks=[lgb.reset_parameter(bagging_fraction=[0.7] * 5 + [0.6] * 5)],
)

print('逐步调整bagging比率完成第 30-40 轮训练...')

# %% [markdown]
##### 5.自定义损失函数

#%%
# 类似在xgboost中的形式
# 自定义损失函数需要
def loglikelood(preds, train_data):
    labels = train_data.get_label()
    preds = 1. / (1. + np.exp(-preds))
    grad = preds - labels
    hess = preds * (1. - preds)
    return grad, hess


# 自定义评估函数
def binary_error(preds, train_data):
    labels = train_data.get_label()
    return 'error', np.mean(labels != (preds > 0.5)), False


# 4.0+ 自定义目标需放入 params['objective']，不再使用 fobj 参数
params_custom = {**params, 'objective': loglikelood}
gbm = lgb.train(
    params_custom,
    lgb_train,
    num_boost_round=10,
    init_model=gbm,
    valid_sets=[lgb_eval],
    feval=binary_error,
)

print('用自定义的损失函数与评估标准完成第40-50轮...')

# %% [markdown]
#### sklearn与LightGBM配合使用
##### 1.LightGBM建模，sklearn评估

#%%
# coding: utf-8
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

# 加载数据
print('加载数据...')
df_train = pd.read_csv('./data/regression.train.txt', header=None, sep='\t')
df_test = pd.read_csv('./data/regression.test.txt', header=None, sep='\t')

# 取出特征和标签
y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

print('开始训练...')
# 直接初始化LGBMRegressor
# 这个LightGBM的Regressor和sklearn中其他Regressor基本是一致的
# 4.0+ early_stopping_rounds、eval_metric 需在构造函数中指定
gbm = lgb.LGBMRegressor(objective='regression',
                        num_leaves=31,
                        learning_rate=0.05,
                        n_estimators=20,
                        early_stopping_rounds=5,
                        eval_metric='l1')

# 使用fit函数拟合
gbm.fit(X_train, y_train, eval_set=[(X_test, y_test)])

# 预测
print('开始预测...')
y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration_)
# 评估预测结果
print('预测结果的rmse是:')
print(mean_squared_error(y_test, y_pred) ** 0.5)

# %% [markdown]
##### 2.网格搜索查找最优超参数

#%%
# 配合scikit-learn的网格搜索交叉验证选择最优超参数
estimator = lgb.LGBMRegressor(num_leaves=31)

param_grid = {
    'learning_rate': [0.01, 0.1, 1],
    'n_estimators': [20, 40]
}

gbm = GridSearchCV(estimator, param_grid)

gbm.fit(X_train, y_train)

print('用网格搜索找到的最优超参数为:')
print(gbm.best_params_)

# %% [markdown]
##### 3.绘图解释

#%%
# coding: utf-8
import lightgbm as lgb
import pandas as pd

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError('You need to install matplotlib for plotting.')

# 加载数据集
print('加载数据...')
df_train = pd.read_csv('./data/regression.train.txt', header=None, sep='\t')
df_test = pd.read_csv('./data/regression.test.txt', header=None, sep='\t')

# 取出特征和标签
y_train = df_train[0].values
y_test = df_test[0].values
X_train = df_train.drop(0, axis=1).values
X_test = df_test.drop(0, axis=1).values

# 构建lgb中的Dataset数据格式，特征名与类别特征在 Dataset 中指定（特征数按数据列数）
num_feature = X_train.shape[1]
feature_name = ['f' + str(i + 1) for i in range(num_feature)]
# 若有类别特征可设 categorical_feature，索引需在 [0, num_feature-1] 内
lgb_train = lgb.Dataset(X_train, y_train, feature_name=feature_name)
lgb_test = lgb.Dataset(X_test, y_test, reference=lgb_train)

# 设定参数
params = {
    'num_leaves': 5,
    'metric': ('l1', 'l2'),
    'verbose': 0
}

evals_result = {}  # to record eval results for plotting

print('开始训练...')
# 训练
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=100,
    valid_sets=[lgb_train, lgb_test],
    callbacks=[lgb.log_evaluation(period=10), lgb.record_evaluation(evals_result)],
)

print('在训练过程中绘图...')
ax = lgb.plot_metric(evals_result, metric='l1')
plt.show()

print('画出特征重要度...')
ax = lgb.plot_importance(gbm, max_num_features=10)
plt.show()

print('画出第84颗树...')
ax = lgb.plot_tree(gbm, tree_index=83, figsize=(20, 8), show_info=['split_gain'])
plt.show()

#print('用graphviz画出第84颗树...')
#graph = lgb.create_tree_digraph(gbm, tree_index=83, name='Tree84')
#graph.render(view=True)
# %%
