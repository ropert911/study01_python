# -*- coding: UTF-8 -*-
import re

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
# 返回一个Match对象，span打印出起始位置
print "match======="
print re.match('www', 'www.runoob.com www.runoob.com').span()  # 在起始位置匹配
print re.match('com', 'www.runoob.com www.runoob.com')  # 不在起始位置匹配
line = "Cats are smarter than dogs Cats are smarter than dogs";
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # re.M :包含换行，  re.I忽略大小写
if matchObj:
    print "matchObj.group() : ", matchObj.group()           #返回所匹配的字符串
    print "matchObj.groups() : ", matchObj.groups()         #返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
    print "matchObj.group(1) : ", matchObj.group(1)         #第一个元素
    print "matchObj.group(2) : ", matchObj.group(2)         #第二个元素
else:
    print "No match!!"



# re.search 扫描整个字符串并返回第一个成功的匹配
print "\nsearch======="
print re.search('www', 'www.runoob.com').span()  # 在起始位置匹配
print re.search('com', 'www.runoob.com', re.M | re.I).span()  # 不在起始位置匹配
line = "Cats are smarter than dogs Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
    print "searchObj.group() : ", searchObj.group()         #匹配的整个表达式的字符串
    print "searchObj.groups() : ", searchObj.groups()        #返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
    print "searchObj.group(1) : ", searchObj.group(1)
    print "searchObj.group(2) : ", searchObj.group(2)
else:
    print "Nothing found!!"
searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
    print "searchObj.groups() : ", searchObj.groups()
    print "searchObj.group() : ", searchObj.group()
else:
    print "No match!!"


# re.search 检索和替换
print "\n检索和替换======="

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是:", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是:", num


sms="abcIot/12345d78)"
print "转义方式:{}".format(re.findall('Iot\/(\\w+)\)', sms))
print "非转义方式:{}".format(re.findall(r'Iot/(\w+)\)', sms))

body=' "邮件" : 254323626@qq.com \r\n "设备id" :  2345d78  \r\n  "发送人" :   肖迁   \r\n'
print "获取全部信息1111======:{}".format(re.findall('(\\S+)\\s+:\\s+(\\S+)\\s+', body))
print "获取全部信息22222======:{}".format(re.findall(':\\s+(\\S+)\\s+', body))
print "获取全部信息2222======:{}".format(re.findall(':\\s+(\\S+)\\s+\r\n', body))
print "获取全部信息333333======:{}".format(re.findall('\\s+:\\s+(\\w+)\\s+\r\n', body))  #这里只有2345d78可以,
print "获取全部信息333333======:{}".format(re.findall('设备id"\\s+:\\s+(\\w+)\\s+', body))

msg=body.split("\r\n")
for m in msg:
    if "设备id" in m:
        print m
        print "获取设备ID22222222222:{}".format(re.findall('设备id"\\s+:\\s+(\\w+)\\s+', m))

