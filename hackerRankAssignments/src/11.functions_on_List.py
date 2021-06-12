def list_functions(*args):

    if args[0][0] == 'insert':
        start_list.insert(int(args[0][1]), int(args[0][2]))

    elif args[0][0] == 'print':
        print(start_list)

    elif args[0][0] == 'remove':
        start_list.remove(int(args[0][1]))

    elif args[0][0] == 'append':
        start_list.append(int(args[0][1]))

    elif args[0][0] == 'sort':
        start_list.sort()

    elif args[0][0] == 'pop':
        start_list.pop()

    elif args[0][0] == 'reverse':
        start_list.reverse()


if __name__ == '__main__':
    start_list = []
    for i in range(int(input())):
        user_input = input().split()
        # print(user_input)
        list_functions(user_input)
