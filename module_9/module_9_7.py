def check_prime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def is_prime(func):
    def wrap(*args):
        res = func(*args)
        print('Простое' if check_prime(res) else 'Составное')
        return res
    wrap.__name__ = func.__name__
    return wrap


@is_prime
def sum_three(a, b, c):
    return sum((a, b, c))


result = sum_three(83, 89, 97)
print(result)

