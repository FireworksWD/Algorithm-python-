a, b, c, d, e, f = map(int, input().split())
x = (c * e - b * f) // (a * e - d * b)
y = (c - a * x) // b
print(f'{x} {y}')
