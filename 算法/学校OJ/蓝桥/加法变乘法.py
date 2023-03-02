for i in range(1,48):
    for j in range(i+2,49):
        s1=1225-i-(i+1)-j-(j+1)
        s2=2015-i*(i+1)-j*(j+1)
        if s1==s2:
            print(i)
