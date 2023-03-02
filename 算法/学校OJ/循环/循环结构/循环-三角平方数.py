import math
s=0
for i in range(1,10000):
    s+=i
    for j in range(1000,10000):
        if j==s:
            if math.sqrt(j)==int(math.sqrt(j)):
                print(j)
                break