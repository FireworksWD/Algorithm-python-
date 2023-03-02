w = int(input())
n = int(input())
price = []
for i in range(n):
    price.append(int(input()))
price.sort()
i, j = 0, len(price) - 1
res = 0
while i <= j:
    if price[i] + price[j] <= w:
        i += 1
        j -= 1
        res += 1
    else:
        j -= 1
        res += 1
print(res)
