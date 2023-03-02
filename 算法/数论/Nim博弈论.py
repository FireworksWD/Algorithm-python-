'''有n nn堆石子（n nn > >> 0 00），
每人每次可以从任意一堆石子里，取出任意多枚石子扔掉，可以取完，不能不取，每次只能从一堆里取。最后没有石子可以取的人输掉这场游戏。
设甲为先手，乙为后手，两个人以最佳策略进行操作
'''
n = int(input('输入石头的堆数:'))
a_list = list(map(int, input('输入每堆石头的重量:').split()))
res = 0
for value in a_list:
    res ^= value
# print(res)
if res == 0:
    print('No')  # 先手必败
else:
    print('Yes')  # 先手必胜

# 衍生，只有一堆石头切每次拿的石头数不超过k
# def slove(n):
#    return n%(k+1)