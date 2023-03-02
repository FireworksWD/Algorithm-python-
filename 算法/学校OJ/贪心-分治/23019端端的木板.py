# n = int(input())
# a = [int(input()) for _ in range(n)]
a1 = list(map(int, input().split()))
n = a1[0]
a = a1[1:]
a.sort()
ans = 0
while n - 1:
    x, y = a[0], a[1]
    ans += x + y
    a[1] = x + y
    a.pop(0)
    a.sort()
    n -= 1
print(ans)
