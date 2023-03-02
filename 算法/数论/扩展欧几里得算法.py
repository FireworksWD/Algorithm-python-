'''给定n对正整数ai,bi，对于每对数，求出一组xi,y，使其满足ai∗xi+bi∗yi=gcd(ai,bi)。
输入格式
第一行包含整数n。
接下来n行，每行包含两个整数ai,bi。
输出格式
输出共n行，对于每组ai,bi，求出一组满足条件的xi,yi，每组结果占一行。
本题答案不唯一，输出任意满足条件的xi,yi均可。
数据范围
1≤n≤10^5
1≤ai,bi≤2∗10^9
输入：
2
4 6
8 18
输出：
-1 1
-2 1
'''
n = int(input())
x, y = 1, 0


def exgcd(a, b):
    global x, y
    if b == 0:
        x, y = 1, 0
        return a
    d = exgcd(b, a % b)
    x, y = y, x
    y -= (a // b) * x
    return d


for _ in range(n):
    a, b = map(int, input().split())
    exgcd(a, b)
    print(x, y)