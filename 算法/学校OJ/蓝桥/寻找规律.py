c=0
for i in range(123, 329):
    j = i*2
    k = i*3
    x = str(int(i))
    y = str(int(j))
    z = str(int(k))
    s = set()
    s.update(x, y, z)
    if len(s) == 9 and '0' not in s:
       c+=1
print(c)