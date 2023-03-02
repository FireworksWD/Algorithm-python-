def An(n, i=1):
    if i == n:
        return 'sin('+str(i)+')'
    else:
        if i % 2 == 0:
            s = '+'
        else:
            s = '-'
        return 'sin('+str(i)+s+An(n, i+1)+')'
def Sn(m, i=1):
    if m == i:
        return An(m)+'+'+str(i)
    else:
        return '('+Sn(m-1, i+1)+')'+An(m)+'+'+str(i)
print(Sn(int(input())))