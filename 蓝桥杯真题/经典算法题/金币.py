k = int(input())
i = 1
res = 0
while k >= i:
    k -= i
    res += i * i
    i += 1
if k:
    res += k * i
print(res)
