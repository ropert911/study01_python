counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)
c = 2
print(a, b, c)
# 1 和 2 分别分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。
a, b, c = 1, 2, "john"
print(a, b, c)

var1 = 1
var2 = 10
print(var1, var2)
del var1, var2

a = 10
# b = 519243611111L
c = 0.0
d = 3.14j
print(a, b, c, d)


print()
print("字符串===================================")
str = 'Hello World!'
print (str)           # 输出完整字符串
print (str[0])        # 输出字符串中的第一个字符
print (str[2:5])      # 输出字符串中第三个至第五个之间的字符串
print (str[2:])       # 输出从第三个字符开始的字符串
print (str * 2)       # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串


print()
print("列表===================================")
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表



print()
print("""元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。========""")
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素
print(tuple[2:])          # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组


print()
print("""字典=======================================================""")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值


print()
print("""算法运算=======================================================""")
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b        #幂 - 返回x的y次幂
print("6 - c 的值为：", c)

a = 10
b = 5
c = a//b        #取整除 - 返回商的整数部分（向下取整）
print("7 - c 的值为：", c)




print()
print("""Python比较运算符=======================================================""")
a = 21
b = 10
c = 0

if ( a == b ):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if ( a != b ):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if ( a < b ):
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if ( a > b ):
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")

if ( b >= a ):
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")




print()
print("""Python赋值运算符=======================================================""")
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)




print()
print("""Python位运算符=======================================================""")
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print("1 - c 的值为：", c)

c = a | b;        # 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print("2 - c 的值为：", c)

c = a ^ b;        #按位异或运算符：当两对应的二进位相异时，结果为1
print("3 - c 的值为：", c)

c = ~a;           #按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
print("4 - c 的值为：", c)

c = a << 2;       #左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
print("5 - c 的值为：", c)

c = a >> 2;       #右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
print("6 - c 的值为：", c)





print()
print("""Python逻辑运算符=======================================================""")
a = 10
b = 20

if ( a and b ):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if ( a and b ):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not( a and b ):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")


print()
print("""Python成员运算符=======================================================""")
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")



print()
print("""Python身份运算符=======================================================""")
a = 20
b = 20

if ( a is b ):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if ( a is not b ):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

# 修改变量 b 的值
b = 30
if ( a is b ):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if ( a is not b ):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")