import datetime

start_time=2018081601
# start_time=0
time = datetime.datetime.strptime(str(start_time), '%Y%m%d%H') if start_time else None
print(time)

now_time=1533300000000
time = datetime.datetime.fromtimestamp(float(now_time) / 1000) if now_time else datetime.datetime.today()
print(time)