a, b, c = map(float, input().split())
t = (b ** 2 - 4 * a * c) ** 0.5
x1 = (-b + t) / (2 * a)
x2 = (-b - t) / (2 * a)
print('%.2f' % (max(x1, x2)), end=' ')
print('%.2f' % (min(x1, x2)))
