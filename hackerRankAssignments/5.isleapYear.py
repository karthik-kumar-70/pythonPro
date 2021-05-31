def is_leap(self):
    if (self % 4 == 0 and self % 100 != 0) or self % 400 == 0:
        return True
    else:
        return False


year = int(input())

if year in range(1900, pow(10, 5)):
    print(is_leap(year))
