immutable_var = 'abc', 12, 10.0, True, [1, 2], (3, 4)
print(immutable_var)
try:
    immutable_var[0] = 'ASD'
except TypeError:
    print('Кортеж относится к неизменяемым типам данных')

mutable_list = list(immutable_var)
mutable_list[0] = 'ASD'
print(mutable_list)
