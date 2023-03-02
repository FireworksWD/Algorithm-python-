n = int(input())
s = ''
for i in range(1, n + 1):
    s += str(i)
res = [int(i) for i in s]
print(sum(res[0:n]))
