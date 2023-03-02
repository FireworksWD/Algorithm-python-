'''给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 '''

target = int(input('输入目标整数:'))
candidates = list(map(int, input('输入数组:').split()))
res = []
length = len(candidates)


def backtrack(begin, path, result):
    if result == 0:
        res.append(path[:])
        return
    for index in range(begin, length):
        if candidates[index] > result:
            break
        if index > begin and candidates[index - 1] == candidates[index]:
            continue
        path.append(candidates[index])
        backtrack(index + 1, path, result - candidates[index])
        path.pop()


candidates.sort()
backtrack(0, [], target)
print(res)
