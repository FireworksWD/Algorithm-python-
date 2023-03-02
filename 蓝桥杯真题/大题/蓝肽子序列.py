x = input()
y = input()


def change(s, path: list):
    x = ''
    for i in s:
        if 'A' <= i <= 'Z':
            if x != '':
                path.append(x)
            x = ''
        x += i
    path.append(x)
    return path


sa, sb = change(x, []), change(y, [])
lenx, leny = len(sa), len(sb)
dp = [[0] * (leny + 1) for i in range(lenx + 1)]
for i in range(1, lenx + 1):
    for j in range(1, leny + 1):
        if sa[i - 1] == sb[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
