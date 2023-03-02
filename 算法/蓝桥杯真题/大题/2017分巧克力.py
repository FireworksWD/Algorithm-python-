n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
l, r = 1, 10 ** 5
while l < r:
    mid = r + l >> 1
    cnt = 0
    for i in range(n):
        cnt += (a[i][0]//mid)*(a[i][1]//mid)
    if cnt >= k:
        l = mid + 1
    else:
        r = mid
print(l - 1)
