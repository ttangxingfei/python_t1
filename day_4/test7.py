x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x

for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        temp = i
        print('%d和%d的最大公约数是%d'%(x, y, temp))
        print('%d和%d的最小公倍数是%d'%(x, y, x*y/temp))
        break