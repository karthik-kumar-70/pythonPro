markSheet = []
scoreList = []


def inputValidator(number):
    if 2 <= number <= 5:
        return True
    else:
        return False


# def negativeNumbersFilter(inputarray):
#     for i in range(len(inputarray)-1, -1, -1):
#         if inputarray[i][1] < 0:
#             inputarray.pop(i)
#     return inputarray


def getSecondLowest(array2d):
    for i in range(0, len(array2d)):
        if second_lowest[1] == array2d[i][1]:
            print(array2d[i][0])


if __name__ == '__main__':
    count = int(input())
    if inputValidator(count):
        for _ in range(count):
            name = input()
            score = float(input())
            markSheet.append(list([name, score]))
            scoreList.append(score)

    markSheet.sort()
    # negativeNumbersFilter(markSheet)
    print(markSheet)
    second_lowest = sorted(list(set(scoreList)), key=lambda x: x)
    print(second_lowest[1])
    markSheetSorted = sorted(markSheet, key=lambda x: x[1])
    print(markSheetSorted)
    getSecondLowest(markSheetSorted)

# scoreList.append(score)
# print(c)
# print(scoreList)

#
# c.sort(reverse=False)
# scoreList.sort(reverse=False)
# print(c)
# print(scoreList)
# setScore = list(set(scoreList))
# print(setScore)
# for i in range(0, len(c)):
#     if setScore[rankFromBottom-1] == c[i][1]:
#         print(c[i][0])


# if scoreList[1] != scoreList[2]:
#     print(c[1][0])
#
# else:
#     for i in range(1,len(scoreList)):
#         if c[i][1] == scoreList[1]:
#             print(c[i][0])
#         else:
#             exit()


#  ########## Other approaches #######
# c = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         # c.append(list(map(list([name,score]),name,score))))
#         scoreList.append(score)
#         c.append(list([name, score]))
#         print(c)
# c_sorted = sorted(c,key=lambda x:x[1])
# print(c_sorted)
# if c_sorted[1][1] != c_sorted[2][1]:
#     print(c_sorted[1][1])
# else:
#     for i in range(1,len(c_sorted)):
#         if c_sorted[1][1] == c_sorted[i][1]:
#             print(c_sorted[i][0])
#         else:
#             exit()
