var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])


var1 = 'Hello World!'
print("更新字符串 :- ", var1[:6] + 'Runoob!')


print("")
print("======================")
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")

if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')


print("My name is %s and weight is %d kg!" % ('Zara', 21))




s = 'a, BCD'
print(s.capitalize())       #该方法返回一个首字母大写的字符串


#该方法返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。
str = 'runoob'
print(str.center(20, '*'))      #'*******runoob*******'
print(str.center(20))           #'       runoob


#返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常
str1 = "this is string example....wow!!!";
str2 = "is";

print(str1.rindex(str2));
print(str1.index(str2));


#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
str = "this is string example....wow!!!";
print(str.rjust(50, '0'))


#rpartition() 方法类似于 partition() 方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符
str = "www.runoob.com"
print(str.rpartition("."))




print("")
print("split=============")
#Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str.split( ))
print(str.split(' ', 1 ))


print("")
print("splitlines=============")
#Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
str1 = 'ab c\n\nde fg\rkl\r\n'
print(str1.splitlines())
str2 = 'ab c\n\nde fg\rkl\r\n'
print(str2.splitlines(True))


print("")
print("startswith=============")
#Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
#strbeg -- 可选参数用于设置字符串检测的起始位置。
#strend -- 可选参数用于设置字符串检测的结束位置。
str = "this is string example....wow!!!";
print(str.startswith( 'this' ))
print(str.startswith( 'is', 2, 4 ))
print(str.startswith( 'this', 2, 4 ))


print("")
print("strip and rstrip=============")
#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
str = "00000003210Runoob01230000000";
print(str.strip( '0' ))  # 去除首尾字符 0
str2 = "   Runoob      ";   # 去除首尾空格
print(str2.strip())
#Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
str = "     this is string example....wow!!!     ";
print(str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print(str.rstrip('8'))


print("")
print("swapcase=============")
#Python swapcase() 方法用于对字符串的大小写字母进行转换。
str = "this is string example....wow!!!";
print(str.swapcase())
str = "THIS IS STRING EXAMPLE....WOW!!!";
print(str.swapcase())


print("")
print("title=============")
#Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
str = "this is string example....wow!!!";
print(str.title())


print("")
print("upper=============")
#返回小写字母转为大写字母的字符串。
str = "this is string example....wow!!!";
print("str.upper() : ", str.upper())


print("")
print("upper=============")
#Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
str = "this is string example....wow!!!";
print(str.zfill(40))
print(str.zfill(50))


print("")
print("upper=============")
#Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
str = "this is string example....wow!!!";

sub = "i";
print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print("str.count(sub) : ", str.count(sub))


print("")
print("encode=============")
#Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码
# str = "this is string example....wow!!!";
# str = str.encode('base64','strict');
# print("Encoded String: " + str)
# print("Decoded String: " + str.decode('base64','strict'))

print("")
print("endswith=============")
#Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置
str = "this is string example....wow!!!";

suffix = "wow!!!";
print(str.endswith(suffix))
print(str.endswith(suffix,20))

suffix = "is";
print(str.endswith(suffix, 2, 4))
print(str.endswith(suffix, 2, 6))


print("")
print("expandtabs=============")
#Python expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
str = "this is\tstring example....wow!!!";
print("Original string: " + str)
print("Defualt exapanded tab: " +  str.expandtabs())
print("Double exapanded tab: " +  str.expandtabs(16))

print("")
print("expandtabs=============")
#python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str1 = "this is string example....wow!!!";
str2 = "exam";
print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))


print("")
print("format=============")
#Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的



print("")
print("format=============")
#Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.index(str2))
print(str1.index(str2, 10))
# print(str1.index(str2, 40))



print("")
print("isalnum=============")
#Python isalnum() 方法检测字符串是否由字母和数字组成。
str = "this2009";  # 字符中没有空格
print(str.isalnum())

str = "this is string example....wow!!!";
print(str.isalnum())
str = "this";  # No space & digit in this string
print(str.isalpha())
str = "this is string example....wow!!!";
print(str.isalpha())



print("")
print("isalnum=============")
#Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
str = u"this2009";
print(str.isdecimal())

str = u"23443434";
print(str.isdecimal())



print("")
print("isalnum=============")
#Python isalnum() 方法检测字符串是否只由数字组成
str = "123456";  # Only digit in this string
print(str.isdigit())

str = "this is string example....wow!!!";
print(str.isdigit())


print("")
print("islower=============")
#Python islower() 方法检测字符串是否由小写字母组成。
str = "THIS is string example....wow!!!";
print(str.islower())

str = "this is string example....wow!!!";
print(str.islower())



print("")
print("isnumeric=============")
#Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象
str = u"this2009";
print(str.isnumeric())

str = u"23443434";
print(str.isnumeric())


print("")
print("isspace=============")
#Python isspace() 方法检测字符串是否只由空格组成
str = "       ";
print(str.isspace())
str = "This is string example....wow!!!";
print(str.isspace())


print("")
print("istitle=============")
#Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
str = "This Is String Example...Wow!!!";
print(str.istitle())
str = "This is string example....wow!!!";
print(str.istitle())


print("")
print("isupper=============")
#Python isupper() 方法检测字符串中所有的字母是否都为大写
str = "THIS IS STRING EXAMPLE....WOW!!!";
print(str.isupper())

str = "THIS is string example....wow!!!";
print(str.isupper())


print("")
print("join=============")
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print(str.join( seq ))



print("")
print("ljust=============")
#Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
str = "this is string example....wow!!!";
print(str.ljust(50, '0'))


str = "THIS IS STRING EXAMPLE....WOW!!!";
print(str.lower())

# lstrip() 方法用于截掉字符串左边的空格或指定字符。
str = "     this is string example....wow!!!     ";
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888";
print(str.lstrip('8'))


str = "www.runoob.com"
print(str.partition("."))

str = "this is really a string example....wow!!!";
print("Max character: " + max(str))

str = "this is a string example....wow!!!";
print("Max character: " + max(str))



str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))
print(str.replace("is", "was", 3))




str = "this is really a string example....wow!!!";
substr = "is";

print(str.rfind(substr))
print(str.rfind(substr, 0, 10))
print(str.rfind(substr, 10, 0))

print(str.find(substr))
print(str.find(substr, 0, 10))
print(str.find(substr, 10, 0))