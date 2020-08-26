from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic   # 从模块中导入Topic类型
from .forms import TopicForm  # 模型的类放在models模块, 表单的类放在forms模块

# Create your views here.

def index(request):   # 定义请求需要跳转到的网页
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):   # 定义/topics请求路径跳转的网页
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# 用户初次请求该网页时, 其浏览器将发送GET请求; 
# 用户填写并提交表单时, 其浏览器将发送POST请求. 
# 根据请求的类型, 我们可以确定用户请求的是空表单(GET请求)
# 还是要求对填写好的表单进行处理(POST请求)
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()  # 如果不是POST请求, 表示首次请求, 返回空表单
    else:
        # POST提交了数据, 对数据进行处理
        form = TopicForm(request.POST)  # 根据请求传入的数据创建一个表单对象
        # is_valid()函数核实用户填写了所有必不可少的字段(表单字段默认都是必不可少的), 
        # 且输入的数据与要求的字段类型一致
        if form.is_valid():   # 检查表单的信息是否合法有效
            form.save()   # 将数据保存至数据库
            # reverse()获取页面对应的URL, HttpResponseRedirect用于将浏览器页面重定向到topic
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}   # 传入到父类模板中显示, html中包含context字段
    return render(request, 'learning_logs/new_topic.html', context)

# def new_entry(request, topic_id):
#     """在特定主题中添加新条目"""
#     topic = Topic.objects.get(id=topic_id)  # 根据topic_id获取一个Topic对象

#     if request.method != 'POST':
#         # 首次请求, 不为POST, 创建一个表单
#         form = EntryForm()
#     else:
#         # POST请求方式提交数据, 对数据进行处理
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.topic = topic   # 设置条目的topic属性
#             new_entry.save()
#             return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
        
#     context = {'topic': topic, 'form': form}
#     return render(request, 'learning_logs/new_entry.html', context)