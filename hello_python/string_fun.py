# 测试Python字符串函数的文件

name = "ada lovelace"
print(name.title())  # title函数表示以首字母大写的方式显示每个单词

name = "Ada Lovelace"
print(name.upper())  # upper函数表示将字符串改为全部大写
print(name)          # name这个变量本身没有改变
print(name.lower())  # lower函数表示将字符串改为全部小写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name   # Python通过+来拼接字符串
print("Hello, " + full_name.title() + "!")