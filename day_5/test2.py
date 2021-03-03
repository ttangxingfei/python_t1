num = int(input('num = '))
re_num = 0
while num > 0:
    re_num = re_num * 10 + num % 10
    num = num // 10

print('re_num = %d'%re_num)