
# 导入单个类--在被导入模块中只包含了需要导入的类
from clazz_be_import_signle_car import Car

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
my_car.read_odometer()   # 使用方法与不导入是一致的

# 导入一个类--在被导入模块中包含了多个类
from clazz_be_import_multi_car import ElectricCar

print('\n')
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())   # 方法的使用与不导入情形是一致的
my_tesla.describe_battery()
my_tesla.battery.get_range()

# 从一个模块中导入多个类
# 从一个模块中导入多个类时, 用逗号分隔了各个类. 
from clazz_be_import_multi_car import Car, ElectricCar

# 导入整个模块
# 可以导入整个模块, 再使用句点表示法访问需要的类. 
# 这种导入方法很简单, 代码也易于阅读. 
# 由于创建类实例的代码都包含模块名, 因此不会与当前文件使用的任何名称发生冲突
# 使用语法module_name.class_name访问需要的类
import clazz_be_import_multi_car as car

my_beetle = car.Car('volkswagen', 'beetle', 2016)  # 模块名.类名 的访问方式
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 导入模块中所有的类
# 语法: from module_name import *
# 不推荐使用这种导入方式, 其原因有二: 
# 首先, 如果只要看一下文件开头的import语句, 就能清楚地知道程序使用了哪些类, 将大有裨益;
# 但这种导入方式没有明确地指出你使用了模块 的哪些类. 
# 其次这种导入方式还可能引发名称方面的困惑. 如果你不小心导入了一个与程序文件中其他东西同名的类, 
# 将引发难以诊断的错误. 

# 需要从一个模块中导入很多类时, 最好导入整个模块, 并使用module_name.class_name语法来访问类
# 这样做时, 虽然文件开头并没有列出用到的所有类, 
# 但你清楚地知道在程序的哪些地方使用了导入的模块; 你还避免了导入模块中的每个类可能引发的名称冲突. 
from clazz_be_import_multi_car import *