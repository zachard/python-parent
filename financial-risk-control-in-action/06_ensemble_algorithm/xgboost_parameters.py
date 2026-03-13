#%% [markdown]
# Xgboost，首先要去除变量之间的共线性；否则，对向量空间的描述会有障碍；<br/>
# 共线性对模型的训练没有什么影响；去掉共线性主要是去掉替代性强的变量；<br/>
# <br/>
# 为什么逻辑回归变量之间要不能相互替代？ <br/>
# 假设有f1到f10共10个变量，并且共线性强，那么可能最后的结果是f1变量的重要性是10，其他f2~f10变量的重要性都是1（在f1变量的基础上，f2～f9的变量只是让模型变得好一点点）<br/>
# 然后筛选变量的时候，会筛选重要性>5的变量，这样f2～f9变量其实都进不了模型；<br/>

# %% [markdown]
# Xgboost不具备模型可解释性；xgboost可以输出模型变量中每个变量的重要性，但是无法保证这个变量在模型中被使用；<br/>
# 可以线上xgboost，线下用逻辑回归模型，这样既可以保证模型的效果，又可以保证模型的可解释性；<br/>
# 线下的逻辑回归模型解释线上的xgboost模型，要求两个模型精度相差不大；<br/>

#%% [markdown]
# Xgboost的参数设置 <br/>
# 总共有3类参数：通用参数/general parameters, 集成(增强)参数/booster parameters 和 任务参数/task parameters <br/>
# 通用参数/general parameters <br/>
# booster [default=gbtree]； gbtree和gblinear；gbtree是默认值（树模型），gblinear是线性模型；<br/>
# silent [default=0]； 0表示输出信息， 1表示安静模式(不打印训练过程中输出的信息)；<br/>
# nthread； 跑xgboost的线程数，默认最大线程数；<br/>
# num_pbuffer [无需用户手动设定]； size of prediction buffer, normally set to number of training instances. The buffers are used to save the prediction results of last boosting step.  <br/>
# num_feature [无需用户手动设定]； feature dimension used in boosting, set to maximum dimension of the feature <br/>

# %% [markdown]
# 集成(增强)参数/booster parameters <br/>
# eta [default=0.3, 可以视作学习率]； 为了防止过拟合，更新过程中用到的收缩步长。在每次提升计算之后，算法会直接获得新特征的权重。 eta通过缩减特征的权重使提升计算过程更加保守。缺省值为0.3； 取值范围为：[0,1] ; 影响模型的学习速度；<br/>
# gamma [default=0, alias: min_split_loss]； 为了对树的叶子节点做进一步的分割而必须设置的损失减少的最小值，该值越大，算法越保守； range: [0,∞]； <br/>
# max_depth [default=6]； 用于设置树的最大深度（是多少层，最小是2次）； range: [1,∞]； 6层深的树的深度总共有2^6 - 1 = 63个叶子节点；<br/>
# min_child_weight [default=1]； 表示子树观测权重之和的最小值（分裂出来的叶子节点权重不能太小），如果树的生长时的某一步所生成的叶子结点，其观测权重之和小于min_child_weight，那么可以放弃该步生长，在线性回归模式中，这仅仅与每个结点所需的最小观测数相对应。该值越大，算法越保守； range: [0,∞] <br/>
# max_delta_step [default=0]； 如果该值为0，就是没有限制；如果设为一个正数，可以使每一步更新更加保守通常情况下这一参数是不需要设置的，但是在logistic回归的训练集中类极端不平衡的情况下，将这一参数的设置很有用，将该参数设为1-10可以控制每一步更新； range: [0,∞] <br/>
# subsample [default=1]； 表示观测的子样本的比率，将其设置为0.5意味着xgboost将随机抽取一半观测用于数的生长，这将有助于防止过拟合现象； range: (0,1] ；相当于随机森林的横采样<br/>
# colsample_bytree [default=1]； 表示用于构造每棵树时变量的子样本比率； range: (0,1]；表示列采样 <br/>
# colsample_bylevel [default=1]； 用来控制树的每一级的每一次分裂，对列数的采样的占比。一般不太用这个参数，因为subsample参数和colsample_bytree参数可以起到相同的作用。； range: (0,1] <br/>
# lambda [default=1, alias: reg_lambda]； L2 权重的L2正则化项； <br/>
# alpha [default=0, alias: reg_alpha]； L1 权重的L1正则化项； <br/> 
# <br/>
# tree_method, string [default='auto']； 树构造算法； 选择{'auto', 'exact', 'approx'}； <br/>
# 'auto': Use heuristic to choose faster one.<br/>
# 'exact': Exact greedy algorithm.<br/>
# 'approx': Approximate greedy algorithm using sketching and histogram.<br/>
# <br/>
# sketch_eps, [default=0.03]； 用于近似贪婪算法。<br/>
# scale_pos_weight, [default=1]； 在各类别样本十分不平衡时，把这个参数设定为一个正值，可以使算法更快收敛；<br/>
# updater, [default='grow_colmaker,prune']； 树更新器； 选择{'grow_colmaker', 'prune'}；<br/>
# refresh_leaf, [default=1]； 刷新叶子节点；<br/>
# <br/>
# process_type, [default='default']； 提升过程类型； 选择{'default', 'update'}；<br/>
# 'default': the normal boosting process which creates new trees.<br/>
# 'update': starts from an existing model and only updates its trees. In each boosting iteration, a tree from the initial model is taken, a specified sequence of updater plugins is run for that tree, and a modified tree is added to the new model. The new model would have either the same or smaller number of trees, depending on the number of boosting iteratons performed. Currently, the following built-in updater plugins could be meaningfully used with this process type: 'refresh', 'prune'. With 'update', one cannot use updater plugins that create new nrees.<br/>
# <br/>

