j,ans=0,0
for i in range(1,2006):
    ans+=i
    j=i
    if ans>=2006:
        break
print(j-1)