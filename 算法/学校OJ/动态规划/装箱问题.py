def main():
    wi,n=int(input()),int(input())
    s=[0]+[int(input())for _ in range(n)]
    dp=[wi for _ in range(wi+1)]
    for i in range(1,n+1):
        for j in range(wi,s[i]-1,-1):
            dp[j]=min(dp[j],dp[j-s[i]]-s[i])
            if dp[j]==0:
                print(0)
                return
    print(dp[-1])
main()