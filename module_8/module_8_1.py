from operator import add, sub, mul, truediv, pow


def add_everything_up(a, b):
    opr_dict = {add: '+', sub: '-', mul: '*', truediv: '/', pow: '^'}
    for opr in opr_dict.keys():
        try:
            print(f'{a} {opr_dict[opr]} {b} = {opr(a, b)}')
        except ZeroDivisionError:
            print(f'{a} {opr_dict[opr]} {b} = Делить на ноль нельзя!')
        except TypeError:
            print(f"'{str(a) + str(b)}'")


a = 3
b = 0

try:
    add_everything_up(a, b)
except TypeError as exc:
    print(f'{exc}\nНеобходимо передать значения <a> и <b> ')

else:
    print('\nBLOCK ELSE')
finally:
    print('BLOCK FINALLY')
