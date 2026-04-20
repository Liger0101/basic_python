#一、函数初步，满足（提前写好的；可以重复使用的；实现目标功能的代码段）
#不用len(),定义一个函数来计算字符串长度
# def len_calculate(data):
#     count = 0;
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度为: {count}")
#
# str = 'dahsasjasdkas'
# len_calculate(str)

#利用将功能封装在函数中，函数用于减少重复性，提高效率

#二、函数的定义格式
# def 函数名(传入参数):
#     函数体
#     return 返回值
# eg：定义一个函数，输出相关信息
# def say_hello():
#     print('hello')
#函数的调用
#函数名(参数)
# say_hello()

# Ps:参数和返回值若不需要可以省略，且函数必须先定义再调用

#案例：欢迎语
# def welcome():
#     print('欢迎！\n请出示身份码')
#
# welcome()

#三、传入参数：函数进行计算时接受外部所提供的数据
# eg:加法运算
# def add(x, y): #x，y为形式参数，表示函数声明将要使用两个参数，且传入参数的个数不受限制，少则没有，多则无数个
#     result = x + y
#     print(f'{x} + {y} = {result}')
#
# add(2, 6) #2，6被称为实际参数，即函数执行时真正使用的参数值

#案例：查核酸
# def check(x):
#     print('请配合测量体温')
#     if x <= 37.5 :
#         print('体温正常')
#     else :
#         print('需要隔离')
#
# check(31.5)
# check(38)

#四、函数的返回值
# eg：
# def add2(a,b):
#     result = a + b
#     return result #两数相加的结果返回给函数调用者，所以返回值即程序完成函数调用后最后给调用者的结果
# print(add2(1,2))
# t = add2(1,2) #变量接受函数的返回值
# print(t)
#ps：函数中return后的代码全不进行，即函数到return即结束

#None类型：当函数没有使用return返回时所有的返回值，返回了None，即返回空
# eg:
# def say_hello():
#     print('hello') #不写return等同于return None
#
# result = say_hello()
# print(result)
# print(type(result))
# 一般用于以下几种情况：
# 1.函数无返回值
# 2.if语句中None等同Flase，一般函数中主动返回None，配合if进行相关处理
# eg：
# def check_age(age):
#     if age >= 18:
#         return 'sucess'
#     else:
#         return None
#
# result = check_age(17)
# if not result:  #等同于result == None
#     #result为Flase，但这个条件为True
#     print('禁止入内')
# 3.定义变量，但暂时不需要变量有确定值

#五、可以通过多行注释对函数进行说明
# eg:
# def add3(x, y, z):
#     '''
#     add3接受三个参数并进行相加
#     :param x: 形参x
#     :param y: 形参y
#     :param z: 形参z
#     :return: 返回值为三个数相加的结果
#     '''
#     result = x + y + z
#     return result
#
# add3(6, 7, 8) #鼠标悬停在括号上即可看见函数说明

#六、函数的嵌套
# 格式：
# def fun1():
#     函数体
# def fun2():
#     函数体上半
#     fun1()
#     函数体下半
#
# fun2()

#七、变量的作用域分为：全局变量和局部变量
#局部变量为定义在函数体内部的变量，在函数外调用会报错，起到临时保存数据的作用
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# print(num) #无法使用
#全局变量是在函数体内和外部都可使用的变量，只要在函数体外定义即可
# num = 100
# def testA():
#     print(num)
# def testB():
#     print(num)
# testA()
# testB()
# print(num)

# ps:在函数内改变变量相当于重新定义了一个局部变量，对外部的全局变量没有影响
#但可以用global对num进行全局变量声明，那么此时就可以改变了
# num = 100
# def testA():
#     print(num)
# def testB():
#     global num
#     num = 500 #此时全局变量改变
#     print(num)

# testA()
# testB()
# print(num)

#综合案例：ATM机
name = None
name = input('请输入您的姓名：')
money = 500000
def query(frag):
    if frag :
        print('----------余额----------')
    print(f'余额还剩{money}')

def push():
    global money
    print('----------存款----------')
    push_num = int(input('请输入您想要存款的金额：'))
    money += push_num
    print(f'当前余额为：{money}')
    query(False)

def take():
    global money
    print('----------取款----------')
    take_num = int(input('请输入您想要取款的金额：'))
    money -= take_num
    print(f'当前余额为：{money}')
    query(False)

def menu():
    print('----------菜单----------')
    print(f'您好{name}，欢迎来到本ATM，请选择操作')
    print('查询余额\t 【请输入1】')
    print('取款\t\t 【请输入2】')
    print('存款\t\t 【请输入3】')
    print('退出\t\t 【请输入4】')
    return input('请选择您的操作：')

while True:
    input_num = menu()
    if input_num == '1':
        query(True)
        continue
    elif input_num == '2':
        take()
        continue
    elif input_num == '3':
        push()
        continue
    else :
        break
print("欢迎下次使用")
