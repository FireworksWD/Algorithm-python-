def check(x):
    while x:
        if x % 10 == 2 or x % 10 == 4:
            return False
        x //= 10
    return True


ans = 0
for i in range(1, 2019 // 3 + 1):
    for j in range(i + 1, 2019 // 3 * 2 + 1):
        k = 2019 - i - j
        if k <= j or k < 0: continue
        if check(i) and check(j) and check(k):
            ans += 1
print(ans)
