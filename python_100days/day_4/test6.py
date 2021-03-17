from math import sqrt

num = int(input('请输入一个正整数： '))
if num <= 0:
    num = int(input('请重新输入一个正整数： '))

end = int(sqrt(num))
is_prime = True

for i in (2, end + 1):
    num % i == 0
    is_prime = False
    break

if is_prime and num !=1:
    print('%d是一个素数'%num)
else:
    print('%d不是一个素数'%num)



