'''给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。

回到本题，我们定义递归函数 dfs(target,combine,idx)\textit{dfs}(\textit{target}, \textit{combine},
\textit{idx})dfs(target,combine,idx) 表
示当前在 candidates\textit{candidates}candidates 数组的第 idx\textit{idx}idx 位，
还剩 target\textit{target}target 要组合，
已经组合的列表为 combine\textit{combine}combine。
递归的终止条件为 target≤0\textit{target} \le 0target≤0
或者 candidates\textit{candidates}candidates 数组被全部用完。那
么在当前的函数中，每次我们可以选择跳过不用第 idx\textit{idx}idx 个数，
即执行 dfs(target,combine,idx+1)\textit{dfs}(\textit{target}, \textit{combine},
\textit{idx} + 1)dfs(target,combine,idx+1)。
也可以选择使用第 idx\textit{idx}idx 个数，
即执行 dfs(target−candidates[idx],combine,idx)\textit{dfs}(\textit{target} - \textit{candidates}[\textit{idx}],
\textit{combine}, \textit{idx})dfs(target−candidates[idx],combine,idx)，
注意到每个数字可以被无限制重复选取，因此搜索的下标仍为 idx\textit{idx}idx。
'''

target = int(input('输入目标整数：'))
candidates = list(map(int, input('输入数组：').split()))
path = []
result = []
length = len(candidates)


def dfs(candidates, begin, length, path, result, target):
    if target < 0:
        return
    if target == 0:
        result.append(path)
    for index in range(begin, length):
        dfs(candidates, index, length, path + [candidates[index]], result, target - candidates[index])


dfs(candidates, 0, length, path, result, target)
print(result)


# target = int(input('输入目标整数：'))
# candidates = list(map(int, input('输入数组：').split()))
# path = []
# result = []
# length = len(candidates)
#
#
# def backtrack(candidates, path, target, result, index):
#     if index == length:
#         return
#     if target < 0:
#         return
#     if target == 0:
#         result.append(path[:])
#     backtrack(candidates, path, target, result, index + 1)
#     if target - candidates[index] >= 0:
#         path.append(candidates[index])
#         backtrack(candidates, path, target - candidates[index], result, index)
#         path.pop()
#
# backtrack(candidates, path, target, result, 0)
# print(result)
