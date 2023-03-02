k, n = map(int, input().split())
x = str(bin(n)[2:][::-1])
ans = 0
for i in range(len(x)):
    tar = int(x[i])
    ans += tar * k ** i
print(ans)
