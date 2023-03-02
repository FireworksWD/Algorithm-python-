'''给定nn组ai,bi,pi对于每组数据，求出ai^bi mod pi的值。
输入格式
第一行包含整数n
接下来n行，每行包含三个整数ai,bi,pi
输出格式
对于每组数据，输出一个结果，表示ai^bi mod pi的值。
每个结果占一行。
数据范围
1≤n≤100000
1≤ai,bi,pi≤2∗10^9
输入：
2
3 2 5
4 3 9
输出：
4
1
'''


def qmi(a, b, p):
    base = a
    res = 1
    while b:
        if b & 1:
            res = res * base % p
        base = base ** 2 % p
        b >>= 1
    return res


n = int(input())
for _ in range(n):
    a, b, p = map(int, input().split())
    print(qmi(a, b, p))
