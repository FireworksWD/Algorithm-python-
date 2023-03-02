n, k = map(int, input().split())
s = list(str(n))
length = len(s) - 1
for i in range(k):
    f = True
    for j in range(length):
        if int(s[j]) > int(s[j + 1]):
            for k in range(j, length):
                s[k] = s[k + 1]
            f = False
            length -= 1
            break
    if f:
        length -= 1
for i in range(length+1):
    print(s[i], end='')