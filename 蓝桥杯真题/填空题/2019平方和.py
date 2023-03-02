def check(x):
    while x:
        if x % 10 in [2, 0, 1, 9]:
            return True
        x //= 10
    return False


ans = 0
for i in range(1, 2020):
    if check(i):
        ans += i**2
print(ans)
