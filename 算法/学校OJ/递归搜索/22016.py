all_n1 = list(map(int, input().split()))
n, M, m = all_n1[0], all_n1[1], all_n1[2]
all_n = all_n1[3:]
a = [[0] * 100 for _ in range(100)]
x = [0] * 100
ans = 0
for i in range(0, len(all_n), 2):
    u, v = all_n[i], all_n[i + 1]
    a[u][v] = 1
    a[v][u] = 1


def check(k, c):
    for y in range(1, k):
        if a[k][y] == 1 and c == x[y]:
            return False
    return True


def backtrack(t):
    global ans
    if t > n:
        ans += 1
        return
    for j in range(1, m + 1):
        x[t] = j
        if check(t, j):
            backtrack(t + 1)
        x[t] = 0


backtrack(1)
print(ans)
