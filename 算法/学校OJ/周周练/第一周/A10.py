n = int(input())
f = [1, 1]
for i in range(3, n + 1):
    x = (f[0] + f[1]) % 10007
    f[0] = f[1]
    f[1] = x
print(f[-1])
