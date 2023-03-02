n = int(input())
nums = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            nums[i][j] = 1
        else:
            nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
        if nums[i][j] != 0:
            print(nums[i][j], end=' ')
    print()