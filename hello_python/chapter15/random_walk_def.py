"""定义随机漫步的类"""

from random import choice   # choice函数用于返回一个列表, 元组或字符串的随机项

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points

        # 所有的随机漫步都始于(0,0)
        self.x_values = [0]   # 注: 这里的x和y是列表
        self.y_values = [0]
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步, 知道到达指定长度
        while len(self.x_values) < self.num_points:
            
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 表示从[-1, 1]列表中随机返回一个数, 1/-1, 决定了随机漫步的方向
            x_distance = choice([0, 1, 2, 3, 4])  # 表示从[0, 1, 2, 3, 4]列表中随机返回一个数, 0/1/2/3/4, 决定了随机漫步的距离
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # 不允许原地踏步.
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点随机漫步的x值和y值.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)