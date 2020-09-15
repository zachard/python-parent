# 如果你要编写的类是另一个现成类的特殊版本, 可使用继承. 
# 一个类继承另一个类时, 它将自动获得另一个类的所有属性和方法; 
# 原有的类称为父类, 而新类称为子类. 
# 子类继承了其父类的所有属性和方法, 同时还可以定义自己的属性和方法  
# 创建子类时, 父类必须包含在当前文件中, 且位于子类前面. 

# from clazz_instance_use import Car   # 也可以直接从其他模块中import父类

# 定义一个表示车的类
class Car():
    """模拟汽车的类"""

    # 类中的每个属性都必须有初始值, 哪怕这个值是0或空字符串. 
    # 在有些情况下, 如设置默认值时, 在方法__init__()内指定这种初始值是可行的;
    # 如果你对某个属性这样做了, 就无需包含为它提供初始值的形参. 
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make    # 制造商
        self.model = model  # 型号
        self.year = year    # 年份
        self.odometer_reading = 0   # 属性在__int__方法中设置了初始值, 无需再传入形参
        self.gas = 100
    
    def get_descriptive_name(self):
        """返回车的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印这辆汽车形式的里程数"""
        print('这辆车已经行驶了' + str(self.odometer_reading) + '英里.')
    
    def update_odometer(self, mileage):   # 相当于Java中的setter方法
        """设置车行驶的里程数"""
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print('里程数不允许减少!')
    
    def increment_odometer(self, miles): 
        """增加汽车的里程数"""
        if miles < 0: 
            print('不允许增加负数里程!')
        else: 
            self.odometer_reading += miles
    
    def fill_gas_tank(self, gas): 
        if gas < 0: 
            print('邮箱中的油不可以是负数.')
        else: 
            self.gas = gas

class Battery():
    """描述电动车电瓶信息"""

    def __init__(self, battery_size=70):
        """初始化电瓶信息"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印当前电瓶信息"""
        print('当前电瓶容量为: ' + str(self.battery_size) + 'KWh.')
        return self.battery_size
    
    def get_range(self): 
        """打印电池可行驶的里程信息"""
        if self.battery_size == 70: 
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        print('当前电池容量可行驶' + str(range) + '英里.')

class ElectricCar(Car): 
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)   # 通过spuer()方法调用父类的__init__方法来初始化父类中的属性, super关键字与Java中类似
        self.battery_size = 70  # 子类特有属性
        self.battery = Battery()  # 实例作为属性, 难道形参我不能传一个对象实例进去吗?
    
    def describe_battery(self):  # 子类特有的行为
        print('这辆车有一个' + str(self.battery.describe_battery()) + 'KWh的电池.')
    
    def fill_gas_tank(self): 
        print('电动汽车没有邮箱.')

print('\n')
my_tesla = ElectricCar('tesla', 'model s', 2016)  # 初始化一个子类实例
print(my_tesla.get_descriptive_name())   # 通过子类实例调用父类中定义的方法
print('我的特斯拉电池容量为: ' + str(my_tesla.battery_size))  # 子类实例直接访问子类特有属性
my_tesla.describe_battery()  # 子类实例访问子类特有的行为

my_general_car = Car('奥迪', 'A8', 2018)  # 创建一个父类实例
# my_general_car.battery_size   # 父类实例访问子类特有的实例, 程序会出现异常
# my_general_car.describe_battery()  # 父类实例调用子类特有的方法, 程序会出现异常

# 重写父类方法
# 对于父类的方法, 只要它不符合子类模拟的实物的行为, 都可对其进行重写. 
# 可在子类中定义一个这样的方法, 即它与要重写的父类方法同名. 
# 这样, Python将不会考虑这个父类方法, 而只关注你在子类中定义的相应方法. 

# 父类中存在fill_gas_tank方法, 在子类中进行重写, 注意: 父类和子类中fill_gas_tank形参不一致
my_tesla.fill_gas_tank()   # 子类实例调用子类的方法, 不会有问题
# my_tesla.fill_gas_tank(100)  # 调用异常, 子类实例不能调用到父类的方法, 被子类同名方法覆盖

print('\n')
my_general_car.fill_gas_tank(50)  # 父类实例可以调用父类中定义的方法
print('我的油耗车的邮箱有' + str(my_general_car.gas) + '升油.')
# my_general_car.fill_gas_tank() # 调用异常, 父类实例不能调用子类实例中重写的方法

# 将实例作为属性
print('\n')
my_tesla.describe_battery()
my_tesla.battery.get_range()