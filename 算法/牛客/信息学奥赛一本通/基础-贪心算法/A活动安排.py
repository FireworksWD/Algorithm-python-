'''设有个n活动的集合E={1,2,..,n}，其中每个活动都要求使用同一资源，如演讲会场等，而在同一时间内只有一个活动能使用这一资源。
每个活动i都有一个要求使用该资源的起始时间
，活动i与活动j相容。选择出由互相兼容的活动组成的最大集合。
输入描述:
4
1 3
4 6
2 5
1 7
输出描述:
2
输出互相兼容的最大活动个数。'''
n = int(input())
ti = [list(map(int, input().split())) for i in range(n)]
ti.sort(key=lambda x: x[1])
res = []
res.append(ti[0])
for i in range(1, n):
    if res[-1][1] <= ti[i][0]:
        res.append(ti[i])
print(len(res))
