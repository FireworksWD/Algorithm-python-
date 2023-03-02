'''def digits(n):
    if n<5 and n > 0:
        return 0
    else:
        k=n//5
        return k+digits(k)
print(digits(int(input())))'''
m=3
n=3
map_int = [[0] * (m + 1)]
for i in range(1, n + 1):
    map_int.append([0] * (m + 1))
    nums = input()
    nums = "0" + nums
    for j in range(0, m + 1):
        map_int[i][j] = ord(nums[j]) - 48
print(map_int)