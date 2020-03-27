#Date Time Module:
#------------------#
'''
The datetime module includes tools for working with dates, times and combinations.
The time module includes tools for working with times and dates in the recent past to
the near future.
'''
import datetime
print(datetime.datetime.today())
#2020-03-27 11:24:53.151024
now=datetime.datetime.today()
other=datetime.datetime(1995,3,12,22,10)
print(now-other)
#9146 days, 13:14:53.151181
datetime.timedelta(18901,35547,421000)
print(now-other)
#9146 days, 13:14:53.151181
print(datetime.MAXYEAR) #Returns the largest year number allowed in a date or datetime object
#9999
print(datetime.MINYEAR) #Returns the smallest year number allowed in a date or datetime object
#1
print(datetime.time())  #Returns a time object with hour, minute, second and microsecond
#00:00:00
print(datetime.timezone)  #Returns a timezone object