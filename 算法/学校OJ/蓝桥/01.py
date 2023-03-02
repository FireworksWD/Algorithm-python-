import itertools
n=10
a=[str(i) for i in range(n)]
s=""
s=s.join(a)
for i in itertools.permutations(s,n):
    print(''.join(i))
