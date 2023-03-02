# n 皇后
'''n = int(input())
board = [0] * n
cnt = 0
def check(board, x, y):
    for i in range(x):
        if abs(board[i] - y) == 0 or abs(board[i] - y) == abs(i - x):
            return False
    return True
def dfs(i):
    global cnt
    if i == n:
        cnt += 1
        print(f'第{cnt}个皇后的坐标:')
        for i in range(n):
            print((i,board[i]),end=' ')
        print()
        return
    for j in range(n):
        if check(board, i, j):
            board[i] = j
            dfs(i+1)
dfs(0)
print(cnt)'''

''' 数组最大值
list_1=list(map(int,input().split()))
max_data1,max_data2=0,2
for i in range(len(list_1)):
    if list_1[i]>max_data1:
        max_data1=list_1[i]
print(f'非递归最大值:{max_data1}')
def back(i):
    global max_data2
    if i==len(list_1):
        print(f'递归最大值:{max_data2}')
        return
    if list_1[i]>max_data2:
        max_data2=list_1[i]
    back(i+1)
back(0)
'''

'''分巧克力
n,k=map(int,input().split())
bag=[list(map(int,input().split())) for _ in range(n)]
left,right=1,100000
result=0
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(n):
        cnt+=(bag[i][0]//mid)*(bag[i][1]//mid)
    if cnt>=k:
        left+=1
        result=mid
    else:
        right-=1
print(result)'''

'''n=int(input())
dress=[list(map(int,input().split())) for _ in range(n)]
dress.insert(0,[0,0])
result=[0]*(n+1)
maxdress=0
for i in range(1,n+1):
    k=0
    for j in range(1,n+1):
        if dress[j][0]<dress[i][0] and dress[j][1]<dress[i][1]:
            k+=1
    result[i]=k
    if result[i]>=result[maxdress]:
        maxdress=i
print(maxdress)'''

def ch(k):
    s=set()
    for i in range(2,k//2+1):
        if k%i==0:
          s.add(i)
    return len(s)+2
res=0
for i in range(1000,1000000):
    if ch(i)==100:
        res=i
        break
print(res)


















