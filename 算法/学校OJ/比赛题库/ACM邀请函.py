s = list(input())
temp = list(set(s))
res_max = []
res_min = []
for i in temp:
    if ord(i) >= 65 and ord(i) <= 90:
        res_max.append(s.count(i))
    if ord(i) >= 97 and ord(i) <= 122:
        res_min.append(s.count(i))
if len(res_max) > 0:
    t1 = max(res_max)
else:
    t1 = 0
if len(res_min) > 0:
    t2 = min(res_min)
else:
    t2 = 0
if (t1 - t2) % 2 == 0:
    print('yes')
else:
    print('no')