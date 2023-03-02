n = input()
if n == 'z':
    print('yza')
if n == 'a':
    print('zab')
if n == 'Z':
    print('YZA')
if n == 'A':
     print('ZAB')
if 97 < ord(n) < 122:
    print(chr(ord(n)-1)+n+chr(ord(n)+1))
if 65 < ord(n) < 90:
    print(chr(ord(n) - 1) + n + chr(ord(n) + 1))