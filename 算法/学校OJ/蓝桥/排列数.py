import itertools
n = int(input())
ar = [0,1,2,3,4,5,6,7,8,9]
for i in itertools.permutations(ar):
    print(','.join(i))