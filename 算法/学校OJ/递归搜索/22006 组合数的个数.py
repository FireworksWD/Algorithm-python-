import math

n, r = map(int, input().split())
s = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
print(s)
