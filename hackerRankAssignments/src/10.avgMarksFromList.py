total = 0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *args = input().split()
        scores = list(map(float, args))
        student_marks[name] = scores

    marks_of_requested_student = student_marks.get(input())
    for i in range(len(marks_of_requested_student)):
        total += marks_of_requested_student[i]
    print("{:.2f}".format(total / 3))
