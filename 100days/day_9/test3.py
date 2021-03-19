from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))


def main():
    a = int(input("请输入三角形的第一条边："))
    b = int(input("请输入三角形的第二条边："))
    c = int(input("请输入三角形的第三条边："))
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print("三角形的周长为%.02f"%t.perimeter())
        print("三角形的面积为%.02f"%t.area())
    else:
        print("您输入的三条边无法构成三角形!")

    
if __name__ == '__main__':
    main()