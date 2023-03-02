c = 0
x = []
for i in range(1,100):
    if i%3==0 or i%5==0:
        x.append(i)
        c+=1
for j in x:
    if j%7==0:
        x.remove(j)
print(len(x))