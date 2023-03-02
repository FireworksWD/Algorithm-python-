n = int(input())
b = list(map(int, input().split()))
c = int(input())
a = 0
for i in range(len(b)):
    if c == b[i]:
        a += 1
        print(i+1)
        break
if a == 0:
    print(-1)