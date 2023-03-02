n = int(input())
cnt = 0
while n != 1:
    if n & 1:
        n = (3 * n + 1) >> 1
        cnt += 1
    else:
        n >>= 1
        cnt += 1
print(cnt)
