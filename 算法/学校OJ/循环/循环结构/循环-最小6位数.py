for i in range(9):
    for j in range(9):
        for k in range(9):
            if i!=j and i!=k and j!=k:
                s=int('947'+str(i)+str(j)+str(k))
                if s%2==0 and s%3==0 and s%5==0:
                    print(s)
                    break