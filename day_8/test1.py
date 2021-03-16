class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course):
        print('%s正在学习%s'%(self.name, course))

    def watch_movie(self):
        if self.age > 18:
            print('%s正在观看大电影'%self.name)
        else:
            print('%s正在观看熊出没'%self.name)

def main():
    stu1 = Student('luohao', 28)
    stu1.study('python')
    stu1.watch_movie()

if __name__ == '__main__':
    main()