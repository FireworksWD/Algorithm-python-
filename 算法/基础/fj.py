n = int(input())

str_n = ''

for i in range(n):
    str_n = str_n + chr(ord('A') + i) + str_n

print(str_n)
