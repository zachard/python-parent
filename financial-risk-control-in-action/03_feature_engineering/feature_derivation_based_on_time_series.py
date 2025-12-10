#%% [markdown]
#### 基于时间序列进行特征衍生

#%%
import pandas as pd
import numpy as np

#%%
# 数据说明：ft1~ft2是一个变量，代表加油次数，ft1代表离当前时间一个月内计算出来的ft（比如：当前时间是20251129，则ft1代表20251029到20251129的加油次数）
# ft2代表离当前时间一个月到两个月内计算出来的ft（比如：当前时间是20251129，则ft2代表20250929到20251029的加油次数），以此内推
# gt1～gt12也是一个变量，代表加油金额，gt1代表离当前时间一个月内计算出来的gt（比如：当前时间是20251129，则gt1代表20251029到20251129的加油金额），以此内推
data = pd.read_excel('textdata.xlsx')
data.head()

#%%
# 先自定义37个函数（对变量进行变化）
#最近p个月，inv>0的月份数
def Num(inv,p):
    # 从数据中提取从inv+'1'到inv+str(p)的所有列，例如：如果inv='ft', p=4，则提取ft1, ft2, ft3, ft4列
    # data.loc[:,inv+'1':inv+str(p)] 表示选择所有行，列从inv+'1'到inv+str(p)（包含两端）
    df=data.loc[:,inv+'1':inv+str(p)]
    # 数据框（DataFrame）类似于Excel表格，包含多行多列的数据
    # 这里的df是一个数据框，包含从inv+'1'到inv+str(p)的所有列（例如：ft1, ft2, ft3, ft4列）
    # 使用np.where将数据框中每个单元格（类似于Excel单元格）大于0的值标记为1，否则标记为0
    # 然后使用sum(axis=1)按行求和，得到每行中inv>0的月份数（即每行中值为1的个数）
    auto_value=np.where(df>0,1,0).sum(axis=1) #axis=0则表示按列求和
    # 返回特征名称（格式：inv_num+p，例如：ft_num4）和对应的值数组（每行inv>0的月份数）
    return inv+'_num'+str(p),auto_value

