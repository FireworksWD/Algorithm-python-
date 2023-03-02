import sys

sys.setrecursionlimit(100000)
N = int(input())
# 下标结点，tree[i][0]为其父节点，其余为孩子结点
tree = [[-1] for _ in range(N+1)]
for i in range(2, N+1):
    fa = int(input().strip())
    tree[i][0] = fa
    tree[fa].append(i)


def getHigh(node):
    # 叶子结点
    if len(tree[node]) == 1:
        # dp[node] = 0
        return 0
    # 最高高度为其孩子结点数+最高的孩子树的高度
    # 求最高孩子树高度
    maxhigh = 0
    for j in range(1, len(tree[node])):
        maxhigh = max(maxhigh, getHigh(tree[node][j]))
    return len(tree[node])-1+maxhigh


print(getHigh(1))
