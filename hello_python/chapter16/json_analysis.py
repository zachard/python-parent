# 处理json数据
import json   # 导入json模块, 系统自带的模块
from pygal_maps_world.i18n import COUNTRIES  # 导入pygal_maps_world中的国家代码列表, 目前没有pygal.i18n的模块了
import pygal_maps_world.maps as pywm  # 导入绘制世界地图的模块
from pygal.style import RotateStyle, LightColorizedStyle

def get_country_code(country_name): 
    """根据国家名称找出对应国家代码的函数"""
    for code, name in COUNTRIES.items():   # COUNTRIES的存在格式是字典数据格式
        if name == contry_name:
            return code
        
    return None    # 注意这个return的位置, 不能是跟if同层级

filename = 'population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)   # json模块直接加载文件内容, 将数据转换为Python能够处理的格式

# for country_code in sorted(COUNTRIES.keys()):     # 测试一下打印国家列表
#     print(country_code, COUNTRIES[country_code])

cc_population = {}   # 创建一个包含人口数量的字典
for pop_dict in pop_data:  # 因为json文件的内容是数组格式存在的, 所以可以进行遍历
    if pop_dict['Year'] == '2010':
        contry_name = pop_dict['Country Name']   # 像字典取值一样, 可以直接通过键值取出对应的值, 且值全部为字符串
        population = int(float(pop_dict['Value']))   # 先将字符串转换为浮点数, 再用int去除小数部分
        code = get_country_code(contry_name)      # 根据国家名称获取国家的代码

        if code:
            # print(code + ': ' + str(population))
            cc_population[code] = population   # 将国家代码及人口放入相应的字典之中
        # else:
        #     print('ERROR: ' + str(population))

# 按人口总数对国家进行分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else: 
        cc_pops_3[cc] = pop

print('人口小于10000000国家个数为: ', len(cc_pops_1))
print('人口大于等于10000000小于1000000000国家个数为: ', len(cc_pops_2))
print('人口大于等于1000000000国家个数为: ', len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)   # 为世界地图指定一种基色
wm = pywm.World(style=wm_style)    # 创建世界地图
# wm.title = '北美、中美和南美'    # 给图表设置属性

# wm.add('北美', ['ca', 'mx', 'us'])   # 添加需要突出显示的国家和国别码
# wm.add('北美', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})  # 不仅显示地区, 还显示地方对应的人口, 传递字典类型参数而非列表
# wm.add('中美', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('南美', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.title = '2010年世界人口地图'
# wm.add('2010', cc_population)   # 直接将一个字典传入到图形中

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1nb', cc_pops_3)

# wm.render_to_file('americas.svg')  # 将图形输出到文件
wm.render_to_file('world_population.svg')