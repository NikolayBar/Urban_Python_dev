def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except Exception as exc:
            result[func.__name__] = f"Ошибка: {exc.args[0]}"
    return result


if __name__ == '__main__':

    data = (([6, 20, 15, 9], max, min),
            ([6, 20, 15, 9], len, sum, sorted),
            (['6', '20', '15', '9'], len, sum, sorted),
            (100, len, sum, sorted),
            ('100', len, sum, sorted))

    for obj in data:
        print(apply_all_func(*obj))
