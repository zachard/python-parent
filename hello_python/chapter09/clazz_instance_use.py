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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值-直接修改属性的值
# 要修改属性的值, 最简单的方式是通过实例直接访问它. 
my_new_car.odometer_reading = 60   # 从提车开回家, 开了60英里
my_new_car.read_odometer()

# 修改属性的值-通过方法修改属性
# 如果有替你更新属性的方法, 将大有裨益. 
# 这样, 你就无需直接访问属性, 而可将值传递给一个方法, 由它在内部进行更新
my_new_car.update_odometer(23)  # 先把里程数调小试试
my_new_car.read_odometer()
my_new_car.update_odometer(100)  # 通过调用方法修改属性值
my_new_car.read_odometer()

# 修改属性的值-通过方法对属性的值进行递增
print('\n')
my_used_car = Car('subaru', 'outback', 2013)
my_used_car.get_descriptive_name()

my_used_car.update_odometer(23500)  # 更新我已经用过的车的里程数
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)  # 增加负数里程
my_used_car.read_odometer()

my_used_car.increment_odometer(100)  # 增加有意义的里程
my_used_car.read_odometer()

# 可以看出, 相对于直接修改实例属性, 通过方法修改属性更好,
# 因为可以添加逻辑判断过滤掉非法传入的值