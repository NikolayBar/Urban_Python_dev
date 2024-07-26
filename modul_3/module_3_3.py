def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 'string', [3, 4, 5]]
values_dict = {'a': 1, 'b': True, 'c': [6, 7, 8]}
values_list_2 = [54.32, 'Строка']

print_params()
print_params(11, 22)
print_params(111, 222, 333)
print_params(b=25)
print_params(c=[1, 2, 3])

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
