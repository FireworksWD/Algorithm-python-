check = ["kfc", "crazy", "thursday", "vivo", "50"]
t = int(input())
s = []
for i in range(t):
    x = input()
    m = x.lower()
    s.append(m)
for i in s:
    f = True
    for j in check:
        pos = i.find(j)
        if pos == -1:
            f = False
            break
    if f:
        print('yes')
    else:
        print('no')
