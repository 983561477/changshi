'''
    定义一个学生类，来形容学生
'''
# 定义一个空类
class Student():
    # pass代表直接跳过
    pass

# 定义一个对象
mingyue = Student()

# 定义一个 python 学生类
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 注意：
    # 1.def doHomework的缩进层级
    # 2.系统默认由一个self参数

    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，是个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()