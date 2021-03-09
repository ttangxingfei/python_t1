def f1(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
        yield a

def main():
    for j in f1(20):
        print(j)


if __name__ == '__main__':
    main()