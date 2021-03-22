from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @classmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print("%s:汪汪汪" %self._name)


class Cat(Pet):
    def make_voice(self):
        print("%s:喵喵喵" %self._name)


def main():
    pets = [Dog('大黄'), Cat('小喵'), Dog('二哈')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()