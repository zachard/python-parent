from django.db import models

# 每当需要修改项目的数据时, 都采取如下三个步骤: 
# 修改models.py; 对model.py的文件夹调用makemigrations; 示例: python manage.py makemigrations <dir>
# 让Django迁移项目. 示例: python manage.py migrate

# Create your models here.
class Topic(models.Model):   # 创建一个Topic继承了Django中的Model(基础模型类)
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # 定义一个可存储200个字符的字符串类型属性
    date_added = models.DateTimeField(auto_now_add=True)  # 定义了一个时间类型的属性

    def __str__(self):   # 定义了模型类调用str()方法应该返回的值, 类似于Java中的toString()方法
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):  # 继承Django的Model类, 表示创建一个自定义的类型
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键引用到相应的其他类型, 使两个数据之间产生关联, 必需加上on_delete属性
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:   # 嵌套了Meta类. Meta存储用于管理模型的额外信息
        verbose_name_plural = 'entries'  # 表示在需要时使用Entries来表示多个条目

    def __str__(self): 
        """返回模型的字符串表示"""
        return self.text[:50] + '...'