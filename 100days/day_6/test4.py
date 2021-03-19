def sum_all(*argv):
    total = 0
    for u in argv:
        total += u
    return total

print(sum_all(1,2,3,4,5,6))