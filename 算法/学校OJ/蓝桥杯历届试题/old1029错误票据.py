N = int(input())
b = [0] * 100001
bag = []
m = n = 0
for i in range(N):
    x = list(map(int, input().split()))
    for value in x:
        b[value] += 1
        bag.append(value)
bag.sort()
# print(bag)
for i in range(bag[0], bag[len(bag) - 1] + 1):
    if b[i] == 0:
        m = i
    if b[i] > 1:
        n = i
print(m, n)
