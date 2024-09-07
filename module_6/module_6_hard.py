class Figure:
    sides_count = 0

    @staticmethod
    def __is_valid_color(red, green, blue) -> bool:
        return all(type(x) is int and 0 <= x <= 255 for x in (red, green, blue))

    def __is_valid_sides(self, sides) -> bool:
        return len(sides) == self.sides_count and all(type(x) is int and x > 0 for x in sides)

    def __init__(self, colors, *sides):
        if len(colors) == 3 and self.__is_valid_color(*colors):
            self.__color = [*colors]
        else:
            self.__color = [0, 0, 0]
        self.__sides = []
        if self.__is_valid_sides(sides):
            self.set_sides(*sides)
        else:
            self.__sides = [1 for _ in range(self.sides_count)]

    def get_color(self):
        return self.__color

    def set_color(self, red: int, green: int, blue: int):
        if self.__is_valid_color(red, green, blue):
            self.__color = [red, green, blue]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = [*sides]

    def __len__(self):
        return sum(self.get_sides())

    def __str__(self):
        res = ''
        for k, v in self.__dict__.items():
            res += f'{k}: {v}\n'
        return res

    def get_square(self):
        pass

    def get_volume(self):
        pass

    def info(self):
        atr = (f'{self.__color=}', f'{self.__sides=}',
               f'{len(self)=}', f'{self.get_sides()=}',
               f'{self.get_color()=}', f'{self.get_volume()=}',
               f'{self.get_square()=}'
               )
        for el in atr:
            if 'None' not in el:
                print(el)


class Circle(Figure):
    from math import pi
    sides_count = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.__get_radius()

    def __get_radius(self):
        self.__radius = self.get_sides()[0] / (2 * self.pi)
        return self.__radius

    def set_sides(self, *args):
        super().set_sides(*args)
        self.__get_radius()

    def get_square(self):
        return self.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__(*args)
        self.__ch_sides()

    def __ch_sides(self):
        a, b, c = self.get_sides()
        if a + b < c or b + c < a or a + c < b:
            self.set_sides(1 for _ in range(self.sides_count))

    def get_square(self):
        p = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        res = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return res


class Cube(Figure):
    sides_count = 12

    def __set_sides(self, *args):
        if len(args) == 1 and type(args[0]) is int:
            return [args[0]] * self.sides_count
        else:
            return args

    def __init__(self, color, *sides):
        sides = self.__set_sides(*sides)
        super().__init__(color, *sides)

    def set_sides(self, *sides):
        sides = self.__set_sides(*sides)
        super().set_sides(*sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    Cls = Cube

    tst = Cls((100, 50, 25), 9, 2)
    print(tst.__class__.__name__)
    tst.info()
    print('CHANGE COLOR')
    tst.set_color(10, 33, 44)
    tst.info()
    print('CHANGE SIDES')
    tst.set_sides(44)
    tst.info()
