#for循环
# for是对一批内容逐个处理
# while则循环条件是自定义的，自控循环条件
'''
格式：
for 临时变量 in 待处理数据集 :（待处理数据集相当于c语言中for括号内的范围）
    循环内容
'''
# eg.遍历字符串
# name = 'asdfghjkl'
# for x in name :
#     print(x)
#ps:for无法定义循环条件，基本不可能无限循环

#例子(找a的个数)
name = 'sadjnkakjapdlasjdasdjkasda'
num = 0
for x in name:
    if x == 'a' :
        num += 1
print(num)

#range语法(更好确定循环次数)
# 数据集即为序列类型，其中包括字符串，列表，元组等
# range可以得到一个序列
#1.range(num):从0开始到num结束(不含num)的序列，eg：range(5)=>[0,1,2,3,4]
#2.range(num1,num2):从num1开始到num2结束的序列，不包括num2
#3.range(num1, num2, step):从num1开始到num2结束，数字间距为step，eg:range(5,10,2)输出为[5,7,9]
# for x in range(5):
#     print(x)
# for y in range(5, 10):
#     print(y)
# for z in range(5, 10, 2):
#     print(z)

#案例2（有多少偶数）
num = int(input('请输入终值：'))
sum = 0
for i in range(1, num+1):
    if i%2 == 0 :
        sum += 1
print(sum)

#补充：for中的临时变量仅作用于for循环中，循环外可以访问到该临时变量，但不建议这么做
# 但可以事先定义使之成为全局变量

#for循环嵌套
#案例（99乘法表）
for i in range(1, 10):
    for j in range(1,i+1):
        print(f'{j} x {i} = {j * i}\t',end='')
    print()

#continue和break,前者结束当前循环进入下一个循环，后者直接结束整个循环

#章节案例（发工资）
sum = 10000
for x in range(1, 21):
    import random
    num_work = random.randint(1, 11)
    if num_work < 5 :
        print(f'员工{x}，绩效分{num_work},不发工资下一个')
        continue
    else :
        sum -= 1000
        print(f'向员工{x}发放工资1000，账户余额{sum}')
    if sum == 0 :
        print('余额不足下个月再来')
        break

