# 需要记录每个数可以使用的数,然后将其存入一个数组中，然后依次进行dfs() 这种博弈论的题目都可以用dfs来解出
from collections import defaultdict

def dfs(value):
    global now
    for i in range(len(table[value]) - 1, -1, -1):
        temp = table[value][i]
        if now[temp] > 0:
            now[temp] -= 1  # 首先去掉一张纸牌
            t = dfs(temp)
            now[temp] += 1  # 把原来的纸牌给补充回来
            if t:  # 说明下个状态时胜的，所以就返回1表示会输
                return False  #
    return True  # 如果这个状态一定是正确的


temp = list(map(int, input().split()))  # 输入剩余所有卡片
now = [0 for i in range(101)]  #
table = defaultdict(list)  # 记录约数和倍数
for i in temp:
    now[i] += 1  # 计算有多少张卡牌
for i in range(1, 101):
    if now[i]:
        for j in range(1, 101):
            if now[j] and (j % i == 0 or i % j == 0):
                table[i].append(j)
choose = list(map(int, input().split()))  # 现在可以选的卡片
choose.sort()
flag = 0
for i in choose:
    now[i] -= 1
    if dfs(i):
        print(i)
        flag = 1
        break
    now[i] += 1
if flag == 0:
    print(-1)
