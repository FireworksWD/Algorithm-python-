import collections

s = input().strip()
res = list(collections.Counter(s).values())
res.sort(reverse=False)
print(res[-1] - res[0])
