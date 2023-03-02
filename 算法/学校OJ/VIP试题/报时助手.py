Time = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
        '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve',
        '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', 
        '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty'}
nowtime = list(map(int, input().split()))  # 输入h,m添加到列表nowtime
for i in range(len(nowtime)):
    if nowtime[1] == 0:  # 当输入的m==0时
        if nowtime[i] <= 20 or nowtime[i] % 10 == 0:
            print(Time[str(nowtime[i])] + " o'clock")
        else:
            print(Time[str(nowtime[i] - nowtime[i] % 10)] + ' ' + Time[str(nowtime[i] % 10)], end=' ' + " o'clock")
        break
    elif nowtime[i] <= 20 or nowtime[i] % 10 == 0:
        print(Time[str(nowtime[i])], end=' ')
    else:
        print(Time[str(nowtime[i] - nowtime[i] % 10)] + ' ' + Time[str(nowtime[i] % 10)], end=' ')
