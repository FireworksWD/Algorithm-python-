'''超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m=len(primes)
        point=[0]*m
        sums=[1]*m
        dp=[0]*(n+1)
        for i in range(1,n+1):
            min_x=min(sums)
            dp[i]=min_x
            for j in range(m):
                if min_x==sums[j]:
                    point[j]+=1
                    sums[j]=dp[point[j]]*primes[j]
        return dp[-1]