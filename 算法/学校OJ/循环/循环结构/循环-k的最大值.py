s=0
for i in range(1,1000):
    s+=i
    if s==2006:
        print(i)
        break
    else:
        print('error')