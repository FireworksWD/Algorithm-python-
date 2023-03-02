s = input()
lt = [-1 for i in range(26)]
out = 0
for i in range(len(s)):
    ind = ord(s[i]) - 97
    x = i - lt[ind]
    y = len(s) - i
    out += x * y
    lt[ind] = i
print(out)
