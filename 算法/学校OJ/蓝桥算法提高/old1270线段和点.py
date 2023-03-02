def f(n, m):
    A = [0 for i in range(n)]
    for i in range(n):
        A[i] = int(input())
    A.sort()  # A点集排序
    B = [[0, 0] for i in range(m)]
    for i in range(m):
        B[i][0], B[i][1] = map(int, input().strip().split())
    B = sorted(B, key=lambda x: (x[0], -x[1]))  # B区间排序

    start = 0  # 定位推进区间
    ans = 0
    while start < m:
        max_num = 0
        max_index = 0
        for i in range(len(A)):  # 寻找使得start最接近m的点
            temp = start
            while temp < m:
                if B[temp][0] <= A[i] <= B[temp][1]:
                    temp = temp + 1
                else:
                    break
            if temp > max_num:  # 记录该点的下标和区间
                max_num = temp
                max_index = i
        start = max_num  # 更新start
        del (A[max_index])  # 删除该点
        ans = ans + 1
        if len(A) == 0:
            break

    if start == m:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    f(n, m)
