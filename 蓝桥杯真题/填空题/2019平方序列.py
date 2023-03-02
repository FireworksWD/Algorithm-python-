def solve():
    for i in range(2020, 3200):
        for j in range(i + 1, 3910):
            if i ** 2 - 2019 ** 2 == j ** 2 - i ** 2 and 2 * i ** 2 == 2019 ** 2 + j ** 2:
                # print(i, j)
                print(i+j)
                return


solve()
