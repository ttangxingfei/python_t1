from random import randint, randrange, sample

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls)-1:
            print('|', end=' ')
        print('%02d'%ball, end=' ')
    print()

def select_ball():
    red_ball = [x for x in range(1, 34)]
    s_ball = []
    s_ball = sample(red_ball, 6)
    s_ball.sort()
    s_ball.append(randint(1, 14))
    return s_ball

def main():
    zhu_num = int(input('机选几注： '))
    for _ in range(zhu_num):
        display(select_ball())

if __name__ == '__main__':
    main()