n = int(input())
h = [0]*1001
h[1] = 1
for i in range(2, n + 1):
    h[i] = h[i - 1]
    if i % 2 == 0:
        h[i] = h[i - 1] + h[i // 2]
print(h[n])
