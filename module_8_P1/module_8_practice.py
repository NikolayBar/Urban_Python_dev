def calc(lines: str):
    value_1, operation, value_2 = lines.strip().split()
    value_1, operation, value_2 = map(str.strip, (value_1, operation, value_2))
    # value_1, value_2 = map(int, (value_1, value_2))
    expression = f'{value_1}{operation}{value_2}'
    return eval(expression)


if __name__ == '__main__':
    err_log = []
    cnt = 0
    with open('calc.txt', 'r', encoding='utf-8') as file:
        for line in file:
            cnt += 1
            try:
                print(f'{cnt:05d}. {calc(line)}')
            except Exception as exc:
                print(f'{cnt:05d}. Ошибка > {line.strip()}')
                err_log.append(str(exc.args[0]) + f'в строке {cnt}: <{line.strip()}>')

    print(*err_log, sep='\n')
