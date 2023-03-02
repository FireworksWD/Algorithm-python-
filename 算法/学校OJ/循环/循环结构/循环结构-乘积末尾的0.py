n = int(input())
s = len(str(n))
c = 0
for i in range(1, s+1):
     c += n // 5**i
print(c)     