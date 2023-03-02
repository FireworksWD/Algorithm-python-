a = int(input('输入整数'))
if 0 <= a <= 2147483647:
    s = hex(a).upper()
    print(s[2:])