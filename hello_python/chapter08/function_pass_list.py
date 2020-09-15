# 将列表传递给函数后, 函数就能直接访问其内容.

# 简单的传递示例
def greet_user(names):
    """向用户列表中每位用户发出问候"""
    for name in names:
        print('Hello, ' + name.title() + '!')

usernames = ['amy', 'bob', 'cindy']
greet_user(usernames)

# 在函数中修改列表
print('\n')
def print_models(unprinted_designs, completed_models):  # 打印设计函数
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()  # 选择需要打印的设计
        print('正在打印模型: ' + current_design)
        completed_models.append(current_design)   # 将打印完成的设计放到完成列表中

def show_completed_models(completed_models): 
    """显示打印好的所有模型"""
    print('\n以下模型已经被打印: ')
    for completed_model in completed_models:
        print('\t' + completed_model)

# print_models函数的另外一种写法(单返回值)
def print_models_other(unprinted_designs): 
    completed_models = []

    while unprinted_designs:
        current_design = unprinted_designs.pop()  # 选择需要打印的设计
        print('正在打印模型: ' + current_design)
        completed_models.append(current_design)   # 将打印完成的设计放到完成列表中
    
    return completed_models   # 返回已经打印的列表

# 开始调用函数
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']  # 准备实参-未打印列表
completed_models = [] # 准备实参-已打印列表
print('开始打印之前, 还未打印的列表为: ')
print(unprinted_designs)
print('开始打印之前, 已打印的列表为: ')
print(completed_models)

print_models(unprinted_designs=unprinted_designs, completed_models=completed_models)
# completed_models = print_models_other(unprinted_designs)   # 另外一个函数的调用方式
show_completed_models(completed_models=completed_models)

print('打印完成之后, 还未打印的列表为: ')  # 可以看到, 经过函数之后, 实参已经发生了改变
print(unprinted_designs)
print('打印完成之后, 已打印的列表为: ')
print(completed_models)

# 每个函数都应只负责一项具体的工作

# 禁止函数修改列表
# 可向函数传递列表的副本而不是原件; 这样函数所做的任何修改都只影响副本, 而丝毫不影响原件. 
# 可以通过向函数中传入列表的切片来实现function_name(list_name[:])
print('\n')
print('通过向函数传入切片实现不改变列表内容.')
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']  # 准备实参-未打印列表
completed_models = [] # 准备实参-已打印列表
print('开始打印之前, 还未打印的列表为: ')
print(unprinted_designs)
print('开始打印之前, 已打印的列表为: ')
print(completed_models)

# 传入函数切片
print_models(unprinted_designs=unprinted_designs[:], completed_models=completed_models)
show_completed_models(completed_models=completed_models)

print('打印完成之后, 还未打印的列表为: ')  # 可以看到, 经过函数之后, 原列表并未被修改
print(unprinted_designs)
print('打印完成之后, 已打印的列表为: ')
print(completed_models)

# 除非有充分的理由需要传递副本, 否则还是应该将原始列表传递给函数, 
# 因为让函数使用现成列表可避免花时间和内存创建副本, 从而提高效率, 在处理大型列表时尤其如此