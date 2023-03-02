n, k = map(int, input().split())
m = k // n
l = k % n
ans1 = m * (n - 1) * n // 2 + l * (l + 1) // 2
print(ans1)
