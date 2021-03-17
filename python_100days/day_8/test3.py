from time import sleep

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def display(self):
        return '%02d:%02d:%02d'%(self.hour, self.minute, self.second)


def main():
    clock = Clock(23, 59, 59)
    while True:
        print(clock.display())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()