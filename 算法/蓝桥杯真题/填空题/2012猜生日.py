import datetime

start = datetime.date(1900, 1, 1)
delta = datetime.timedelta(days=1)
while True:
    s = list(start.strftime('%Y%m%d'))
    x = int(''.join(s))
    if x % 2012 == 0 and x % 3 == 0 and x % 12 == 0 and s[5] == '6':
        print(x)
        break
    start += delta
