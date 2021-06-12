import math


def doSquaresTillNumber(number):
    for i in range(number):
        print(int(math.pow(i, 2)))


if __name__ == '__main__':
    number = int(input())

    if number in range(1, 21):
        doSquaresTillNumber(number)
