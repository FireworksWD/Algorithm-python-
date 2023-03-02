n = int(input())
ans = 0
for i in range(1, n + 1):
    if int(i ** 0.5) == i ** 0.5:
        x = [int(i) for i in str(i)]
        s = sum(x)
        if int(s ** 0.5) == s ** 0.5:
            ans += 1
print(ans)
