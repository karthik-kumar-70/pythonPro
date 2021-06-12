def threeOutputs(first, second):
    print(first + second)
    print(first - second)
    print(first * second)


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    if (a and b >= 1) and (a and b <= pow(10,10)):
        threeOutputs(a, b)
