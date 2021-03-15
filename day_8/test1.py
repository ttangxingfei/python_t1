class student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s'%(self.name, course_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s在正在观看<熊出没>'%self.name)
        else:
            print('%s正在观看岛国爱情大电影'%self.name)

def main():
    stu1 = student('luohao', 38)
    stu1.study('python_design')
    stu1.watch_movie()

if __name__ == '__main__':
    main()