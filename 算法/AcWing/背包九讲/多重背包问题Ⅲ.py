N, V = map(int, input().split())
dp = [0]*(V+1)
for _ in range(N):
    v, w, s = map(int, input().split())
    for c in range(v):
        queue = []
        hh, tt = 0, -1
        times = (V-c) // v
        for k in range(times+1):
            curr = dp[k*v+c] - k*w
            if hh <= tt and queue[hh][0] == k-s-1:
                hh += 1
            while hh <= tt and queue[-1][1] < curr:
                queue.pop()
                tt -= 1
            queue.append([k, curr])
            tt += 1
            dp[k*v+c] = queue[hh][1] + k*w
print(dp[V])