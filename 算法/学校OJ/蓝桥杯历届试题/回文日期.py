import datetime

s = input()
y, m, d = int(s[:4]), int(s[4:6]), int(s[6:8])
start = datetime.date(y, m, d)
dalta = datetime.timedelta(days=1)
f = True
while True:
    start += dalta
    x = start.strftime("%Y%m%d")
    if x == x[::-1]:
        if f:
            print(x)
            f = False
    if x[0] == x[2] == x[5] == x[7] and x[1] == x[3] == x[4] == x[6]:
        print(x)
        break
