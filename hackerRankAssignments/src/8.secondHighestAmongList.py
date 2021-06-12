if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if 10 >= n >= 2 and -100 <= len(arr) <= 100:

        # arr.sort(reverse=True)
        newArr = list(set(arr))
        newArr.sort(reverse=True)
        if len(newArr) >= 1:
            print(newArr[1])
