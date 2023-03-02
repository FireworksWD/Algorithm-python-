def main():
    a = [True] * (10 ** 4)
    res = []
    for i in range(2, 10 ** 4):
        if a[i]: res.append(i)
        for j in res:
            if i * j >= 10 ** 4:
                break
            a[i * j] = False
            if i * j == 0:
                break
    for i in range(len(res) - 9):
        for d in range(1, 1000):
            if a[res[i] + d] and a[res[i] + 2 * d] and a[res[i] + 3 * d] and a[res[
                                                                                   i] + 4 * d] and a[res[i] + 5 * d] and \
                    a[res[i] + 6 * d] and a[res[
                                                i] + 7 * d] and a[res[i] + 8 * d] and a[res[i] + 9 * d]:
                print(d)
                return


main()


def check(a, d, lis):
    for i in range(1, 10):
        if not lis[a + i * d]:
            return False
    return True


def isprime(n):
    res = [True] * n
    temp = []
    for i in range(2, n):
        if res[i]: temp.append(i)
        for j in temp:
            if i * j >= n: break
            res[i * j] = False
            if i % j == 0:
                break
    for k in temp:
        for d in range(1, 1000):
            if check(k, d, res):
                return d


print(isprime(10 ** 5))
