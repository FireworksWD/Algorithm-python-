n = int(input())
ans = 0


def check(x):
    while x:
        t = x % 10
        if t == 2 or t == 4:
            return False
        x //= 10
    return True


for i in range(1, n // 3):
    for j in range(i + 1, n):
        k = n - j - i
        if k <= j or k <= 0: continue
        if check(i) and check(j) and check(k): ans += 1
print(ans)
