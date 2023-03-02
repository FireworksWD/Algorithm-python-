a = [0, 2, 4, 6, 8]
for i in range(1, 10 ** 5):
    x = 2019 * i
    j = x
    f = True
    while j:
        if j % 10 in a:
            f = False
            break
        j //= 10
    if f:
        print(x)
        break
