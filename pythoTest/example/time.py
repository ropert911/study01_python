import time;  # 引入time模块


ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化日期
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 日历
import calendar
print("")
print("")
print("=======  日历：calendar  ===========")
cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)



print("")
print("")
print("=======  datetime  ===========")
import datetime

s = datetime.date.today();
print("datetime.date.today() = ", s)
print("加一天 ", s + datetime.timedelta(days=1));

start_time = 20180816010203
# start_time=0
time = datetime.datetime.strptime(str(start_time), '%Y%m%d%H%M%S') if start_time else None
print("strptime-----")
print(time)
print(time.date())
print(time.time())



now_time = 1533300000000
time = datetime.datetime.fromtimestamp(float(now_time) / 1000) if now_time else datetime.datetime.today()
print("fromtimestamp-----")
print(time)
