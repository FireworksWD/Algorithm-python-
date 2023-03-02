n = int(input())
j = 0
p = 0
for i in range(n):
    a = int(input())
    if 60 < a <= 85:
        j += 1
    if a > 85:
        p += 1
r1 = (j+p)/n
r2 = p/n
print(int(r1*100+0.5), '%', sep='')
print(int(r2*100+0.5), '%', sep='')