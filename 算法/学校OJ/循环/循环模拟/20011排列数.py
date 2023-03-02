import itertools
n=int(input())
temp=0
s=[i for i in range(10)]
for x in itertools.permutations(s):
    temp+=1
    l=list(x)
    if temp==n:
        for i in l:
            print(i,end='')
        break