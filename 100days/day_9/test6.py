from abc import abstractmethod, ABCMeta

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_noise(self):
        pass


class Dog(Pet):

    def make_noise(self):
        print('%s:汪' % self._nickname)


class Cat(Pet):

    def make_noise(self):
        print('%s:喵' % self._nickname)


def main():
    pets = [Dog('大哈'), Cat('大喵'), Dog('二哈')]
    for pet in pets:
        pet.make_noise()

if __name__ == '__main__':
    main()