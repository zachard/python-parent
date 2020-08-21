# 定义了函数的模块

def make_pizza(size, *toppings): 
    """概述要制作的比萨"""
    print('\n制作一个' + str(size) + 
        '英尺的披萨, 包含以下配料: ')
    
    for topping in toppings: 
        print('-' + topping)