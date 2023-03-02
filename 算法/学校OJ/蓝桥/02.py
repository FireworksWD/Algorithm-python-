time = eval(input())
time = time // 1000
s = time % 60
min = (time - s) / 60 % 60
h = ((time - s) / 60 // 60 - min) % 24
def pr(n):
	n=int(n)
	if n >= 0 and n <= 9:
		n = str(0) + str(n)
	else:
		n = str(n)
	return n
print(pr(h)+':'+pr(min)+':'+pr(s))
