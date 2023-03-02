for i in range(100):
    for j in range(100):
        if 97 * i - 127 * j == 1:
            print(i + j)
            break
