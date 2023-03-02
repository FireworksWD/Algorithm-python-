n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)


def move(a, n):
    t = a[n]
    for i in range(n - 1, 0, -1):
        if t < a[i]:
            a[i + 1] = a[i]
            print('  Move back:',end=' ')
            for j in range(1, n + 1):
                print(a[j], end=' ')
            print()
            a[i] = t


for i in range(1, n + 1):
    print(f'Insert element[{i}]:', end='  ')
    print()
    print('  Init:',end='')
    for j in range(1, i + 1):
        print(a[j], end=' ')
    print()
    move(a, i)
    print('  Final:', end='')
    for j in range(1, i + 1):
        print(a[j],end=' ')
    print()
