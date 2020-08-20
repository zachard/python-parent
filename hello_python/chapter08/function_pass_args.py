# 向函数传递实参的方式很多, 
# 可使用位置实参, 这要求实参的顺序与形参的顺序相同;
# 也可使用关键字实参, 其中每个实参都由变量名和值组成;
# 还可使用列表和字典

# 位置实参
# 调用函数时, Python必须将函数调用中的每个实参都关联到函数定义中的一个形参. 
# 为此, 最简单的关联方式是基于实参的顺序
def describe_pet(animal_type, pet_name):  # 定义一个函数, 传两个参数, 第一个为宠物类型, 第二个为宠物名字
    """显示宠物信息"""
    print('\n我有一个宠物' + animal_type + '.')
    print('我的宠物' + animal_type + '名字叫做' + pet_name + '.')

describe_pet('仓鼠', '大白') # 位置实参的顺序很重要
describe_pet('狗', '灭霸')

# 关键字实参
# 关键字实参是传递给函数的名称—值对. 
# 你直接在实参中将名称和值关联起来了, 因此向函数传递实参时不会混淆. 
# 关键字实参让你无需考虑函数调用中的实参顺序, 还清楚地指出了函数调用中各个值的用途

describe_pet(animal_type='鸭', pet_name='唐老鸭')  # 关键字实参顺序无所谓
describe_pet(pet_name='汤姆', animal_type='猫')

# 默认值
# 编写函数时, 可给每个形参指定默认值. 
# 在调用函数中给形参提供了实参时, Python将使用指定的实参值; 
# 否则, 将使用形参的默认值. 因此, 给形参指定默认值后, 可在函数调用中省略相应的实参. 
# 使用默认值可简化函数调用, 还可清楚地指出函数的典型用法. 
def describe_pet_default_dog(pet_name, animal_type = '狗'):  # 定义一个形参带默认值的函数
    """显示宠物信息"""
    print('\n我有一个宠物' + animal_type + '.')
    print('我的宠物' + animal_type + '名字叫做' + pet_name + '.')

describe_pet_default_dog(pet_name='八公')  # 没指定animal_type, 传入默认值
describe_pet_default_dog(animal_type='鹅', pet_name='飞天鹅') # 形参指定了animal_type, 使用形参的默认值

# 使用默认值时, 在形参列表中必须先列出没有默认值的形参, 再列出有默认值的实参. 
# 这让Python依然能够正确地解读位置实参
# def describe_pet_default_dog(animal_type = '狗', pet_name):  # 所以这个函数的定义会运行异常

# 避免实参错误
# describe_pet()  # 这个函数调用将会出现异常, 因为缺少函数运行所必需的参数