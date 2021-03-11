def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' %ball, end=' ')
    print()

def random_select():
    red

def main():
    n = int(input('机选几注： '))
    for _ in range(n):
        dispaly(random_select())

if __name__ == '__main__':
    main()