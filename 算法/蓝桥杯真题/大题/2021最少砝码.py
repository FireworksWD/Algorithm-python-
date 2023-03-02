n = int(input())
cnt, t, res = 1, 1, 1
while n > t:
    cnt += 1
    res *= 3
    t += res
print(cnt)
