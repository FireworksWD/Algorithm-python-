n = int(input())
res = 0
while n:
    res += n % 10
    n //= 10
dis = {0: 'ling', 1: 'yi', 2: 'er', 3: 'san', 4: 'si', 5: 'wu', 6: 'liu', 7: 'qi', 8: 'ba', 9: 'jiu'}
ret = []
while res:
    ret.append(dis[res % 10])
    res //= 10
print(' '.join(ret[::-1]))
