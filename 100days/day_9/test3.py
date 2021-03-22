from math import sqrt

def Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def isvalid(a, b, c):
        return a+b > c and a+c > b and b+c > a

    def zhouchang(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.zhouchang()
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

    
def main():
    a = int(input('请输入三角形的第一条边: '))
    b = int(input('请输入三角形的第二条边: '))
    c = int(input('请输入三角形的第三条边: '))
    if Triangle.isvalid(a, b, c):
        t = Triangle(a, b, c)
        print("三角形的周长为%.02f" % t.zhouchang())
        print("三角形的面积为%.02f" % t.area())
    else:
        print("您输入的三条边无法构成三角形")

if __name__ == '__main__':
    main()