from random import randint

def rac(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def sum_abc(a=0, b=0, c=0):
    return a + b + c


print(rac())
print(rac(3))

print(sum_abc())
print(sum_abc(1, 2, 3))
