def maxsum(a,left,right):
    if left==right:
        if a[left]>0:
            return a[left]
        else:
            return 0
    mid=(left+right)//2
    maxleftsum=maxsum(a,left,mid)
    maxrightsum=maxsum(a,mid+1,right)
    maxl = 0
    maxbl = 0
    maxr = 0
    maxbr = 0
    for i in range(mid, left - 1, -1):
        maxl += a[i]
        if maxl > maxbl:
            maxbl = maxl
    for j in range(mid + 1, right + 1):
        maxr += a[j]
        if maxr > maxbr:
            maxbr = maxr
    m = maxbl + maxbr
    return max(maxleftsum,maxrightsum,m)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_right=len(a)-1
b_right=len(b)-1
print(maxsum(a,0,a_right))
print(maxsum(b,0,b_right))