def Receive_data(n, matrix):
    for i in range(n):
        row = input().split()
        for j in range(n):
            matrix[i].append(int(row[j]))
    return matrix


# 定义矩阵的幂
def matrix_power(matrix, n, m):
    result_temp = matrix  # 临时存放每次相乘的数据
    m -= 1
    while m != 0:
        result = [[0 for _ in range(n)] for _ in range(n)]  # 创建新的二维列表存放结果 注意不能创建空列表，否则会出现result列表index越界
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += result_temp[i][k] * matrix[k][j]
        m -= 1
        result_temp = result
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n)]  # 创建二维列表
    matrix = Receive_data(n, matrix)
    if m != 0:
        result = matrix_power(matrix, n, m)
    else:
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            result[i][i] = 1

    # print(matrix_power(matrix,n,m))
    # 按照格式输出
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=' ')
        print()