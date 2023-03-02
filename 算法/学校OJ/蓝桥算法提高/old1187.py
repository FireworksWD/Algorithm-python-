n = int(input())
a = list(map(int, input().split()))
res = []


def CompactIntegers(t, a, res):
    if t == n:
        for i in res:
            print(i, end=' ')
        print()
        print(len(res))
        return
    elif a[t] != 0:
        res.append(a[t])
    CompactIntegers(t + 1, a, res)


CompactIntegers(0, a, res)
