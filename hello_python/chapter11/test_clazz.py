
# 各种断言方法
# 只能在继承unittest.TestCase的类中使用这些方法
# assertEqual(a, b)         核实a == b
# assertNotEqual(a, b)      核实a != b 
# assertTrue(x)             核实x为True 
# assertFalse(x)            核实x为False 
# assertIn(item, list)      核实item在list中 
# assertNotIn(item, list)   核实item不在list中

# 运行测试用例时, 每完成一个单元测试, Python都打印一个字符: 
# 测试通过时打印一个句点; 测试引发错误时打印一个E; 测试导致断言失败时打印一个F

import unittest
from survey_clazz import AnonymousSurvey

class AnonymousSurveyTestCase(unittest.TestCase):
    """匿名调查问卷的测试类"""

    # 方法setUp()让测试方法编写起来更容易: 
    # 可在setUp()方法中创建一系列实例并设置它们的属性, 再在测试方法中直接使用这些实例. 
    # 相比于在每个测试方法中都创建实例并设置其属性, 这要容易得多
    def setUp(self):   # setUp方法在每个test_执行之前都会执行一遍
        """在所有test_之前执行, 初始化一些测试所需的东西"""
        print('初始化方法setUp执行了.\n')

    def test_store_single_response(self):
        """测试添加的问卷的单个答案储存"""
        question = '您说哪种语言? '
        survey = AnonymousSurvey(question)    # 创建一个问卷
        survey.store_response('中文')         # 将答案储存到问卷之中

        self.assertIn('中文', survey.responses)   # 断言新增加的答案是否已经储存在答案列表中

    def test_store_three_response(self): 
        """测试问卷储存三个答案是否可行"""
        question = '您说哪种语言? '
        three_answer_survey = AnonymousSurvey(question)  # 构建一个问卷

        responses = ['中文', '英语', '西班牙语']   # 问卷答案列表
        for response in responses:    # 将问卷答案分别存储到问卷答案列表中
            three_answer_survey.store_response(response)
        
        # self.assertIn('中文', three_answer_survey.responses)   # 断言判断答案列表是否包含相应的答案
        # self.assertIn('韩语', three_answer_survey.responses)   # 这个断言会失败

        for response in responses:  # 循环遍历答案是否添加到了答案列表之中
            self.assertIn(response, three_answer_survey.responses)

unittest.main()