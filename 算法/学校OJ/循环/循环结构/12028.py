n = int(input())
res = 0


# def check(k):
#     f = True
#     while k:
#         t = k % 10
#         if t == 7:
#             f = False
#             break
#         k //= 10
#     return f
#

for i in range(1, n + 1):
    if i % 7 == 0 or 7 in [int(j) for j in str(i)]:
        continue
    else:
        res += i ** 2
print(res)
