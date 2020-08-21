# 这个类将被导入--一个模块(文件)包含多个类的情况

"""一组用于表示燃油汽车和电动汽车的类"""  # 模块及文档字符串

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