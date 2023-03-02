n = int(input())
a = list(map(int, input().split()))
T = int(input())
b = [0] * n
temp = 0
def printf(y):
    for i in range(y, -1, -1):
        print(b[i], end=' ')
    print()
def check(x, y, num):
    global temp
    if x < 0: return
    check(x - 1, y, num)
    b[y] = a[x]
    num += a[x]
    if num == T:
        temp += 1
        printf(y)
    check(x - 1, y + 1, num)
check(n - 1, 0, 0)
print(temp)
