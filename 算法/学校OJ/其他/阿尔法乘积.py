n=int(input())
def check(n):
    if n<10:
        print(n)
        return
    else:
        t=1
        while n!=0:
            if n%10!=0:
                t*=n%10
                n//=10
            else:n//=10
        return check(t)
check(n)