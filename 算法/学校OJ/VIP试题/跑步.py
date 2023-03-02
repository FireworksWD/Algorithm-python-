import datetime
s = datetime.date(2000, 1, 1)
e = datetime.date(2020, 10, 2)
t = datetime.timedelta(days=1)
ans = 0
while s != e:
    if s.weekday() == 0 or e.day == 1:
        ans += 2
    else:
        ans +=1
    s = s + t
print(ans)