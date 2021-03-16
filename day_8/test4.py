from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)'%(str(self.x), str(self.y))

def main():
    a = Point(0, 0)
    print(a)
    b = Point(2, 3)
    print(b)
    b.move_by(1, 1)
    print(b)
    print(a.distance_to(b))

if __name__ == '__main__':
    main()