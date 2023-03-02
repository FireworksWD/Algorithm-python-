from collections import defaultdict
n = int(input())
board = []
for i in range(n):
    board.append(input().split())
col1 = defaultdict(bool)
dia11 = defaultdict(bool)
dia21 = defaultdict(bool)
col2 = defaultdict(bool)
dia12 = defaultdict(bool)
dia22 = defaultdict(bool)
count = 0
def dfs2(index):
    global count
    if index == n:
        count += 1
        return
    for j in range(n):
        if not col2[j] and not dia12[index + j] and not dia22[index - j] and board[index][j] == "1":
            col2[j] = True
            dia12[index + j] = True
            dia22[index - j] = True
            board[index][j] = "0"
            dfs2(index + 1)
            col2[j] = False
            dia12[index + j] = False
            dia22[index - j] = False
            board[index][j] = "1"
    return 0
def dfs1(index):
    if n <= 0:
        return 0
    if index == n:
        dfs2(0)
        return
    for j in range(n):
        if not col1[j] and not dia11[index + j] and not dia21[index - j] and board[index][j] == "1":
            col1[j] = True
            dia11[index + j] = True
            dia21[index - j] = True
            board[index][j] = "0"
            dfs1(index + 1)
            col1[j] = False
            dia11[index + j] = False
            dia21[index - j] = False
            board[index][j] = "1"
    return 0
dfs1(0)
print(count)