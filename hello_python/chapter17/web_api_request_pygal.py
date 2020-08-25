# 使用request模块来请求数据
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 被请求的api
r = requests.get(url)   # 通过get方法请求api
print('状态码: ', r.status_code)  # 这个status_code不是api响应实体中的一个key, 而是python封装对象中的一个属性

response_dict = r.json()   # 将API的响应信息存储到变量中, 方法json()将这些信息转换为一个Python字典

# 处理返回的json仓库信息
print('GitHub中总的Python数为: ', response_dict['total_count'])  # 类似于从字典中取对应的键值

repo_dicts = response_dict['items']
print('当前返回的仓库总数为: ', len(response_dict))

# names, stars = [], []   # 创建两个列表, 分别存储项目的名称和星标
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    if repo_dict['description']:     # 仓库中会碰见description为空的情况, 所以这里需要对空进行特殊处理
        desc = repo_dict['description']
    else:
        desc = ''
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': desc,     # label标签表示自定义柱状图中的工具提示
        'xlink': repo_dict['html_url'],  # 在图表中添加柱状图可点击的链接, 这里也应该做一个是否为空的判断
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)   # 定义一种绘图的基色
# style指定绘图的基色, x_label_rotation指定x坐标轴标签旋转度数, show_legend决定是否显示图例
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

# 将图表的所有配置集中到config类
my_config = pygal.Config()   # 定义config对象, 用于保存图表的修改
my_config.x_label_rotation = 45  # x轴的标签旋转45度
my_config.show_legend = False   # 不显示图例

# 在这个图表中, 副标签是x轴上的项目名以及y轴上的大部分数字. 
# 主标签是y轴上为5000整数倍的刻度; 这些标签应更大, 以与副标签区分开来
my_config.title_font_size = 24  # 图表的标题为24号字体
my_config.label_font_size = 14  # 图表的副标题为14号字体, 副标题? 不是标签?
my_config.major_label_font_size = 18  # 图表主标签为18号字体

my_config.truncate_label = 15   # 将较长的项目名缩短为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000    # 自定义图表的宽度, 让图表更充分的利用浏览器空间

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'GitHub上最多星标的Python项目'
chart.x_labels = names

# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')