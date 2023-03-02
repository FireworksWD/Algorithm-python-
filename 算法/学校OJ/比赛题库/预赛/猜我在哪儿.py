x1 = list(map(int, input().split()))
n = x1[0]
a = x1[1:]
maxi = a.index(max(a))
mini = a.index(min(a))
print(f'{maxi} {mini}')
