n = int(input())

pal = list(input())

count = flag = 0  # count计数，flag判断是否已经有一个单独的奇个数的字符了

m = n - 1

for i in range(m):  # 从头遍历到倒数第二个字符
    for k in range(m, i - 1, -1):  # 从后面往前一直到i寻找和pal[i]相同的pal[k]
        if k == i:  # 如果找不到相同的
            if n % 2 == 0 or flag == 1:  # impossible的两种情况
                print('Impossible')
                exit()
            flag = 1
            count += int(n / 2) - i
        elif pal[k] == pal[i]:
            for j in range(k, m):  # 找到相同的，进行交换
                pal[j], pal[j + 1] = pal[j + 1], pal[j]
                count += 1  # 计数器加1
            m -= 1  # 最后拍好序的不在进行比较
            break

print(count)
