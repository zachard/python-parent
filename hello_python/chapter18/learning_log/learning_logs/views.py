from django.shortcuts import render
from .models import Topic   # 从模块中导入Topic类型

# Create your views here.

def index(request):   # 定义请求需要跳转到的网页
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):   # 定义/topics请求路径跳转的网页
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)