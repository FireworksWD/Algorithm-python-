import collections

s = input()
dit = collections.Counter(s)
max_v, min_v = float('-inf'), float('inf')
for key, value in dit.items():
    max_v = max(max_v, value)
    min_v = min(min_v, value)
print(max_v-min_v)
