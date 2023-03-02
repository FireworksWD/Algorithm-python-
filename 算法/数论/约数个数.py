'''给定n个正整数aiai，请你输出这些数的乘积的约数个数，答案对109+7109+7取模。
输入格式
第一行包含整数n。
接下来n行，每行包含一个整数aiai。
输出格式
输出一个整数，表示所给正整数的乘积的约数个数，答案需对109+7109+7取模。
数据范围
1≤n≤100
1≤ai≤2∗10^9
输入：
3
2
6
8
输出：
12
'''
n = int(input())
from collections import defaultdict

dict = defaultdict(int)


def divide(a):
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            dict[i] += 1
            a //= i
    if a > 1: dict[a] += 1


for _ in range(n):
    a = int(input())
    divide(a)

res = 1
for key, value in dict.items():
    res = res * (value + 1) % int(1e9 + 7)
print(res)