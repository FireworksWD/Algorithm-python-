n, m = map(int, input().split())
nodeL = [dict() for i in range(n)]  # 列表nodeL的元素为字典，第 i 个字典中的键值对表示点 i+1 到key的距离为value
disL = [100000 for _ in range(n)]  # 记录点1到点 i（i>=1）的距离，将初始值设为极大
disL[0] = 0  # 点1到它本身的距离为0
for i in range(m):
    u, v, l = map(int, input().split())
    nodeL[u - 1][v] = l  # 点 u 到点 v 的距离为 l
queue = [1]
while len(queue) > 0:
    Next = queue.pop(0)  # 弹出队首的元素
    Dict = nodeL[Next - 1]  # 查看所弹出元素可到达的节点有哪些
    L = Dict.keys()
    for item in L:
        newdis = disL[Next - 1] + Dict[item]  # 经由节点Next到节点item的新距离
        if newdis < disL[item - 1]:
            disL[item - 1] = newdis
            queue.append(item)
for i in range(1, len(disL)):
    print(disL[i])