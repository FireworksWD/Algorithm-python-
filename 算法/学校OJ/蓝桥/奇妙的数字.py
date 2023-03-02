for i in range(1, 100):
    s1=list(str(i*i))
    s2=list(str(i*i*i))
    s3=s1+s2
    s3.sort()
    a=['0','1','2','3','4','5','6','7','8','9']
    if s3==a:
        print(i)
