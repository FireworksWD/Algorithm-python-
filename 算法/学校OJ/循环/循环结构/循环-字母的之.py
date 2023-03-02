for i in range(9):
    for j in range(9):
        for k in range(9):
            if i!=j!=k:
                if int(str(i)*3) + int(str(j)*3) + int(str(k)*3) == int(str(k)+str(j)*2+str(k)):
                    print(i, end=' ')
                    print(j, end=' ')
                    print(k)