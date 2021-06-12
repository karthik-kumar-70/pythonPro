def isWeird(number):
    if number % 2 == 0:
        if number > 20 or number in range(2, 5):
            return print("Not Weird")
        else:
            return print("Weird")
    elif number % 2 != 0 and number in range(2, 5):
        return print("Weird")



if __name__ == '__main__':

    n = int(input().strip())

    if n >= 1 & n <= 100:
        isWeird(n)
    else:
        pass