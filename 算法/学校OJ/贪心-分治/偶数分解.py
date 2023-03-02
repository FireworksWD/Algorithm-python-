from math import sqrt
def isPrime(num):
    flag = True
    if num == 2 or num == 3:
        flag = True
    if num % 6 != 1 and num % 6 != 5:
        flag = False
    else:
        sqrt_num = int(sqrt(num)) + 1
        for x in range(5, sqrt_num, 6):
            if num % x == 0 or num % (x + 2) == 0:
                flag = False
                break
            flag = True
    return flag
def main(n):
    a=[]
    for i in range(2,n//2+1):
        if isPrime(i) and isPrime(n-i):
            x=abs(n-2*i)
            a.append([x,i,n-i])
    a.sort(reverse=False,key=lambda x:x[0])
    print(a[0][1],end=' ')
    print(a[0][2])
n=int(input())
main(n)