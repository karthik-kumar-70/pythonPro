if __name__ == '__main__':
    s = input()
    print(type(s))
    print any (s.isalnum() for s in s)
    print(s.isalpha())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())

print(qA2.isalpha())
