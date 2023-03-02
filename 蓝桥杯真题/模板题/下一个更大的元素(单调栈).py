# 下一个更大的元素(线性)
# 输出[4,2,4,-1,-1]
def stack_():
    s = [2, 1, 2, 4, 3]
    stack = []
    res = [0] * len(s)
    for i in range(len(s) - 1, -1, -1):
        while stack and stack[-1] <= s[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(s[i])
    return res


print(stack_())


# 环形 输出[4,2,4,-1,4]
def stack_2():
    s = [2, 1, 2, 4, 3]
    stack = []
    res = [0] * len(s)
    for i in reversed(range(2 * len(s) - 1)):
        while stack and stack[-1] <= s[i % len(s)]:
            stack.pop()
        res[i % len(s)] = stack[-1] if stack else -1
        stack.append(s[i % len(s)])
    return res


print(stack_2())
