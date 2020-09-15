# 单元测试和测试用例  
import unittest    # 导入单元测试需要的模块
from names_function import get_format_name    # 导入被测试的方法
from names_function import get_format_name_with_middle
from names_function import get_format_name_with_option_middle

class NamesTestCase(unittest.TestCase):    # 创建一个用于包含针对方法的单元测试的测试类
    """names_function的测试类"""

    def test_first_last_name(self): 
        """测试姓名的拼接"""
        format_name = get_format_name('janis', 'joplin')
        self.assertEqual(format_name, 'Janis Joplin')  # 断言方法, 判断是否和期望结果一致
    
    def test_first_middle_last_name(self): 
        """测试含中间名的姓名拼接"""
        # format_name = get_format_name_with_middle('janis', 'joplin')  # 测试会报错误, 因为函数调用缺少了必要参数
        # self.assertEqual(format_name, 'Janis Joplin')
    
    # 添加新的测试用例, 新增一个test_开头的测试方法
    def test_first_last_option_middle_name(self):
        """测试可选中间名的姓名拼接"""
        full_name_no_middle = get_format_name_with_option_middle('janis', 'joplin')
        self.assertEqual(full_name_no_middle, 'Janis Joplin')

        full_name_with_middle = get_format_name_with_option_middle('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(full_name_with_middle, 'Wolfgang Mozart Amadeus')  # 注意这里的测试结果

unittest.main()   # 运行时, 所有以test_开头的方法都会运行

# 测试未通过怎么办
# 测试未通过时, 不要修改测试, 而应修复导致测试不能通过的代码