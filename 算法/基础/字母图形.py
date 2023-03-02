m, n = map(int, input().split())
for i in range(m):
    for j in range(n):
        print(chr(65+abs(i-j)), end='')
    print()