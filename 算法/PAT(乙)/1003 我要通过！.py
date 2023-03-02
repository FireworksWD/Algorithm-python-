import re

n = int(input())
for i in range(n):
    word = input()
    if re.match(r'A*PA+TA*', word):
        temp = re.split(r'[P|T]', word)
        # print(temp)
        if temp[0] * len(temp[1]) == temp[2]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
