n = int(input())
f = [1, n]
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    for i in range(3, n + 1):
        f.append(abs(f[-1] - f[-2]))
    print(sum(f))
