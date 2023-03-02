n = int(input())
st = [True]*(n+1)
cnt = 0
primes = []
for i in range(2, n+1):
    if st[i]:
        cnt += 1
        primes.append(i)
    for p in primes:
        if p > n//i: break
        st[p*i] = False
        if i % p == 0: break # i是p的倍数，就不用再继续了
print(cnt)
print(primes)