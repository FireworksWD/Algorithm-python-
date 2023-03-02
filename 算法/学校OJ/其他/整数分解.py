list1 = []
for i in range(2022 // 3, 2022):  # i 必须大于2019 / 3
    for j in range(1, i):  # j 比 i小
        k = 2022- i - j
        if k >= j or k <= 0:  # k比j小  或者 k不能小于0
            continue
        list1.append([i, j, k])

# 剔除2 4
list_new1 = []
for i in list1:
    flag = True
    for j in i:
        if "2" in str(j) or "4" in str(j):
            flag = False
            break

    if flag == True:
        list_new1.append(i)

print(len(list_new1))
