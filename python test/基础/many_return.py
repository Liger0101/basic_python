#一、函数多返回值
# 若一个函数要返回多个返回值，可以用以下语法
def test_return():
    return 1, 'hello', True
x, y, z= test_return()
print(x)
print(y)
print(z)
#其中按照顺序进行多个变量的吸收，变量之间用逗号隔开，且支持不同类型的数据return

#二、函数的多种传参方式
#1.常见参数方式有：位置；关键字；缺省；不定长
#（1）：位置参数：根据函数定义的参数位置来传递参数
def user_info(name, age, gender):
    print(f'姓名：{name},年龄为：{age},性别为：{gender}')

user_info('tom',24,'男')

#关键字传参：键等于参
user_info(name = 'Tonny', age = 21, gender = 'M')
#可以不按照固定顺序
user_info(age = 21, gender = 'M',name = 'Tonny')
#可以和位置参数混用但必须位置参数在前并匹配参数顺序
user_info('Tonny', age = 21, gender = 'M')

#缺省参数又称默认参数，定义函数时给参数默认值（ps：所有位置参数必须在默认参数前，包括定义与调用）
#除非改变对应值，否则用默认值

def user_info2(name, age, gender = '男'):
    print(f'姓名：{name},年龄为：{age},性别为：{gender}')

user_info2('Tonny', 21,'女')
user_info2('Tonny', 21)

#不定长参数，又称可变参数，用于不确定调用时会传递多少参数，分为位置传递和关键字传递
#1.位置传递：变量吸收所有参数并合成一个元组,args为元组类型
def user_info3(*agrs):
    print(agrs)
    print(type(agrs))

user_info3('Tonny')
user_info3('Tonny',11)

#关键字传递：根据键 = 值组成字典
def user_info4(**kwargs):
    print(kwargs)
    print(type(kwargs))

user_info4(name = 'Tonny', age = 21, gender = 'M')

#三、匿名函数
# 1.函数作为参数传递
# eg
def test(compute):#要求传入代码的执行逻辑
    result = compute(1,2) #利用函数作为参数，可以使之使用不同的函数，常用于参数已知，参需要改变执行逻辑
    print(result)
def add(x, y):
    return x + y

test(add) #3
#是一种逻辑运算的传递而非数据的传递
# def test():
#     result = add(1,2) #相比之下，这个代码只能使用一种函数
#     print(result)
# def add(x, y):
#     return x + y
#
# test(add) #3

#Lambda匿名函数
# 函数定义中：def定义带有名称的函数，lambda定义匿名函数（无名称）
# 有名称的函数可以重复使用，但无名称的匿名函数只能临时使用一次
# lambda 传入参数 : 函数体(一行代码)
# eg：
# def fun_test(compute):
#     result = compute(1,2)
#     print(result)
#
# def fun_add(x, y):
#     return x + y
#
# fun_test(fun_add)
#可化为：
def fun_test(compute):
    result = compute(1,2)
    print(result)

fun_test(lambda x, y: x + y) #只能使用一次
fun_test(lambda x, y: x - y)
