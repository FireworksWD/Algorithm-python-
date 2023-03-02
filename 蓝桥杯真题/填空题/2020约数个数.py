x = 1200000
ans = set()
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
        ans.add(i)
        if x // i != i:
            ans.add(x // i)
print(len(ans))
