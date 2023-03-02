# a = [True] * 20210606
# b = []
# for i in range(2, 20210606):
#     if a[i]: b.append(i)
#     for j in b:
#         if i * j >= 20210606:
#             break
#         a[i * j] = False
#         if i % j == 0:
#             break
#
#
# def check(x):
#     while x:
#         if x % 10 in [1, 4, 0, 6, 8, 9]:
#             return False
#         x //= 10
#     return True
#
#
# ans = 0
# for i in b:
#     if check(i):
#         ans += 1
# print(ans)
print(1903)
