a1 = list(map(int, input().split()))
n, c = a1[0], a1[1]
bag = []
for i in range(2, len(a1), 2):
    weight, price = a1[i], a1[i + 1]
    bag.append([weight, price])
tall_value = 0
bag.sort(key=lambda x: x[0] / x[1], reverse=True)
for i, [weight, price] in enumerate(bag):
    if c >= weight:
        tall_value += price
        c -= weight
    else:
        tall_value += c / weight * price
print(int(tall_value))
