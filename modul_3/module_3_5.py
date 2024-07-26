def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    first = first if first != 0 else 1
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


def r_func(num):
    if num == 0:
        return 1
    else:
        b = num % 10 if num % 10 != 0 else 1
        return b * r_func(num // 10)


number = 12300

result = get_multiplied_digits(number)
print(result)

result2 = r_func(number)
print(result2)
