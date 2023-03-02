import datetime
star = datetime.datetime(2000, 1, 1)
deal = datetime.timedelta(days=1)
end = datetime.datetime(2020, 10, 1)
t = end - star
s = 0
while star <= end:
    if star.day == 1 or star.weekday() == 0:
        s += 2
    else:
        s += 1
    star += deal
print(s)