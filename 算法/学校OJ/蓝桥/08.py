n = int(input())
s = n//1000//60//60%60
f = n//1000//60%60
m = n//1000%60
if s<10:
    s='0'+str(s)
if f<10:
    f='0'+str(f)
if m<10:
    m='0'+str(m)
print(s,end=':')
print(f,end=':')
print(m)