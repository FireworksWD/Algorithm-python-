import itertools
n=int(input())
s=['A','C','M']
for i in itertools.permutations(s,n):
    print(i)