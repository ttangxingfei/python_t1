import os
import time

def main():
    content = '我爱北京天安门......'
    set_time = 5
    while set_time > 0:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        set_time -= 0.2
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()