my_dict = {'Ivan': 2000, 'Petr': 2005, 'Vera': 2012}
print(my_dict)
print(my_dict['Ivan'], my_dict.get('Max', 'Пусто'))
my_dict.update({'Serg': 1990, 'Deyns': 2015})
print(my_dict.pop('Vera'))
print(my_dict)

my_set = {1, 1, 2, 2, (3, 4), 'abc', 6, 'abc', '7', 5, (3, 4)}
print(my_set)
my_set.add(9)
my_set.add('zxc')
my_set.discard((3, 4))
print(my_set)
