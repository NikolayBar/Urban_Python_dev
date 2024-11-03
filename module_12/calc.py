import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        res = a / b
        logging.info(f'Successful divide {a} / {b}')
        return res
    except ZeroDivisionError as e:
        logging.error('На ноль делить нельзя', exc_info=True)
        return 'На ноль делить нельзя'


def sqrt(a, b=0.5):
    x = 1 / b
    try:
        res = a ** x
        logging.info(f'Successful extraction of the root of {b} degrees out of {a}')
        return res
    except TypeError as e:
        logging.error(f'Errror', exc_info=True)


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='calc.log', encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")

    for fn in (add, sub, mul, div, sqrt, pow):
        print(fn(25, 2))
