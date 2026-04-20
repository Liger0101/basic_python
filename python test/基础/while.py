#while循环
'''
常见语法
while 条件(bool类型) :
    满足，结果1
    满足，结果2
    满足，结果3
    ...
'''
#例子
# i = 0
# while i<10:
#     print(i)
#     i=i+1
#需要设置终止条件，否则无限循环

#案例2
# i = 1
# sum = 0
# while i<= 100 :
#     sum += i
#     i += 1
# print(sum)

#数字判断优化
# import random
# num = random.randint(1,100)
# count = 0
# flag = True
# while flag :
#     guess_num = int(input('请输入你所猜的数字：'))
#     count += 1
#     if guess_num == num :
#         print('你猜对了')
#         flag = False
#     elif guess_num > num :
#         print('你猜大了')
#     else :
#         print('你猜小了')
# print(count)

#while嵌套循环
# while 条件1 :
#     满足，结果1
#     满足，结果2
#     while 条件2 :
#         满足，结果1
#         满足，结果2

#案例3（九九乘法表）
# ps: 默认print语句输出完会自动换行，如果输出不换行，则利用print('字符串',end = '')
# 特殊符号\t可实现多行字符串对其
i = 1
while i <= 9 :
    j = 1
    while j <= i :
        if j < i :
            print(f"{j} * {i} = {j * i}\t",end = '')
        else :
            print(f"{j} * {i} = {j * i}\t")
        j += 1
    i += 1
#可以换成最后写一个print()表示换行
i = 1
while i <= 9 :
    j = 1
    while j <= i :
        print(f"{j} * {i} = {j * i}\t",end = '')
        j += 1
    i += 1
    print()