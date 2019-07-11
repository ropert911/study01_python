# -*- coding: utf-8 -*-

# @property
# 参考https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820062641f3bcc60a4b164f8d91df476445697b9e000
# @staticmethod 类静态方法
# http://www.runoob.com/python/python-func-staticmethod.html
# @abstractmethod 类抽像方法
# class AHiveDataHandler(ABC)  抽象类

class TimeConstant:
    # 时间配置
    MIN_MICRO_SECOND = 0
    MAX_MICRO_SECOND = 999999
    MIN_SECOND = 0
    MAX_SECOND = 59
    MIN_MINUTE = 0
    MAX_MINUTE = 59
    MIN_HOUR = 0
    MAX_HOUR = 23
    MIN_MONTH = 1
    MAX_MONTH = 12
    MIN_DAY = 1
    MAX_DAY = 31
    # Number of days per month
    MDAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_MDAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_MONTH = 2
    WEEK_DAYS = 7


import calendar
import datetime
from collections import namedtuple


def time_delta(src: datetime, years: int = 0, months: int = 0, weeks: int = 0, days: int = 0,
               hours: int = 0) -> datetime:
    """对src进行时间差的计算。 可以计算年月周日时的时间差，可以同时指定，如果设置为负数表示求前一个时间点，如果
    设置为正数，表示求将来的时间点。

    :param src: 源时间点，type: datetime
    :param years: 年份的差值， type: int
    :param months: 月份的差值， type: int
    :param weeks: 周的差值， type: int
    :param days: 日的差值， type: int
    :param hours: 小时的差值， type: int

    :return: 计算后的datetime的对象
    """

    # 利用timedelta先计算时，天，周的差值
    src += datetime.timedelta(hours=hours, days=days, weeks=weeks)
    # 计算月的差值
    dy, dm = divmod(src.month + months, TimeConstant.MAX_MONTH)
    # 如果余数刚好是0(刚好被12整除)，那么是上一年的12月份
    month = dm or TimeConstant.MAX_MONTH
    dy = src.year + dy + years
    # 如果余数刚好是0(刚好被12整除)，那么是上一年的12月份
    year = dy if dm else dy - 1
    # 如果源时间是月份的最后一天，需要判断计算后的月份是否有31号(如果是2月，还需要判断是否是闰年)
    day = src.day
    if src.day == TimeConstant.MAX_DAY:
        day = TimeConstant.MDAYS[month]
    if month == TimeConstant.LEAP_MONTH and src.day > TimeConstant.MDAYS[TimeConstant.LEAP_MONTH]:
        day = TimeConstant.LEAP_MDAYS[TimeConstant.LEAP_MONTH] if calendar.isleap(year) else TimeConstant.MDAYS[
            TimeConstant.LEAP_MONTH]
    return src.replace(year=year, month=month, day=day)


class RangeTime:
    """给定一个指定的时间区间，可以返回区间包含的小时，天，月和年，返回类型都是datetime对象，包含前后的时间值。
    """

    # xiaoqian:已看
    def __init__(self, start_time, end_time):
        # info('RangeTime start: {}, end: {}'.format(start_time, end_time))
        self.start_time = start_time
        self.end_time = end_time

    def _yield_datetime(self, years=0, months=0, weeks=0, days=0, hours=0):
        ret = []
        temp = self._yield_datetime_helper(self.start_time, years, months, weeks, days, hours)
        while True:
            ret.append(temp)
            temp = time_delta(temp, years, months, weeks, days, hours)
            if temp > self.end_time:
                break
        return ret

    @staticmethod
    def _yield_datetime_helper(src, years=0, months=0, weeks=0, days=0, hours=0):
        deltas = [_ for _ in [years, months, weeks, days, hours] if _ != 0]
        # 区间计算，只能选择年月周日时中一个进行运算，不能一次计算多个
        if sum([1 for _ in deltas]) > 1:
            raise KeyError('You can only assign one parameter.')
        ret = src.replace(minute=0,
                          second=0,
                          microsecond=0)
        if years:
            ret = ret.replace(month=1, day=1, hour=0)
        elif months:
            ret = ret.replace(day=1, hour=0)
        elif days:
            ret = ret.replace(hour=0)
        return ret

    @property
    def hours(self):
        # 区间计算，按照步长为1进行递增
        return self._yield_datetime(hours=1)

    @property
    def days(self):
        # 区间计算，按照步长为1进行递增
        return self._yield_datetime(days=1)

    @property
    def weeks(self):
        raise NotImplemented

    @property
    def months(self):
        # 区间计算，按照步长为1进行递增
        return self._yield_datetime(months=1)

    @property
    def years(self):
        # 区间计算，按照步长为1进行递增
        return self._yield_datetime(years=1)


class WeekTime:
    """用于设定周开始日期，并且计算某一天属于的周的起始和结束时间，默认从周一开始进行计算，并且以[1,2,3,4,5,6,7]的方式
    表示周一到周日，也就是说1代表周一，7代表周日。
    """

    def __init__(self, weekday=1):
        self.weekday = weekday

    def set_first_week(self, weekday=1):
        self.weekday = weekday

    def build_se_time(self, day):
        # calendar模块默认用0表示周一，6表示周日
        real = calendar.weekday(day.year, day.month, day.day) + 1
        start_time = day - datetime.timedelta(days=(real - self.weekday))
        # 如果计算的起始时间大于了当前需要计算的时间，证明当前时间是属于上一个的某个周期
        while start_time > day:
            start_time -= datetime.timedelta(days=TimeConstant.WEEK_DAYS)
        # 由于起始时间已经包含了一天，所以计算结束日期的时候，只需要加上6天即可
        end_time = start_time + datetime.timedelta(days=(TimeConstant.WEEK_DAYS - 1))
        start_time = start_time.replace(hour=TimeConstant.MIN_HOUR,
                                        minute=TimeConstant.MIN_MINUTE,
                                        second=TimeConstant.MIN_SECOND,
                                        microsecond=TimeConstant.MIN_MICRO_SECOND)
        end_time = end_time.replace(hour=TimeConstant.MAX_HOUR,
                                    minute=TimeConstant.MAX_MINUTE,
                                    second=TimeConstant.MAX_SECOND,
                                    microsecond=TimeConstant.MAX_MICRO_SECOND)
        # 这里自定义一个结构类型
        WeekSTTime = namedtuple('WeekSTTime', ('start_time', 'end_time'))
        return WeekSTTime(start_time, end_time)


start_time1 = 2018081601
# start_time=0
time1 = datetime.datetime.strptime(str(start_time1), '%Y%m%d%H') if start_time1 else None

start_time2 = 2018091702
# start_time=0
time2 = datetime.datetime.strptime(str(start_time2), '%Y%m%d%H') if start_time2 else None

rang = RangeTime(time1, time2)
print(rang.years)
print(rang.months)
# print(rang.days)
# print(rang.hours)

week = WeekTime()
print(week.build_se_time(time1))
