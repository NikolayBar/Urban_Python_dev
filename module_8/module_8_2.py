def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for n in numbers:
        try:
            result += n
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {n}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
        len_ = len(numbers) - res[1]
        return res[0] / len_
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


if __name__ == '__main__':

    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
    print(f'Результат 5: {calculate_average([0, 0, 0, 0])}')
    print(f'Результат 6: {calculate_average(("0", 10, 0b000111, 4, "a"))}')
    print(f'Результат 7: {calculate_average([])}')


