class AnonymousSurvey():
    """匿名搜集答案的问卷"""

    def __init__(self, question):   # 初始化问卷
        self.question = question   #  初始化问卷答案
        self.responses = []

    def show_question(self):
        """显示问卷问题"""
        print(self.question)
    
    def store_response(self, new_response):
        """存储问卷答案"""
        self.responses.append(new_response)  # 将新的问卷调查答案添加到列表中
    
    def show_result(self):
        """显示问卷调查结果"""
        print('问卷结果为: ')
        for response in self.responses:
            print('- ' + response)