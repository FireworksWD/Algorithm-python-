n = int(input())
for i in range(1, 100000):
    f = True
    temp = (1 + i) * i // 2
    for j in range(1, n + 1):
        if temp - j * 2 == n:
            print(f'{j} {i}')
            f = False
            break
    if f == False:
        break
