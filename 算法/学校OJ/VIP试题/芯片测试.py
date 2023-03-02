n = int(input())
test = []
for i in range(n):
    test.append(list(map(int, (input().split()))))
for i in range(n):
    num = 0
    for j in range(n):
        if test[i][j] == 1:
            num += 1
    if num > n/2:
        print(i+1, end='')