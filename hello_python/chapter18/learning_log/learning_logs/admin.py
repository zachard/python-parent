from django.contrib import admin

from learning_logs.models import Topic, Entry  # 导入创建的模型类

# Register your models here.

admin.site.register(Topic)   # 让Django通过管理网站注册自定义创建的模型
admin.site.register(Entry)