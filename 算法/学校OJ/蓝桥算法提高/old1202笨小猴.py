s = input()
t = set(s)


def check(x):
    if x<2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return False
    return True


res = []
for i in t:
    res.append(s.count(i))
ans = max(res) - min(res)
if check(ans):
    print('Lucky Word')
    print(ans)
if not check(ans):
    print("No Answer")
    print(0)
