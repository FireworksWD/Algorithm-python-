d = {'1':'yi', '2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
n = input().strip()#str.strip()就是把这个字符串头和尾的空格，以及位于头尾的\n \t之类给删掉
a = []
b = [] #b存的是逆序的读法，最后再逆序输出即为结果
def numexchange(i):
    i = i[::-1]
    for j in range(len(i)):
        if j == 0:
            if i[j]!='0':
                b.append(d[i[j]])
        elif j == 1:
            if i[j]=='0'  and  i[0]!='0':
                b.append(d['0'])
            elif i[j] == '1' and len(i)==2:
                b.append('shi')
            elif i[j]!='0':
                b.append('shi')
                b.append(d[i[j]])
        elif j == 2:
            if i[j]=='0'  and i[1]!='0':
                b.append(d['0'])
            elif i[j]!='0':
                b.append('bai')
                b.append(d[i[j]])
        elif j == 3:
            if  i[j]!='0':
                b.append('qian')
                b.append(d[i[j]])
            elif i[j]=='0'  and i[2]!='0':
                b.append(d['0'])

while n!='':  #倒着读，每四位为一组字符串
    if len(n)>=4:
        s = n[-4:] #取后四位
        n = n[:-4] #删除后四位
        a.append(s)
    else:
        a.append(n)
        n = ''
for i in range(len(a)):
    if i == 0:
        numexchange(a[i])
    elif i == 1:
        b.append('wan')
        numexchange(a[i])
    elif i == 2:
        b.append('yi')
        numexchange(a[i])
for i in range(len(b)-1,-1,-1):
    if i == len(b)-1:
        print(b[i], end='')
    else:
        print(' %s'%(b[i]), end='')
