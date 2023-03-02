s = '202020020020202002020' \
    '202020202020202020202' \
    '202020202020220202020' \
    '200020002020222000220' \
    '200220020020202020022' \
    '202222000000020002000' \
    '202000200020202020202' \
    '002000000022020200020' \
    '000002002220000002020'
data = []
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(s)
with open('data.txt', 'r') as fp:
    for i in fp:
        i = list(i.strip())
        data.append(i)
def check(s):
    return s == '2020'
m, n = len(data), len(data[0])
c = 0
for i in range(m):
    for j in range(n):
        if i + 3 < m and check(data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]):
            c += 1
        if j + 3 < n and check(data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3]):
            c += 1
        if i + 3 < m and j + 3 < n and check(data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]):
            c += 1
print(c)
