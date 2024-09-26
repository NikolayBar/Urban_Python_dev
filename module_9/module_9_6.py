def all_variants(text, *, num_chars=1, start=0):
    num_chars = num_chars if num_chars > 0 else 1
    index = start
    while num_chars <= len(text):
        if len(text[index: index + num_chars]) == num_chars:
            yield text[index: index + num_chars]
        index += 1
        if index == len(text):
            index = start
            num_chars += 1


if __name__ == '__main__':

    a = all_variants("abcd")
    for i in a:
        print(i)
