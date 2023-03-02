import datetime

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
# print((end - start).days // 7)
delta = datetime.timedelta(days=1)
t = 0
while start <= end:
    if start.isoweekday() == 1:
        t += 1
    start += delta
print(t)
