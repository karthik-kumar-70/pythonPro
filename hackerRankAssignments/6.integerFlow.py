def intFlow(self):
    flow = []
    for i in range(1, self + 1):
        flow.append(str(i))
    print(flow)
    integer = ""
    print(integer.join(flow))


if __name__ == '__main__':
    number = int(input())
    if number in range(1, 151):
        intFlow(number)
