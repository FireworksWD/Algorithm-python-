ans=0
def queen(A, cur=0):
    global ans
    if cur == len(A):
        ans+=1
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)
n = int(input())
queen([None] * n)
print(ans)