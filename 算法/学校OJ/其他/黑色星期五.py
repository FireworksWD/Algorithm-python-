import datetime
x=int(input())
start=datetime.datetime(x,1,1)
delta=datetime.timedelta(days=1)
end=datetime.datetime(x,12,31)
temp=0
while start<=end:
    if start.day==13 and start.weekday()==4:
        temp+=1
    start+=delta
print(temp)