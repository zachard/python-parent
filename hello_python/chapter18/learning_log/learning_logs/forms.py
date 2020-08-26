from django import forms   # 从django模块导入表单
from .models import Topic, Entry   # 从自己的模块中导入自定义类Topic

class TopicForm(forms.ModelForm):  # 定义一个继承了forms.ModelForm的表单类
    class Meta:       # 内嵌类, 表示当前类型的属性
        model = Topic      # 表示当前表单类根据Topic类创建表单
        fields = ['text']  # 表示根据Topic表单创建的只包含text字段
        labels = {'text': ''}   # 表示不要为text字段生成标签

# class EntryForm(forms.ModelForm):  # 创建新条目的表单
#     class Meta:
#         model = Entry     # 根据Entry类来创建当前表单类
#         fields = ['text']   # 根据Entry创建的表单只包含text字段
#         labels = {'text': ''}   # 表示不要为text字段生成标签
#         # 我们定义了属性widgets. 小部件(widget)是一个HTML表单元素, 
#         # 如单行文本框、多行文本区域或下拉列表. 
#         # 通过设置属性widgets, 可覆盖Django选择的默认小部件. 
#         # 通过让Django使用forms.Textarea, 
#         # 我们定制了字段'text'的输入小部件, 将文本区域的宽度设置为80列, 
#         # 而不是默认的40列
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}