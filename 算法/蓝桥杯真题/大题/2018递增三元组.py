import bisect

# N = int(input())
# A = sorted(list(map(int, input().split())))
# B = sorted(list(map(int, input().split())))
# C = sorted(list(map(int, input().split())))

al = list(map(int, input().split()))
N = al[0]
A = sorted(al[1:N + 1])
B = sorted(al[N + 1:2 * N + 1])
C = sorted(al[2 * N + 1:])
res = 0
# print(A,B,C)
# 对 b 遍历 分别检索 a, c
for i in range(N):
    ia = bisect.bisect_left(A, B[i])
    ib = N - bisect.bisect_right(C, B[i])
    res += ia * ib

print(res)
