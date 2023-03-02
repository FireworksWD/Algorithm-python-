import math

t, ans = 1, 2 ** 19
f = 0
for i in range(1, 20):
    t *= 2
    a = ans // t
    f += a
m = math.gcd(f + ans, ans)
print(f'{(f + ans) // m}/{ans // m}')
