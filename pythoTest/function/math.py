import math


print("sum={}".format(sum([1, 2, 3])))
print("max={}".format(max([1, 2, 3])))
print("min={}".format(min([1, 2, 3])))
print ("abs(-45) : ", abs(-45))

#向上取整: ceil:取大于等于x的最小的整数值，如果x是一个整数，则返回x
print("math.ceil(1.5) = {}".format(math.ceil(1.5)))


#参考  https://www.cnblogs.com/renpingsheng/p/7171950.html
# copysign:把y的正负号加到x前面，可以使用0
# cos:求x的余弦，x必须是弧度
# degrees:把x从弧度转换成角度
# e:表示一个常量
# exp:返回math.e,也就是2.71828的x次方
# expm1:返回math.e的x(其值为2.71828)次方的值减１
# fabs:返回x的绝对值
# factorial:取x的阶乘的值
# floor:取小于等于x的最大的整数值，如果x是一个整数，则返回自身
# fmod:得到x/y的余数，其值是一个浮点数
# frexp:返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围
# fsum:对迭代器里的每个元素进行求和操作
# gcd:返回x和y的最大公约数
# hypot:如果x是不是无穷大的数字,则返回True,否则返回False
# isfinite:如果x是正无穷大或负无穷大，则返回True,否则返回False
# isinf:如果x是正无穷大或负无穷大，则返回True,否则返回False
# isnan:如果x不是数字True,否则返回False
# ldexp:返回x*(2**i)的值
# log:返回x的自然对数，默认以e为基数，base参数给定时，将x的对数返回给定的base,计算式为：log(x)/log(base)
# log10:返回x的以10为底的对数
# log1p:返回x+1的自然对数(基数为e)的值
# log2:返回x的基2对数
math.log(10)

# modf:返回由x的小数部分和整数部分组成的元组
math.modf(math.pi)
math.log2(32)
math.log2(20)
math.log2(16)

# pi:数字常量，圆周率
print(math.pi)

# pow:返回x的y次方，即x**y
math.pow(3,4)
math.pow(2,7)

# radians:把角度x转换成弧度
math.radians(45)
math.radians(60)

# sin:求x(x为弧度)的正弦值
math.sin(math.pi/4)
math.sin(math.pi/2)
math.sin(math.pi/3)

# sqrt:求x的平方根
math.sqrt(100)
math.sqrt(16)
math.sqrt(20)

# tan:返回x(x为弧度)的正切值
math.tan(math.pi/4)
math.tan(math.pi/6)
math.tan(math.pi/3)

# trunc:返回x的整数部分
math.trunc(6.789)
math.trunc(math.pi)
math.trunc(2.567)