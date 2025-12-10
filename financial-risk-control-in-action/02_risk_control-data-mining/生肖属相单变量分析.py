#%% [markedown]
# 背景: 入职一家新的公司, 目前不能做一些金额相关的策略及规则, 然后领导希望分析生肖属相是否与风险有关联
# 数据说明: ft_zodiac.txt 中包含每个订单的订单号、属相、星座；zodiac_label.txt 中包含每个订单的订单号、历史最大逾期天数、最后一次还款日期、客户标签
# 思路总结：确定需要分析的变量后，对选择的变量做分箱（星座和属相本身为离散变量，无需做分箱），计算每个分箱的badrate，看分箱之间的badrate差异大小决定变量是否有用

# %% [markdown]
# badrate=bad/total; 坏人率=坏人/总数

#%%
import pandas as pd
import numpy as np

#%%
# 读取订单与星座之间的数据
f = open(r'ft_zodiac.txt', encoding='utf-8')
ft_zodiac = pd.read_csv(f)  
print(ft_zodiac.shape)
ft_zodiac.head()  # 数据第一列为0,可能是数据提取错误

#%%
# set(ft_zodiac.zodiac) # 查看星座集合
len(set(ft_zodiac.zodiac))  # 查看星座的个数

# %%
# 读取订单与还款相关的数据
l = open(r'zodiac_label.txt')
zodiac_label=pd.read_csv(l)

ft_label = zodiac_label[zodiac_label['label'] != 2] # 去掉既不是好人, 也不是坏人的人
ft_label.head()

# %%
set(zodiac_label.label)
# label有0、1、2三个值；其中0代表是好人(历史最大逾期天数<5)，1代表坏人(历史最大逾期天数>15)

#%% [markdown]
# 将pd15作为分割节点, 并不是就是>15就是坏人, 小于15就是好人
# 而是会将pd>15天以上作为坏人, 小于5天的人作为好人, 对于5~15天区间的人丢掉
# 因为一个逾期15和一个逾期14天的人其实本质上没有什么区别, 做模型的时候必须找一个节点切出来好人/坏人, 但无论怎么找这个节点, 周围都会有一些相似的人, 所以需要在中间挖一个洞(把中间部分的人去掉)
# 模型最后的结果是一个二分类的结果, 结果要么好人, 要么坏人

# %%
# 拼接数据
data = pd.merge(ft_label,ft_zodiac,on = 'order_id',how = 'inner') # on表示拼接主键, how表示怎么关联
data.head()

# %%
# 把生肖和星座的集合取出来
zodiac_list = set(data.zodiac)
chinese_zodiac_list = set(data.chinese_zodiac)

# %%
# 计算星座的badrate
zodiac_badrate = {}
for x in zodiac_list:
#     a = data[data.zodiac == x]   # 先获取属于当前星座中的所有data数据
    
#     bad = a[a.label == 1]['label'].count()    # 再计算星座所有data数据中坏人(lable==1)的数量
#     good = a[a.label == 0]['label'].count()   # 再计算星座所有data数据中好人(lable==0)的数量
    
    # ['label']表示只获取label列的结果, 不然的话, 会展示data数据中的所有列的结果
    bad = data[(data.zodiac == x) & (data.label == 1)]['label'].count()   # 直接筛选星座为当前星座, 且为坏人的人
    good = data[(data.zodiac == x) & (data.label == 0)]['label'].count()   # 直接筛选星座为当前星座, 且为好人的人
    
    zodiac_badrate[x] = bad/(bad+good)

# %%
zodiac_badrate  # 打印badrate

# %%
# zodiac_badrate.keys()为一个['处女座', '魔蝎座',...]的数组, zodiac_badrate.values()同理
f = zip(zodiac_badrate.keys(),zodiac_badrate.values()) # zip后f得到一个<zip at 0x7f91df2a2c30>对象
# list(f)  # 得到一个[('处女座', 0.13035143769968052), ('摩羯座', 0.12920489296636087),...]数组

# 进行sorted函数排序, 排序方式为通过key取迭代对象中的一个元素进行排序, f为要排序的对象, reverse=True表示倒序
# lambda为匿名函数, 格式为lambda [args0, ...]:expression  # lambda为函数关键字, [args0,...]为函数入参, expression为函数逻辑
f = sorted(f,key = lambda x : x[1],reverse = True ) # key取迭代对象中元素时, x[1]表示取第二个元素(数组取数方式)
#list(f)

zodiac_badrate = pd.DataFrame(f) # 创建一个二维的表格或数据库中的数据表, 表格形式数据结构; 这一步还对badrate截取了一定的长度?
# columns为DataFrame 的列索引, 用于标识每列数据; Series创建一个带索引(系统内置)的一位数组
zodiac_badrate.columns = pd.Series(['星座','badrate'])
zodiac_badrate

# %%
from pyecharts.charts import Line
x = zodiac_badrate['星座'].astype(str).tolist()    # X轴标签, 新版本的Line必须这么转换类型
y = zodiac_badrate['badrate']  # Y轴标签
line = (
    Line().add_xaxis(x).add_yaxis('badrate', y)
)
line.render_notebook()
# 结论: 坏账率最高的为双鱼座, 为0.1487364; 坏账率最低的为天蝎座, 为0.120050; 这种坏账率的差异其实本质没什么差异
# 若要体现星座对逾期率之间有关系, 最大坏账率和最小坏账率之间应该至少相差一倍

# %%
#生肖
chinese_zodiac_badrate = {}
for x in chinese_zodiac_list:
    
    a = data[data.chinese_zodiac == x]
    
    bad = a[a.label == 1]['label'].count()
    good = a[a.label == 0]['label'].count()
    
    chinese_zodiac_badrate[x] = bad/(bad+good)

# %%
chinese_zodiac_badrate

# %%
f = zip(chinese_zodiac_badrate.keys(),chinese_zodiac_badrate.values())
f = sorted(f,key = lambda x : x[1],reverse = True )
chinese_zodiac_badrate = pd.DataFrame(f)
chinese_zodiac_badrate.columns = pd.Series(['生肖','badrate'])
chinese_zodiac_badrate

#%%
from pyecharts.charts import Line
x = chinese_zodiac_badrate['生肖'].astype(str).tolist()
y = chinese_zodiac_badrate['badrate']
line = (
    Line().add_xaxis(x).add_yaxis("badarate", y)
)
line.render_notebook()
# %%
