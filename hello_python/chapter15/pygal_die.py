"""骰子类"""

from random import randint

class Die():

    def __init__(self, num_sizes=6):
        """骰子默认有6面"""
        self.num_sizes = num_sizes

    def roll(self):
        """模拟投骰子的操作"""
        return randint(1, self.num_sizes)  # 返回1-num_sizes之间的随机数