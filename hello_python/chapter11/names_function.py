
def get_format_name(first, last): 
    """返回姓名的全名并首字母大写"""
    full_name = first + ' ' + last
    return full_name.title()

def get_format_name_with_middle(first, middle, last): 
    """返回姓名的全名并首字母大写, 包含中间名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

def get_format_name_with_option_middle(first, last, middle = ''):
    """返回可选的中间名姓名"""
    if middle: 
        full_name = first + ' ' + middle + ' ' + last
    else: 
        full_name = first + ' ' + last
    
    return full_name.title()