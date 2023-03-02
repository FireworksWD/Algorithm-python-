'''给定若干个字符串，不定数量，每行一个。有些字符串可能出现了多次。如果读入一个字符串后，发现这个字符串以前被读入过，则这个字符串被称为前面相同的字符串的复读，这个字符串被称为复读字符串。相应的，每个首次出现的字符串就是非复读字符串。

举个例子，

abc
def
abc
abc
abc
第 1,3,4,51,3,4,5 行是字符串 abc，那么 3,4,53,4,5 行的字符串会被称为“复读”。

请你把所有的非复读字符串，按照行号从小到大的顺序，依次拼接为一个长串并输出。'''
temp = []
while True:
    s = input()
    if s == '0':
        break
    temp.append(s)
res = []
res.append(temp[0])
for i in range(1, len(temp)):
    if temp[i] in res:
        continue
    res.append(temp[i])
print(''.join(res))
