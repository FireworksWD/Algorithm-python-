N = input()
multiple_negative = 1
multiple_even = 1
number2 = 0
digit = len(str(abs(int(N))))
for i in N:
    if i == '2':
        number2 += 1
if int(N) < 0:
    multiple_negative += 0.5
if int(N) % 2 == 0:
    multiple_even += 1
result = number2 / digit * multiple_negative * multiple_even * 100
print("{0:.2f}%".format(result))
