def D():
    n = int(input())
    arrs = []
    for item in range(n):
        arr = list(map(int, input().split()))
        arrs.append(arr)
    for item in reversed(range(0, n)):
        for iter in range(item):
            arrs[item - 1][iter] += max(arrs[item][iter], arrs[item][iter + 1])
    print(arrs[0][0])
D()
