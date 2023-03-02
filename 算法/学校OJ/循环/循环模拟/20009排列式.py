ans = 0
for i in range(11, 99):
    for j in range(123, 987):
        a = [0] * 10
        x = i * j
        if x > 9876:
            continue
        a[i // 10] += 1
        a[i % 10] += 1
        a[j // 100] += 1
        a[j % 100 // 10] += 1
        a[j % 10] += 1
        a[x // 1000] += 1
        a[x % 1000 // 100] += 1
        a[x % 100 // 10] += 1
        a[x % 10] += 1
        v = 0
        for k in range(1, 10):
            if a[k] == 1:
                v += 1
        if v == 9:
            ans += 1
print(ans)
