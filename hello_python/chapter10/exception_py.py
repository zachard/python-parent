# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误. 
# 每当发生让Python不知所措的错误时, 它都会创建一个异常对象. 
# 如果你编写了处理该异常的代码, 程序将继续运行; 
# 如果你未对异常进行处理, 程序将停止, 并显示一个traceback, 其中包含有关异常的报告. 

# 处理ZeroDivisionError异常
try: 
    print(5 / 0) 
except ZeroDivisionError: 
    print('除数不能为零.')

# else代码块
# try-except后包含else代码块, 依赖于try代码块成功执行的代码都应放到else代码块中
print('\n')
print('请输入两个数, 我们将对它们进行除法操作: ')
print("输入'q'退出. ")

while True:
    first_number = input('\n请输入第一个数: ')
    
    if first_number == 'q':
        break

    second_number = input('请输入第二个数: ')

    if second_number == 'q': 
        break

    try:   # 包含可能会发生错误的程序代码
        answer = int(first_number) / int (second_number) 
    except ZeroDivisionError:   # 捕捉有可能出现的程序异常
        print('第二个数(除数)不能为0.')
    else:   # 如果程序没有发生异常, 则else包含所有正常执行的代码
        print(first_number + ' / ' + second_number + ' = ' + str(answer))

# 处理FileNotFoundError异常
print('\n')
filename = 'alice.txt'

try: 
    with open(filename) as file_content:   # 这个as之后的变量名并非固定为file_object
        contents = file_content.read()
except FileNotFoundError:
    print('对不起, 文件' + filename + '不存在!')
else: 
    words = contents.split()   # contents在这里也可以被使用, 说明contents的作用域不止try-except范围
    words_num = len(words)
    print('文件' + filename + '中总共包含' + str(words_num) + '个单词.')

# 使用多个文件
def count_words(filename):  # 先定义一个计算文件含多少个单词的函数
    """计算一个文件中包含多少个单词"""
    try: 
        with open(filename) as file_content:   # 这个as之后的变量名并非固定为file_object
            contents = file_content.read()
    except FileNotFoundError:
        print('对不起, 文件' + filename + '不存在!')
        # pass  # pass表示程序发现错误之后, 什么都不做
    else: 
        words = contents.split()   # contents在这里也可以被使用, 说明contents的作用域不止try-except范围
        words_num = len(words)
        print('文件' + filename + '中总共包含' + str(words_num) + '个单词.')


print('\n')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:  # 处理异常的好处: siddhartha.txt文件不存在, 但是不影响其他后续其他文件的计算
    count_words(filename)

# 失败时一声不吭
# 并非每次捕获到异常时都需要告诉用户, 有时候你希望程序在发生异常时一声不吭, 
# 就像什么都没有发生一样继续运行. 
# 要让程序在失败时一声不吭, 可像通常那样编写try代码块, 
# 但在except代码块中明确地告诉Python什么都不要做. 
# Python有一个pass语句, 可在代码块中使用它来让Python什么都不要做. 

# pass语句还充当了占位符, 它提醒你在程序的某个地方什么都没有做, 并且以后也许要在这里做些什么
# 有点像Java里的TODO标识
# Python有没有像Java中的Exception和Throwable这样的顶级异常? 