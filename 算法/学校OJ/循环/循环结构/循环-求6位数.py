for i in range(9):
    for j in range(9):
        if int('20'+str(i)+str(j)+'08')%99==0:
            print(i,end='')
            print(j)