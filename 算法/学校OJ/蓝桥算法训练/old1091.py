import itertools

n = int(input())
m = int(input())
a = [i for i in range(1, n + 1)]
b = [0] * (n + 1)
t = list(map(int, input().split()))
for i in range(len(t)):
    b[i + 1] = t[i]
b.pop(0)
temp, cout = 0, 0
for i in itertools.permutations(a):
    t = list(i)
    temp += 1
    if t == b:
        cout = temp
        cout += m
    if temp == cout:
        for i in t:
            print(i, end=' ')
        break
