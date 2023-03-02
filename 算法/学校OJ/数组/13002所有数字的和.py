n = int(input())
ans = [] # 存放每一位数字
def back(x):
    if x == 0:
        return
    back(x // 10)
    ans.append(x % 10) # 回溯的思想让数字能够正着存进去
for i in range(1, n + 10): # 保证取的到所以+10
    back(i) # 调用
    if len(ans) >= n: # 如果>=n了就结束循环
        break
# print(ans)
print(sum(ans[:n])) # 1-n之间的和

n = int(input())
s = ''
for i in range(1, n + 1):
    s += str(i)
a = [int(i) for i in s]
# print(a)
print(sum(a[:n]))
