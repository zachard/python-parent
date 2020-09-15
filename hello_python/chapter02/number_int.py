# 在Python中可对整数执行 + , - , * , /
total = 3 + 2
print('3 + 2 = ' + str(total))
sub = 5 - 4
print('5 - 4 = ' + str(sub))
multiply = 5 * 4
print('5 * 4 = ' + str(multiply))
divide = 20 / 5
print('20 / 5 = ' + str(divide))

# 在Python中, 用两个乘号 ** 表示乘方运算  
# 10 ** 6 = 1000000
power = 10 ** 6
print('10 ** 6 = ' + str(power))

# 通过括号可以改变运算顺序
expression = 3 + 2 * 4
print('3 + 2 * 4 = ' + str(expression))
bracket_expression = (3 + 2) * 4
print('(3 + 2) * 4 = ' + str(bracket_expression))

# 注: Python2中 3 / 2 会得到 1, (Python2直接将小数部分删除) 
# 要保留小数部分需要将其中一个数保留为浮点数 3.0 / 2 -> 1.5