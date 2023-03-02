def gcb(a, b):
    return gcb(b, a % b) if b else a


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(gcb(a, b))