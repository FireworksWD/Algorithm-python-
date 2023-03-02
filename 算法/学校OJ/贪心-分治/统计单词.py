a = input().strip().lower()
b = input().lower()  # 考虑到首尾的空格会单词首次出现的位置有影响，在此不能去除
b_list = b.split()
count = 0
first = 0

if a not in b_list:
    print(-1)
else:
    for i in b_list:
        if i == a:
            count += 1
    for j in range(len(b) - len(a)):
        if (b[j:j + len(a)] == a):
            first = j
            # 若单词首次出现在字符串首，则只需判断单词后的字符是否为分隔符（空格）
            if (j == 0) and (b[j + len(a)] == ' '):
                break
            # 若单词在字符串尾才出现，则需要判断单词前的字符是否为分隔符
            elif (j == (len(b) - len(a)) and b[j - 1] == ' '):
                break
            # 若单词出现在字符串中，则需要同时满足单词前后字符均为空格
            elif (j != 0) and (j != len(b) - len(a)) and (b[j - 1] == ' ') and (b[j + len(a)] == ' '):
                break

    print(count, first)
