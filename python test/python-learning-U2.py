'''
666#整数字面量
13.14#浮点数字面量
"华东理工"#字符串字面量
#上述为常见三种字面量
'''


'''
print(666)
print(13.14)
print("华东理工")
'''
#多行注释用'''...'''

#变量定义式：变量名称 = 变量的值

'''
#定义一个变量，用来记录钱包余额
money = 50
#print语句输出内容
print("钱包中还有：",money)
#买了个食物花费10元
money = money - 10
print("剩余",money,"元")
'''

'''
#数据类型有string（字符串），int（有符号整型），float（有符号浮点型）
#用type函数得出数据类型
print(type(666))
print(type(13.14))
print(type("华东"))
name = "华东"
name_type = type(name)
print(name_type)
'''

#ps：变量没有类型

'''
#类型转换
#1.数字转字符串
num_str = str(666)
num2_str = str(13.14)
print(type(num_str))
print(type(num2_str))
#2.字符串转数字
num = int("11")
print(type(num))
num2 = float("13.14")
print(type(num2))
#ps:2必须满足字符串中全是数字
#3.整数和浮点数
int_num = int(13.14)
print(type(int_num),int_num)
float_num = float(666)
print(type(float_num),float_num)
'''

#标识符命名含：中文（不建议用），英文，下划线，数字，其中数字不可开头，区分大小写，不可用关键字
#命名规范：1.见名知义 2.下划线区分单词 3.英文字母全小写

'''
运算符
+：加
-：减
*：乘
/：除
//：整除
%：求余
**：指数
'''
'''
print("1 + 1 =",1 + 1)
print("2 - 1 =",2 - 1)
print("2 * 3 =",2 * 3)
print("3 / 2 =",3 / 2)
print("12 // 11 =",12 // 11)
print("23 % 12 =",23 % 12)
print("2 ** 4 =",2 ** 4)
'''
#=为赋值运算符，可和算数运算符复合

#字符串的定义
#可以用'...',''...'','''...'''表示
