def swap_case(s):
    split_text = str(s)
    result = ''
    for letter in split_text:
        if letter.isupper():
            final_letter = letter.lower()
        else:
            final_letter = letter.upper()
        result += ''.join(final_letter)
    return result


if __name__ == '__main__':
    s = input()  # .swapcase() --> easy way than creating function
    result = swap_case(s)
    print(result)
