board=[[0]*1025for i in range(1026)]
tile=0
def chessboard(tr,tc,dr,dc,size):
    global tile
    if size==1:
        return
    tile+=1
    t=tile
    s=size//2
    if dr<tr+s and dc<tc+s:
        chessboard(tr, tc, dr, dc, s)
    else:
        board[tr+s-1][tc+s-1]=t
        chessboard(tr,tc,tr+s-1,tc+s-1,s)
    if dr<tr+s and dc>=tc+s:
        chessboard(tr,tc+s,dr,dc,s)
    else:
        board[tr+s-1][tc+s]=t
        chessboard(tr,tc+s,tr+s-1,tc+s,s)
    if dr>=tr+s and dc<tc+s:
        chessboard(tr+s,tc,dr,dc,s)
    else:
        board[tr+s][tc+s-1]=t
        chessboard(tr+s,tc,tr+s,tc+s-1,s)
    if dr>=tr+s and dc>=tc+s:
        chessboard(tr+s,tc+s,dr,dc,s)
    else:
        board[tr+s][tc+s]=t
        chessboard(tr+s,tc+s,tr+s,tc+s,s)
x,y,k=map(int,input().split())
size=2**k
chessboard(0,0,x,y,size)
for i in range(size):
    for j in range(size):
        print('%4d'%board[i][j],end='  ')
    print('\n')