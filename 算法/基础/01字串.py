for i in range(0, 32):
    a = bin(i)[2:]
    a = '0000' + a
    print(a[-5:])