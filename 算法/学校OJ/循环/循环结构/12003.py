a = int(input())
res = 0
for i in range(a // 3 + 1):
    for j in range(a // 2 + 1):
        k = a - j - i
        if k % 3 != 0:
            continue
        if i * 3 + j * 2 + k // 3 == a :
            res += 1
print(res)
