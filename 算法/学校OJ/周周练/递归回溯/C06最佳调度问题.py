a1=list(map(int,input().split()))
n, k = a1[0],a1[1]
path = [0] * 100
list_1 = a1[1:]
list_1.insert(0, 0)
max_num = 1000000


def dfs(t):
    global max_num
    if t > n:
        temp = 0
        for i in range(1, k + 1):
            if path[i] > temp:
                temp = path[i]
        if temp < max_num:
            max_num = temp
        return
    else:
        for i in range(1, k + 1):
            path[i] += list_1[t]
            if path[i] < max_num:
                dfs(t + 1)
            path[i] -= list_1[t]


dfs(1)
print(max_num)
