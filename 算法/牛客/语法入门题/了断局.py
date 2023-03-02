def f(x):
    if x == 1: return 0
    if x == 2 or x == 3: return 1
    f1, f2, f3 = 0, 1, 1
    for i in range(4, x + 1):
        c = f1 + f2 + f3
        f1, f2, f3 = f2, f3, c
    return f3


while True:
    try:
        s = int(input())
        print(f(s))
    except:
        break
