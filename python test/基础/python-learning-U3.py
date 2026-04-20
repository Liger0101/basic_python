##判断类型
#布尔类型
'''
result = 10 > 5
result2 = 'leedcode' == 'leadcode'
print(result) True
print(result2) False

类型均为bool

比较运算符
== 相等
！= 不相等
>/>= 大于/大于等于
</<= 小于/小于等于

num1 = 100
num2 = 100
print(f'result of 'num1 == num2' = {num1 == num2} }')
'''

##判断语句
'''
一般格式:
if 条件 :
    条件成立时所做的事
eg
if 10  > 5 :
    print('10 > 5')
ps:四格缩进是必要的,否则视为与if同级

'''

#案例1
'''
print("欢迎来到游乐场,儿童免费,成人收费")
age = int(input('请输入您的年龄: '))
if age >= 18 :
    print('您已成年,游玩需补票10元')
print('祝您游玩愉快')
'''

'''
双条件格式
if 条件 :
    结果1
else :    --(不需要条件)
    结果2
    
多条件格式
if 条件1 :
    结果1
elif 条件2 :
    结果2 
elif 条件3 :
    结果3
...
else :
    结果N
    
ps:多条件下,前者满足后者无论是否满足均舍弃,条件之间是互斥的
且else可以省略
条件判断中,可以在条件中直接使用input
eg 
if int(input('请输入你的年龄: ')) >= 18 :
    print('您已成年,游玩需补票10元')
    
'''

#条件嵌套
'''
格式
if 条件1 :
    结果1
    if 条件2 :
        结果2
外层满足才会进行内层判断,内外层以缩进程度区分
'''

#综合案例
import random
num1 = random.randint(1,10)
num = int(input('你所猜的数字为: '))
if num != num1 :
    if num > num1 :
        print('猜大了')
    else :
        print('猜小了')
    num = int(input('第二次猜的数字为: '))
    if num != num1:
        if num > num1:
            print('猜大了')
        else:
            print('猜小了')
        num = int(input('第三次猜的数字为: '))
        if num != num1:
            print('很遗憾,猜错了,答案为: %d' % num1)
        else :
            print('恭喜第三次猜对了')
    else:
        print('恭喜第二次猜对了')
else :
    print('恭喜第一次猜对了')

#代码过于长了,可用循环化简
