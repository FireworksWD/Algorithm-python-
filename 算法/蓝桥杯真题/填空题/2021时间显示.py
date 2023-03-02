import datetime

start = datetime.datetime(1970, 1, 1)
delta = datetime.timedelta(milliseconds=1)
n = int(input())
now = start + n * delta
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
