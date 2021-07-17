def split_and_join(args):
    return '-'.join((args.split()))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)