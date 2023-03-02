def count(index,n):                    #index: 当前正在统计的数字
    num, low, temp, copyn = 0,0,1,n    #temp:当前位数, low: 当前位数以下的数, num = 统计数字index的个数
    if(index):
        while(n):
            if(n%10 > index):          #由高位决定当前位数的index出现的次数
                num += (n//10 +1)*temp
            elif(n%10 < index):
                num += (n//10)*temp
            else:
                num += (n//10)*temp + low+1   #不仅由高位决定index出现的次数，还有低位决定
            temp *= 10
            low = copyn % temp
            n //= 10
    else:
        while(n):
            if(n%10 == 0):    #由高位和低位决定
                 num += (n//10-1)*temp + low+1
            else:             #仅由高位决定
                num += (n//10)*temp
            temp *= 10
            low = (copyn % temp)
            n //= 10
    return num
n = int(input('请输入页码：'))
for i in range(10):
    print(count(i,n))