#%% [markdown]
# 任务参数/task parameters <br/>
# objective [ default=reg:linear ] 这个参数定义需要被最小化的损失函数。最常用的值有<br/>
# "reg:linear" --线性回归<br/>
# "reg:logistic" --逻辑回归<br/>
# "binary:logistic" --二分类的逻辑回归，返回预测的概率(不是类别)<br/>
# "binary:logitraw" --输出归一化前的得分<br/>
# "count:poisson" --poisson regression for count data, output mean of poisson distribution<br/>
# <br/>
# max_delta_step is set to 0.7 by default in poisson regression (used to safeguard optimization)<br/>
# "multi:softmax" --设定XGBoost做多分类，你需要同时设定num_class(类别数)的值<br/>
# "multi:softprob" --输出维度为ndata * nclass的概率矩阵<br/>
# "rank:pairwise" --设定XGBoost去完成排序问题(最小化pairwise loss)<br/>
# "reg:gamma" --gamma regression with log-link. Output is a mean of gamma distribution. It might be useful, e.g., for modeling insurance claims severity, or for any outcome that might be <a href="https://en.wikipedia.org/wiki/Gamma_distribution#Applications">gamma-distributed</a><br/>
# "reg:tweedie" --Tweedie regression with log-link. It might be useful, e.g., for modeling total loss in insurance, or for any outcome that might be <a href="https://en.wikipedia.org/wiki/Tweedie_distribution#Applications">Tweedie-distributed</a>.<br/>
# <br/>
# base_score [ default=0.5 ] -- the initial prediction score of all instances, global bias<br/>
# for sufficient number of iterations, changing this value will not have too much effect.<br/>
# <br/>
# eval_metric [ 默认是根据 损失函数/目标函数 自动选定的 ] -- 有如下的选择:<br/>
# "rmse": <a href="http://en.wikipedia.org/wiki/Root_mean_square_error">均方误差</a><br/>
# "mae": <a href="https://en.wikipedia.org/wiki/Mean_absolute_error">绝对平均误差</a><br/>
# "logloss": negative <a href="http://en.wikipedia.org/wiki/Log-likelihood">log损失</a><br/>
# "error": 二分类的错误率<br/>
# "error@t": 通过提供t为阈值(而不是0.5)，计算错误率<br/>
# "merror": 多分类的错误类，计算公式为#(wrong cases)/#(all cases).<br/>
# "mlogloss": <a href="https://www.kaggle.com/wiki/MultiClassLogLoss">多类log损失</a><br/>
# "auc": <a href="http://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_curve">ROC曲线下方的面积</a> for ranking evaluation.<br/>
# "ndcg":<a href="http://en.wikipedia.org/wiki/NDCG">Normalized Discounted Cumulative Gain</a><br/>
# "map":<a href="http://en.wikipedia.org/wiki/Mean_average_precision#Mean_average_precision">平均准确率</a><br/>
# "ndcg@n","map@n": n can be assigned as an integer to cut off the top positions in the lists for evaluation.<br/>
# "ndcg-","map-","ndcg@n-","map@n-": In XGBoost, NDCG and MAP will evaluate the score of a list without any positive samples as 1. By adding "-" in the evaluation metric XGBoost will evaluate these score as 0 to be consistent under some conditions.
# training repeatedly<br/>
# <br/>
# seed [ default=0 ] -- random number seed.<br/>

#%% [markdown]
# 模型训练期望达到的效果：<br/>
#（1）KS/AUC最大；不建议用网络搜索，因为网络搜索训练出来是train训练集的指标最大，而不是off跨时间验证集的指标最大；<br/>
#（2）训练集的KS - 跨时间验证集的KS <= 5%；
# 依据以上两个目标，来挑选模型训练的参数；本质上想让跨时间验证集的KS最大，即argmax(off_KS)，而agrmin(train_KS - off_KS)；
# 所以在参数空间中，要argmax(off_KS + K*(off_KS - train_KS))； K代表一个参数；