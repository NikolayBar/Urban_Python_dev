def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return 'На ноль делить нельзя'


if __name__ == '__main__':
    print(add(3,4))

