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
#可以用'...',"...","""..."""表示
'''
例如
name = 'Aitouka'
name = "Aitouka"
name = """Aitouka"""
PS:单引号定义可以内涵双引号
双引号定义可以内涵单引号
转义字符可以表示解除引用
'''

#字符串拼接
#1.利用加法拼接
'''
print("my name is" + "AItouka") 
变量也一样
print("my name is" + name) 
'''
#2.字符串格式化
'''
name = "Aitouka"
message = "my name is %s" % name
print(message)
%s为占位符
name = "Aitouka"
print("my name is %s" % name)
与此同时，%d为整形,%f为浮点型

ps：精度控制
%5d，控制五位，如果为11，则输出   11；若宽度小于自身则不生效
%.2f,小数点精度为2，四舍五入；和小数点都算入宽度计算
eg：对于11.345，以%7.2f输出
则为：  11.34
'''
#字符串格式化2
'''
name = "aitouka"
print(f"我是{name}")
以f("...{变量名}")完成快速格式化
但是无法进行精度控制
'''

#表达式格式化
'''
eg
print("1+1=%s" % (1+1))
print(f"1+1= {1+1}")
print("字符串的类型为：%s" % type("字符串"))
'''

#章节练习
name = 'CUST'
stock_price = 19.99
stock_code = '003032'
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数为：%.1f，经过%d天后的增长，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))

#数据输入
'''
input函数，输入语句，从键盘的输入内容获取输入
eg：
print("what is your name")
input()
print("yes")
注意前两句可以简化为：input("what is your name"),此时会在第一句的后面输入没有换行
并且输入默认为字符串形式
'''

#训练二
username = input("请输入姓名：")
usertype = input("请输入等级：")
print(f"hello: {username},您是 {usertype}，欢迎使用")
