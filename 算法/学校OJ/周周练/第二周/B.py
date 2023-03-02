n, q = map(int, input().split())
price = list(map(int, input().split()))
price.sort(reverse=True)
check = []
for i in range(q):
    check.append(list(map(int, input().split())))
for i in range(q):
    x = price[:check[i][0]]
    t = 0
    for j in range(check[i][1]):
        t += x[len(x) - 1 - j]
    print(t)
