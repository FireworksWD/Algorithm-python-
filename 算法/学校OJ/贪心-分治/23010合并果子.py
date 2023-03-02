lis1 = list(map(int, input().split()))
n = lis1[0]
lis = lis1[1:]
lis.sort()
ans = 0
while n - 1:
    temp = lis[0] + lis[1]
    ans += temp % 2310000
    lis[1] = temp
    lis.pop(0)
    lis.sort()
    n -= 1
print(ans % 2310000)
