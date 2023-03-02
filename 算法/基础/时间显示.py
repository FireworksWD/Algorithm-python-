import datetime
n=int(input())
start=datetime.datetime(1970,1,1,0,0,0,0)
delta=datetime.timedelta(milliseconds=n)
end=start+delta
hour=end.hour
minute=end.minute
seconds=end.second
print('{:0>2d}:{:0>2d}:{:0>2d}'.format(hour,minute,seconds))