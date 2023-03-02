n = int(input())
s = '0'
for i in range(n):
    t = ''
    for j in s:
        if j == '0':
            t += '1'
        else:
            t += '01'
    s = t
print(s)
