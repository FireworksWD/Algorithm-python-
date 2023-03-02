a, b = 1, 3
ans = 0.618034
while True:
    t = round(a / b, 6)
    if t == ans:
        print(f'{a}/{b}')
        break
    c = a + b
    a, b = b, c
