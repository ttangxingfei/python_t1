for x in range(0,20):
    for y in range(0,34):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print("100块钱可以买公鸡%d只，母鸡%d只，小鸡%d"%(x, y, z))
