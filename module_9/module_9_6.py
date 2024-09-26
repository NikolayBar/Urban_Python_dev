def all_variants(text, reverse=False):
    if not reverse:
        index, k = 0, 1
    else:
        index, k = len(text)-1, -1
    while 0 <= index < len(text):
        yield text[index]
        index += k


if __name__ == '__main__':

    a = all_variants("abc")
    for i in a:
        print(i, end=' ')
    print()

    b = all_variants("1234567890", True)
    for i in b:
        print(i, end=' ')
    print()
