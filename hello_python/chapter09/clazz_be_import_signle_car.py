# 定义一个表示车的类
# 这个类将被导入--导入单个类, 被导入的类

"""一个表示汽车的类"""  # 模块及文档字符串

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