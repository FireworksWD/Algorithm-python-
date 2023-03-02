n = int(input())
s = list(map(int, input().split()))
s.sort()
for i in range(n - 2):
    if s[i] + s[i + 1] > s[i + 2] and s[i] + s[i + 2] > s[i + 1] and s[i + 1] + s[i + 2] > s[i]:
        print(s[i], s[i + 1], s[i + 2])
        break
else:
    print("No solution")
