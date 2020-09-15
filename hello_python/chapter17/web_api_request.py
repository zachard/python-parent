# 使用request模块来请求数据
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 被请求的api
r = requests.get(url)   # 通过get方法请求api
print('状态码: ', r.status_code)  # 这个status_code不是api响应实体中的一个key, 而是python封装对象中的一个属性

response_dict = r.json()   # 将API的响应信息存储到变量中, 方法json()将这些信息转换为一个Python字典
# print(response_dict.keys())   # 这个keys()方法只返回了第一级数据的键值dict_keys(['total_count', 'incomplete_results', 'items'])

# 处理返回的json仓库信息
print('GitHub中总的Python数为: ', response_dict['total_count'])  # 类似于从字典中取对应的键值

repo_dicts = response_dict['items']
print('当前返回的仓库总数为: ', len(response_dict))

repo_dict_0 = repo_dicts[0]  # 获取返回的仓库中的第一个仓库
print('\n第一个仓库中包含的key值个数为: ', len(repo_dict_0))
# for key, value in repo_dict_0:
#     print(key, value)
# for key in sorted(repo_dict_0.keys()):
#     print(key)

# print('\n打印一些关键的key: ')
# print('名称:', repo_dict_0['name'])
# print('项目负责人:', repo_dict_0['owner']['login'])
# print('星标数:', repo_dict_0['stargazers_count'])
# print('仓库地址:', repo_dict_0['html_url'])
# print('创建人:', repo_dict_0['created_at'])
# print('更新人:', repo_dict_0['updated_at'])
# print('描述:', repo_dict_0['description'])

print('\n打印多个仓库的关键字key: ')
for repo_dict in repo_dicts: 
    print('\n名称:', repo_dict_0['name'])
    print('项目负责人:', repo_dict_0['owner']['login'])
    print('星标数:', repo_dict_0['stargazers_count'])
    print('仓库地址:', repo_dict_0['html_url'])
    print('创建人:', repo_dict_0['created_at'])
    print('更新人:', repo_dict_0['updated_at'])
    print('描述:', repo_dict_0['description'])