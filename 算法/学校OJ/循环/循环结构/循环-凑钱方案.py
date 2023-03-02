c=0
for i in range(10):
    for j in range(20):
        for k in range(50):
            for m in range(100):
                if 100*i+50*j+20*k+10*m == 2000:
                    c+=1
print(c)