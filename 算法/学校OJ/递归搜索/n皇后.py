# n = int(input())
ans = 0
n = 8


def check(row, col, res):
    for t in res:
        if abs(t[0] - row) == abs(t[1] - col) or t[0] == row or t[1] == col:
            return False
    return True


def back(row, col, path):
    global ans
    if row == n - 1:
        # print(path[:])
        ans += 1
        return
    if row > n - 1 or col > n - 1:
        return
    for i in range(n):
        if check(row + 1, i, path):
            path.append([row + 1, i])
            back(row + 1, i, path)
            path.pop()


for k in range(n):
    back(0, k, [[0, k]])
print(ans)
