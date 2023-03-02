N, Q = map(int, input().split())
a = list(map(int, input().split()))
op = [0 for _ in range(N + 1)]
for _ in range(Q):
    l, r, x = map(int, input().split())
    op[l - 1] += x
    op[r] -= x

for i in range(1, N):
    op[i] += op[i - 1]
# print(' '.join(str(max(a[i] + op[i], 0)) for i in range(N)))

for i in range(N):
    print(max(a[i] + op[i], 0), end=" ")
