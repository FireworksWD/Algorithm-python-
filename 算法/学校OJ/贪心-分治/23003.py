al = list(map(int, input().split()))
n, c = al[0], al[1]
w = al[2:]
w.sort()
res = 0
i, j = 0, len(w)-1
while i <= j:
    if i != j and w[i]+w[j] > c:
        res += 1
        j -= 1
    else:
        res += 1
        i += 1
        j -= 1
print(res)
