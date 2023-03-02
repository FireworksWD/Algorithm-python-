n = int(input())
w = int(input())
price = []
for i in range(n):
    price.append(int(input()))
price.sort()
i, j = 0, n - 1
res = 0
while i <= j:
    if i != j and price[i] + price[j] > w:
        j -= 1
        res += 1
    else:
        i += 1
        j -= 1
        res += 1
print(res)
