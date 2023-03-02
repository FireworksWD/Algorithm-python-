n = int(input())
a = list(map(int, input().split()))


def select_sort(temp, a, n):
    if temp == n:
        return
    minid = temp
    for i in range(temp + 1, n):
        if a[i] < a[minid]:
            minid = i
    a[temp], a[minid] = a[minid], a[temp]
    print(f'swap(a[{temp}], a[{minid}]):{a[0]}', end=' ')
    for i in range(1, n):
        print(a[i], end=' ')
    print()
    select_sort(temp + 1, a, n)


select_sort(0, a, n)
