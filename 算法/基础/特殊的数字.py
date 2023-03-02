for i in range(100, 1000):
    a, b, c = map(int, str(i))
    if pow(a, 3) + pow(b, 3) + pow(c, 3) == i:
        print(i)