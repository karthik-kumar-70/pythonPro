# def createList(*args):
#     a = []
#     for i in range(*args):
#         a.append(i)


x, y, z = list(range(0, int(input())+1)), list(range(0, int(input())+1)),\
          list(range(0, int(input())+1))
print(x, y, z)
# y = createList(int(input()))
# z = createList(int(input()))
#
ListOfNumbers = [[x, y] for i in x for j in y]
print(len(ListOfNumbers),ListOfNumbers)
