import random


def generate_code(code_len=4):
    xchar = '0123456789abcdefghijklmnopqrstuvwxyz'
    xchar_len = len(xchar)
    code = ''
    for _ in range(code_len):
        index = random.randint(0, xchar_len-1)
        code += xchar[index]
    return code

def main():
    print(generate_code())

if __name__ == '__main__':
    main()