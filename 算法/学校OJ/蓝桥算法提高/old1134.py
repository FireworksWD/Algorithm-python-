n = sorted(list(input()))
rst = []
solution = []


def back(n, solution, rst):
    if len(n) == 0:
        tmp = ''.join(solution)
        if tmp not in rst:
            rst.append(tmp)
            print(tmp)
        return
    for i in range(len(n)):
        newsolution = solution + [n[i]]
        newarry = n[:i] + n[i + 1:]
        back(newarry, newsolution, rst)


back(n, solution, rst)
