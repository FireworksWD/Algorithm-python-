c1, c2 = map(int, input('两艘轮船的容量:').split())
n = int(input('集装箱数量:'))
w = list(map(int, input('集装箱重量:').split()))
thisw, bestw, r = 0, 0, sum(w)
vis = [False] * n
result = [False] * n


def backtrack(i):
    global thisw, bestw, r, result
    if i >= n:
        result = vis
        bestw = thisw
        return
    r -= w[i]
    if thisw + w[i] <= c1:
        vis[i] = True
        thisw += w[i]
        backtrack(i + 1)
        thisw -= w[i]
    if thisw + r > bestw:
        vis[i] = False
        backtrack(i + 1)
    r -= w[i]


def printf(n):
    for i in range(n):
        if result[i]:
            print(f'将第{i + 1}个物品放入c1中')
        else:
            print(f'将第{i + 1}个物品放入c2中')


def solve(n):
    sumw = 0
    for i in range(n):
        if not result[i]:
            sumw += w[i]
    if sumw <= c2:
        return True
    return False


backtrack(0)
if solve(n):
    printf(n)
