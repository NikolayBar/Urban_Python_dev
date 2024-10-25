import requests
import random


class MyClass(object):

    def __init__(self, attr=99):
        super().__init__()
        self.attr = attr

    def set_attr(self, value):
        self.attr = value


def my_function(a= 0, *args):
    in_arg = args
    b = a
    message = ('Параметр', 'Вызов без параметров')
    print(f'{message[not in_arg]} {args}')


s_number= 45
s_string = 'qwerty'
s_list = [s_number, s_string]
s_inst = MyClass
s_set = {1, 2, 2, 3, 3}
