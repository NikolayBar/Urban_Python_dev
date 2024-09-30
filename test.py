# import os
# import time
#
# os.chdir('module_7')
# print('Текущий каталог', os.getcwd())
#
# path = os.getcwd()
#
# def scan_dir(path, level=1):
#     print('Level=', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\' + i):
#             print('Спускаемся', path + '\\' + i)
#             scan_dir(path + '\\' + i, level + 1)
#             print('Возвращаемся в', path)
#
#
# scan_dir(path)

numbers_list = [1, 1, 2, 2, 3, 3, 4, 4]

numbers_list_ordered = sorted(numbers_list, reverse=True)
numbers_set = set(numbers_list)
numbers_set.add(max(numbers_list) + 1)
_list = sorted(set(numbers_list))
numbers_frozenset = frozenset(_list[1:])
print(numbers_frozenset)
