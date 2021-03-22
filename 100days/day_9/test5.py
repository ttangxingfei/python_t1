class Person(object):
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch_mv(self):
        if self._age > 18:
            print("%s正在观看大电影" % self._name)
        else:
            print("%s正在观看喜洋洋" % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s%s正在学习%s" %(self._grade, self._name, course))


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title =title

    @property
    def title(self):
        return self._title

    @title.setter
    def titel(self, title):
        self._title = title

    def teach(self, course):
        print("%s%s正在教%s" %(self._title, self._name, course))


def main():
    stu = Student('Tom', 14, '初二')
    stu.watch_mv()
    stu.study('math')
    tea = Teacher('Mrs.Wang', 32, '教授')
    tea.watch_mv()
    tea.teach('语文')


if __name__ == '__main__':
    main()
