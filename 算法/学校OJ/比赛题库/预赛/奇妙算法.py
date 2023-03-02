# 奇妙算法
n, k = map(int, input().split())
s = list(str(n))
while k:
    if s[-1] == '0':
        s.pop()
    else:
        s[-1] = str(int(s[-1]) - 1)
    k -= 1
print(''.join(s))