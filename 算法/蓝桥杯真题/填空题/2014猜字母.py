s = ''
for i in range(97, 97 + 19):
    s += chr(i)
s *= 106
while len(s) != 1:
    s = s[1::2]
print(*s)
