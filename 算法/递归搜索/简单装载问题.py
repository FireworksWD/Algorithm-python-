n, c = map(int, input('集装箱的个数和轮船载重量：').split())
w = list(map(int, input('集装箱的重量：').split()))
thisw, bestw, rw = 0, 0, sum(w)
vis = [False] * n
result = [] * n


def backtrack(i):
    global thisw, bestw, result, rw
    if i >= n:
        if thisw > bestw:
            bestw = thisw
            result = vis
        return
    rw -= w[i]
    if thisw + w[i] <= c:
        vis[i] = True
        thisw += w[i]
        backtrack(i + 1)
        thisw -= w[i]
    if thisw + rw > bestw:
        vis[i] = False
        backtrack(i + 1)
    rw -= w[i]


backtrack(0)
print(bestw)
print(result)
