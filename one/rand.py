import random
import math

# 输入函数
num = input("请输入一个三位数：")
# 检测输入是否为纯数字
if num.isdigit() and 100 <= int(num) <= 999:
    # 输入函数输入的是字符类型，不强制转换会报错
    pass
else:
    print("请按规定输入：")
