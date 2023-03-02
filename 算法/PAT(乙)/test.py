a = list(map(int, input().split()))
n = int(input())
vis = [i for i in range(1, 7)]
temp = []
while n:
    for num in a:
        temp.append(max(vis.remove(num)))
