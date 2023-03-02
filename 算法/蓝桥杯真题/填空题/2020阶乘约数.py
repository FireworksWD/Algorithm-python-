li = [0 for i in range(100)]


def fj(n):
    tmp = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            tmp.append(i)
            n //= i
        i += 1
    if n > 1: tmp.append(n)
    return tmp


for i in range(2, 101):
    for j in fj(i):
        li[j] += 1
res = 1
for i in li:
    if i != 0:
        res *= (i + 1)
print(res)