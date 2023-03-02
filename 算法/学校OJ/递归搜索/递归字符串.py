n = int(input())
s = 'A'
x = ''
for i in range(1, n):
    x = s
    s += chr(ord('A') + i)
    s += x
print(s)
