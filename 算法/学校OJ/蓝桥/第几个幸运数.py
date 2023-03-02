'''n = int(input())
def is_lucky(num):
    while num != 1:
        for i in [3, 5, 7]:
            if num % i == 0:
                num = num // i
                break
        else:
            return False
    return True
ans = 0
for i in range(2, n+1):
    if is_lucky(i):
        ans += 1
print(ans)'''
MAX = int(input())
a = [3, 5, 7]
s = set()
tou = 1
while True:
    for i in a:
       t = tou * i
       if t <= MAX:
        s.add(t)
    lst = sorted(s)
    for i in lst:
        if i > tou:
            tou = i
            break
    if tou >= MAX:
        break
print(len(s))