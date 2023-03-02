n=int(input())
F1,F2=1,1
for i in range(3, n+1):
    F1,F2=F2%10007,(F1+F2)%10007
print(F2)    
