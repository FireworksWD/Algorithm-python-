s=input()
while True:
    s=s.replace('ab', '')
    if 'ab' not in s:
        break
if s:
    print('Bad')
else:
    print('Good')
