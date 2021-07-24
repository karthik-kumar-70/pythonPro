def count_substring(first_string, second_string):
    length_of_first_string = len(first_string)
    length_of_second_string = len(second_string)
    counter = 0
    for i in range(1, length_of_first_string - length_of_second_string + 2): # 2 is added to reduced number of runs
        print(
            f"{list(first_string)[i - 1:length_of_second_string + i - 1]} and {list(second_string)}")
        print(True if (list(first_string)[
                       i - 1:length_of_second_string + i - 1] == list(
            second_string)) else False)
        if list(first_string)[i - 1:length_of_second_string + i - 1] == list(
            second_string):
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(f"{string} and  {sub_string}")
    counter = count_substring(string, sub_string)
    print(counter)
