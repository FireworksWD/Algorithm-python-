left = 0
s = input()


def dfs():
    global left  # 单指针遍历整个字符串
    ans, temp = 0, 0
    while left < len(s):
        if s[left] == '(':
            left += 1
            temp += dfs()
        elif s[left] == 'x':
            left += 1
            temp += 1
        elif s[left] == '|':
            left += 1
            ans = max(ans, temp)
            temp = 0
        elif s[left] == ')':
            left += 1
            ans = max(ans, temp)
            return ans
    ans = max(ans, temp)  # 考虑特殊情况：xx|xxx
    return ans


print(dfs())
