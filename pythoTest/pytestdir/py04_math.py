import math
import cmath
import sys

print(abs(-1))          #绝对值
# print(cmp(80,100))       #如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
print(max(1,2,3,4,10,6))       #返回给定参数的最大值，参数可以为序列
print(min(9,2,3,4,10,6))        #返回给定参数的最小值，参数可以为序列

print("")
print("math===========")
print(math.ceil(4.1))       #返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.exp(3))          #返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.fabs(3))         #返回数字的绝对值，如math.fabs(-10) 返回10.0
print(math.floor(3.7))      #返回数字的下舍整数，如math.floor(4.9)返回 4
print(math.log(100,10))     #如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print(math.log10(100))      #返回以10为基数的x的对数，如math.log10(100)返回 2.0
print(math.modf(3.26))      #返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print(math.pow(3, 3))       #x**y 运算后的值
print(round(2.3456, 3))     #返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数

print("")
print("cmath===========")
print(cmath.sqrt(-1))
print(cmath.sin(1))     #sin函数



print("")
print("sys===========")
print(sys.path)