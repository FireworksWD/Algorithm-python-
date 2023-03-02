wide = 2019
high = 324
count = 0  # 计数
while wide != high:
    wide = wide - high
    if wide < high:
        wide, high = high, wide  # wide, high交换
    count += 1
print(count + 1)
