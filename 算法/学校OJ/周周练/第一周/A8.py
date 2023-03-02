res = 0
for i in range(1, 1000000):
    res += str(i).count('1')
    if res == 2021:
        print(i)
        break