#最近p个月，inv=0的月份数
def Nmz(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.where(df==0,1,0).sum(axis=1)
    return inv+'_nmz'+str(p),auto_value


#最近p个月，inv>0的月份数是否>=1     
def Evr(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    # 计算每行中inv>0的月份数：将大于0的值标记为1，否则为0，然后按行求和
    # arr是一个一维数组，每个元素表示对应行中inv>0的月份数
    arr=np.where(df>0,1,0).sum(axis=1)
    # 判断arr中的值是否>=1：如果月份数>=1（即arr>=1），则标记为1，否则标记为0
    # np.where(arr,1,0) 会将非零值（即>=1的情况）转换为1，零值转换为0
    auto_value = np.where(arr,1,0)
    # 返回特征名称（格式：inv_evr+p，例如：ft_evr4）和对应的值数组（每行是否至少有1个月inv>0）
    return inv+'_evr'+str(p),auto_value

#最近p个月，inv均值
def Avg(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nanmean(df,axis = 1 )
    return inv+'_avg'+str(p),auto_value    


#最近p个月，inv和
def Tot(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nansum(df,axis = 1)
    return inv+'_tot'+str(p),auto_value  


#最近(2,p+1)个月，inv和

def Tot2T(inv,p):
    df=data.loc[:,inv+'2':inv+str(p+1)]
    auto_value=df.sum(1)
    return inv+'_tot2t'+str(p),auto_value


#最近p个月，inv最大值
def Max(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nanmax(df,axis = 1)
    return inv+'_max'+str(p),auto_value 


#最近p个月，inv最小值
def Min(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nanmin(df,axis = 1)
    return inv+'_min'+str(p),auto_value

#最近p个月，最近一次inv>0到现在的月份数
def Msg(inv,p):
    # 从数据中提取从inv+'1'到inv+str(p)的所有列（例如：ft1到ft4）
    df=data.loc[:,inv+'1':inv+str(p)]
    # 将数据框中大于0的值标记为1，否则标记为0，得到一个0/1矩阵
    # df_value的每一行代表一个样本，每一列代表一个时间段（从最近1个月到最近p个月）
    df_value=np.where(df>0,1,0)
    # 初始化结果列表，用于存储每个样本的计算结果
    auto_value=[]
    # 遍历每一行（每个样本）
    for i in range(len(df_value)):
        # 获取第i行的所有值，row_value是一个一维数组，表示该样本在最近p个月中inv>0的情况
        row_value=df_value[i,:]
        # 判断这一行是否所有值都<=0（即最近p个月中没有任何一个月inv>0）
        if row_value.max()<=0:
            # 如果没有任何一个月inv>0，则返回字符串'0'，表示没有找到
            indexs='0'
            auto_value.append(indexs)
        else:
            # 如果至少有一个月inv>0，则从第一个位置（最近1个月）开始查找
            # indexs初始化为1，表示从第1个月开始计数
            indexs=1
            # 从左到右遍历这一行的每个值（从最近1个月到最近p个月）
            for j in row_value:
                # 如果找到第一个值>0的位置（即最近一次inv>0的月份）
                if j>0:
                    # 跳出循环，此时indexs就是最近一次inv>0到现在的月份数
                    break
                # 如果当前值<=0，则继续查找下一个月份，月份数加1
                indexs+=1
            # 将计算得到的月份数添加到结果列表中
            auto_value.append(indexs)
    # 返回特征名称（格式：inv_msg+p，例如：ft_msg4）和对应的值数组（每个样本最近一次inv>0到现在的月份数）
    return inv+'_msg'+str(p),auto_value
 

#最近p个月，最近一次inv=0到现在的月份数
def Msz(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    df_value=np.where(df==0,1,0)  # 这里已经将inv=0的值标记为1了
    auto_value=[]
    for i in range(len(df_value)):
        row_value=df_value[i,:]
        if row_value.max()<=0:
            indexs='0'
            auto_value.append(indexs)
        else:
            indexs=1
            for j in row_value:
                if j>0:
                    break
                indexs+=1
            auto_value.append(indexs)
    return inv+'_msz'+str(p),auto_value
    
#当月inv/(最近p个月inv的均值)；用客户贷款前夕的情况与之前的平均值进行比较，可以看出来这个人最近有没有什么重大转折
# 做变量的时候，经常会用客户最近的情况与过去的情况做比较，评估客户的稳定性
def Cav(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    # 当月就限定为df[inv+'1']
    auto_value = df[inv+'1']/np.nanmean(df,axis = 1 ) 
    return inv+'_cav'+str(p),auto_value

#当月inv/(最近p个月inv的最小值)
def Cmn(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = df[inv+'1']/np.nanmin(df,axis = 1 ) 
    return inv+'_cmn'+str(p),auto_value 

#最近p个月，每两个月间的inv的增长量的最大值
def Mai(inv,p):
    # 从数据中提取从inv+'1'到inv+str(p)的所有列，并转换为numpy数组
    # arr是一个二维数组，每一行代表一个样本，每一列代表一个时间段（从最近1个月到最近p个月）
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    # 初始化结果列表，用于存储每个样本的计算结果
    auto_value = []
    # 遍历每一行（每个样本）
    for i in range(len(arr)):
        # 获取第i行的所有值，df_value是一个一维数组，表示该样本在最近p个月中的inv值
        # df_value[0]是最近1个月的值，df_value[1]是最近2个月的值，以此类推
        df_value = arr[i,:]
        # 初始化增长量列表，用于存储该样本所有相邻两个月间的增长量
        value_lst = []
        # 遍历相邻的两个月，计算每两个月间的增长量
        # range(len(df_value)-1) 确保可以访问 df_value[k] 和 df_value[k+1]
        for k in range(len(df_value)-1):
            # 计算增长量：较近的月份值减去较远的月份值
            # df_value[k] 是较近的月份（例如：k=0表示最近1个月），df_value[k+1] 是较远的月份（例如：k+1=1表示最近2个月）
            # 如果 minus > 0，表示增长了；如果 minus < 0，表示减少了
            minus = df_value[k] - df_value[k+1]
            # 将计算得到的增长量添加到列表中
            value_lst.append(minus)
        # 找出该样本所有相邻月份增长量中的最大值（使用np.nanmax忽略NaN值）
        # 这个最大值表示该样本在最近p个月中，单次增长的最大幅度
        auto_value.append(np.nanmax(value_lst))     
    # 返回特征名称（格式：inv_mai+p，例如：ft_mai4）和对应的值数组（每个样本相邻月份增长量的最大值）
    return inv+'_mai'+str(p),auto_value

#最近p个月，每两个月间的inv的减少量的最大值
def Mad(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])      
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        for k in range(len(df_value)-1):
            minus = df_value[k+1] - df_value[k]
            value_lst.append(minus)
        auto_value.append(np.nanmax(value_lst))     
    return inv+'_mad'+str(p),auto_value 

#最近p个月，inv的标准差
def Std(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nanvar(df,axis = 1)
    return inv+'_std'+str(p),auto_value 

    
#最近p个月，inv的变异系数
def Cva(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value=np.nanmean(df,axis = 1 )/np.nanvar(df,axis = 1)
    return inv+'_cva'+str(p),auto_value 



#(当月inv) - (最近p个月inv的均值)
def Cmm(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = df[inv+'1'] - np.nanmean(df,axis = 1 ) 
    return inv+'_cmm'+str(p),auto_value 

#(当月inv) - (最近p个月inv的最小值)
def Cnm(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = df[inv+'1'] - np.nanmin(df,axis = 1 ) 
    return inv+'_cnm'+str(p),auto_value 


#(当月inv) - (最近p个月inv的最大值)
def Cxm(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = df[inv+'1'] - np.nanmax(df,axis = 1 ) 
    return inv+'_cxm'+str(p),auto_value 



#（ (当月inv) - (最近p个月inv的最大值) ） / (最近p个月inv的最大值) ）
def Cxp(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    temp = np.nanmin(df,axis = 1 )
    auto_value = (df[inv+'1'] - temp )/ temp
    return inv+'_cxp'+str(p),auto_value 

#最近p个月，inv的极差
def Ran(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = np.nanmax(df,axis = 1 )  -  np.nanmin(df,axis = 1 ) 
    return inv+'_ran'+str(p),auto_value 


#最近min( Time on book，p )个月中，后一个月相比于前一个月增长了的月份数
def Nci(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        for k in range(len(df_value)-1):
            minus = df_value[k] - df_value[k+1]
            value_lst.append(minus)           
        value_ng = np.where(np.array(value_lst)>0,1,0).sum()
        auto_value.append(np.nanmax(value_ng))     
    return inv+'_nci'+str(p),auto_value 
   

#最近min( Time on book，p )个月中，后一个月相比于前一个月减少了的月份数
def Ncd(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        for k in range(len(df_value)-1):
            minus = df_value[k] - df_value[k+1]
            value_lst.append(minus)           
        value_ng = np.where(np.array(value_lst)<0,1,0).sum()
        auto_value.append(np.nanmax(value_ng))     
    return inv+'_ncd'+str(p),auto_value 
           

#最近min( Time on book，p )个月中，相邻月份inv 相等的月份数
def Ncn(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        for k in range(len(df_value)-1):
            minus = df_value[k] - df_value[k+1]
            value_lst.append(minus)           
        value_ng = np.where(np.array(value_lst)==0,1,0).sum()
        auto_value.append(np.nanmax(value_ng))     
    return inv+'_ncn'+str(p),auto_value    
 
#If  最近min( Time on book，p )个月中，对任意月份i ，都有 inv[i] > inv[i+1] ，
#即严格递增，且inv > 0则flag = 1 Else flag = 0
def Bup(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        index = 0
        for k in range(len(df_value)-1):
            if df_value[k] > df_value[k+1]:
                break
            index =+ 1
        if index == p:            
            value= 1    
        else:
            value = 0
        auto_value.append(value)     
    return inv+'_bup'+str(p),auto_value   

#If  最近min( Time on book，p )个月中，对任意月份i ，都有 inv[i] < inv[i+1] ，
#即严格递减，且inv > 0则flag = 1 Else flag = 0
def Pdn(inv,p):
    arr=np.array(data.loc[:,inv+'1':inv+str(p)])     
    auto_value = []
    for i in range(len(arr)):
        df_value = arr[i,:]
        value_lst = []
        index = 0
        for k in range(len(df_value)-1):
            if df_value[k+1] > df_value[k]:
                break
            index =+ 1
        if index == p:            
            value= 1    
        else:
            value = 0
        auto_value.append(value)     
    return inv+'_pdn'+str(p),auto_value            



#最近min( Time on book，p )个月，inv的修建均值
def Trm(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = []
    for i in range(len(df)):
        trm_mean = list(df.loc[i,:])
        trm_mean.remove(np.nanmax(trm_mean))
        trm_mean.remove(np.nanmin(trm_mean))
        temp=np.nanmean(trm_mean) 
        auto_value.append(temp)
    return inv+'_trm'+str(p),auto_value 

#当月inv / 最近p个月的inv中的最大值
def Cmx(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = (df[inv+'1'] - np.nanmax(df,axis = 1 )) /np.nanmax(df,axis = 1 ) 
    return inv+'_cmx'+str(p),auto_value 

#( 当月inv - 最近p个月的inv均值 ) / inv均值
def Cmp(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = (df[inv+'1'] - np.nanmean(df,axis = 1 )) /np.nanmean(df,axis = 1 ) 
    return inv+'_cmp'+str(p),auto_value 


#( 当月inv - 最近p个月的inv最小值 ) /inv最小值 
def Cnp(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    auto_value = (df[inv+'1'] - np.nanmin(df,axis = 1 )) /np.nanmin(df,axis = 1 ) 
    return inv+'_cnp'+str(p),auto_value 


#最近min( Time on book，p )个月取最大值的月份距现在的月份数
def Msx(inv,p):
    df=data.loc[:,inv+'1':inv+str(p)]
    df['_max'] = np.nanmax(df,axis = 1)
    for i in range(1,p+1):
        df[inv+str(i)] = list(df[inv+str(i)] == df['_max'])
    del df['_max']
    df_value = np.where(df==True,1,0)
    auto_value=[]
    for i in range(len(df_value)):
        row_value=df_value[i,:]
        indexs=1
        for j in row_value:
            if j == 1:
                break
            indexs+=1
        auto_value.append(indexs)
    return inv+'_msx'+str(p),auto_value


#最近p个月的均值/((p,2p)个月的inv均值)
def Rpp(inv,p):
    df1=data.loc[:,inv+'1':inv+str(p)]
    value1=np.nanmean(df1,axis = 1 )
    df2=data.loc[:,inv+str(p):inv+str(2*p)]
    value2=np.nanmean(df2,axis = 1 )   
    auto_value = value1/value2
    return inv+'_rpp'+str(p),auto_value    


#最近p个月的均值 - ((p,2p)个月的inv均值)
def Dpp(inv,p):
    df1=data.loc[:,inv+'1':inv+str(p)]
    value1=np.nanmean(df1,axis = 1 )
    df2=data.loc[:,inv+str(p):inv+str(2*p)]
    value2=np.nanmean(df2,axis = 1 )   
    auto_value = value1 - value2
    return inv+'_dpp'+str(p),auto_value   


#(最近p个月的inv最大值)/ (最近(p,2p)个月的inv最大值)
def Mpp(inv,p):
    df1=data.loc[:,inv+'1':inv+str(p)]
    value1=np.nanmax(df1,axis = 1 )
    df2=data.loc[:,inv+str(p):inv+str(2*p)]
    value2=np.nanmax(df2,axis = 1 )   
    auto_value = value1/value2
    return inv+'_mpp'+str(p),auto_value  

  
#(最近p个月的inv最小值)/ (最近(p,2p)个月的inv最小值)
def Npp(inv,p):
    df1=data.loc[:,inv+'1':inv+str(p)]
    value1=np.nanmin(df1,axis = 1 )
    df2=data.loc[:,inv+str(p):inv+str(2*p)]
    value2=np.nanmin(df2,axis = 1 )   
    auto_value = value1/value2
    return inv+'_npp'+str(p),auto_value

#%%
 
#首先执行下面的全部函数 
       
#定义批量调用双参数的函数        
def auto_var2(inv,p):
    #global data_new
    try:
        columns_name,values=Num(inv,p)
        data_new[columns_name]=values
    except:
           print("Num PARSE ERROR",inv,p)
    try:
        columns_name,values=Nmz(inv,p)
        data_new[columns_name]=values
    except:
           print("Nmz PARSE ERROR",inv,p)
    try:
        columns_name,values=Evr(inv,p)
        data_new[columns_name]=values
    except:
           print("Evr PARSE ERROR",inv,p)
    try:
        columns_name,values=Avg(inv,p)
        data_new[columns_name]=values
    except:
           print("Avg PARSE ERROR",inv,p)
    try:
        columns_name,values=Tot(inv,p)
        data_new[columns_name]=values
    except:
        print("Tot PARSE ERROR",inv,p) 
    try:
        columns_name,values=Tot2T(inv,p)
        data_new[columns_name]=values
    except:
        print("Tot2T PARSE ERROR",inv,p)        
    try:
        columns_name,values=Max(inv,p)
        data_new[columns_name]=values
    except:
        print("Tot PARSE ERROR",inv,p)
    try:
        columns_name,values=Max(inv,p)
        data_new[columns_name]=values
    except:
        print("Max PARSE ERROR",inv,p)
    try:
        columns_name,values=Min(inv,p)
        data_new[columns_name]=values
    except:
        print("Min PARSE ERROR",inv,p)
    try:
        columns_name,values=Msg(inv,p)
        data_new[columns_name]=values
    except:
        print("Msg PARSE ERROR",inv,p)
    try:
        columns_name,values=Msz(inv,p)
        data_new[columns_name]=values
    except:
        print("Msz PARSE ERROR",inv,p)
    try:
        columns_name,values=Cav(inv,p)
        data_new[columns_name]=values
    except:
        print("Cav PARSE ERROR",inv,p)
    try:
        columns_name,values=Cmn(inv,p)
        data_new[columns_name]=values
    except:
        print("Cmn PARSE ERROR",inv,p)        
    try:
        columns_name,values=Std(inv,p)
        data_new[columns_name]=values
    except:
        print("Std PARSE ERROR",inv,p)   
    try:
        columns_name,values=Cva(inv,p)
        data_new[columns_name]=values
    except:
        print("Cva PARSE ERROR",inv,p)   
    try:
        columns_name,values=Cmm(inv,p)
        data_new[columns_name]=values
    except:
        print("Cmm PARSE ERROR",inv,p)  
    try:
        columns_name,values=Cnm(inv,p)
        data_new[columns_name]=values
    except:
        print("Cnm PARSE ERROR",inv,p)         
    try:
        columns_name,values=Cxm(inv,p)
        data_new[columns_name]=values
    except:
        print("Cxm PARSE ERROR",inv,p)          
    try:
        columns_name,values=Cxp(inv,p)
        data_new[columns_name]=values
    except:
        print("Cxp PARSE ERROR",inv,p)
    try:
        columns_name,values=Ran(inv,p)
        data_new[columns_name]=values
    except:
        print("Ran PARSE ERROR",inv,p)
    try:
        columns_name,values=Nci(inv,p)
        data_new[columns_name]=values
    except:
        print("Nci PARSE ERROR",inv,p)
    try:
        columns_name,values=Ncd(inv,p)
        data_new[columns_name]=values
    except:
        print("Ncd PARSE ERROR",inv,p)
    try:
        columns_name,values=Ncn(inv,p)
        data_new[columns_name]=values
    except:
        print("Ncn PARSE ERROR",inv,p)
    try:
        columns_name,values=Pdn(inv,p)
        data_new[columns_name]=values
    except:
        print("Pdn PARSE ERROR",inv,p) 
    try:
        columns_name,values=Cmx(inv,p)
        data_new[columns_name]=values
    except:
        print("Cmx PARSE ERROR",inv,p)         
    try:
        columns_name,values=Cmp(inv,p)
        data_new[columns_name]=values
    except:
        print("Cmp PARSE ERROR",inv,p)   
    try:
        columns_name,values=Cnp(inv,p)
        data_new[columns_name]=values
    except:
        print("Cnp PARSE ERROR",inv,p) 
    try:
        columns_name,values=Msx(inv,p)
        data_new[columns_name]=values
    except:
        print("Msx PARSE ERROR",inv,p)
    try:
        columns_name,values=Nci(inv,p)
        data_new[columns_name]=values
    except:
        print("Nci PARSE ERROR",inv,p)
    try:
        columns_name,values=Trm(inv,p)
        data_new[columns_name]=values
    except:
        print("Trm PARSE ERROR",inv,p)
    try:
        columns_name,values=Bup(inv,p)
        data_new[columns_name]=values
    except:
        print("Bup PARSE ERROR",inv,p)
    try:
        columns_name,values=Mai(inv,p)
        data_new[columns_name]=values
    except:
        print("Mai PARSE ERROR",inv,p)
    try:
        columns_name,values=Mad(inv,p)
        data_new[columns_name]=values
    except:
        print("Mad PARSE ERROR",inv,p)
    try:
        columns_name,values=Rpp(inv,p)
        data_new[columns_name]=values
    except:
        print("Rpp PARSE ERROR",inv,p)
    try:
        columns_name,values=Dpp(inv,p)
        data_new[columns_name]=values
    except:
        print("Dpp PARSE ERROR",inv,p)
    try:
        columns_name,values=Mpp(inv,p)
        data_new[columns_name]=values
    except:
        print("Mpp PARSE ERROR",inv,p)
    try:
        columns_name,values=Npp(inv,p)
        data_new[columns_name]=values
    except:
        print("Npp PARSE ERROR",inv,p)
    return data_new.columns.size

#%%
data_new = data.copy()
p = 4
inv = 'ft'
auto_data = pd.DataFrame()
for p in range(1,12):
    for inv in ['ft','gt']:
        auto_var2(inv,p)  # inv代表ft/gt变量，p代表变量后缀1～12，对特征进行每一列的进行特征组合
# %%
