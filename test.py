from module_6.module_6_hard import *

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'{circle1.get_color()=}')
cube1.set_color(300, 70, 15)  # Не изменится
print(f'{cube1.get_color()=} | [222, 35, 130]')

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(f'{cube1.get_sides()=} | [6, 6, ..., 6]')  # [6, 6, ..., 6]
circle1.set_sides(15)  # Изменится
print(f'{circle1.get_sides()=}')

# Проверка периметра (круга), это и есть длина:
print(f'{len(circle1)=}')

# Проверка объёма (куба):
print(f'{cube1.get_volume()=}')
