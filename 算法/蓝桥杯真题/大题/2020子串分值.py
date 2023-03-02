word = input()
sum = 0
for i in range(len(word)):
    t = word.rfind(word[i], 0, i)
    key = word[i]
    right = 1
    left = i - t
    a = i + 1
    while a < len(word) and word[a] != word[i]:
        right += 1
        a = a + 1
    sum += left * right
print(sum)
