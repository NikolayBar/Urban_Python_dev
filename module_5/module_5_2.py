class House:

    def __init__(self, name: str, floors: int) -> None:
        self.name = name
        self.number_of_floors = floors

    def go_to(self, floor: int) -> None:
        if not (1 <= floor <= self.number_of_floors):
            print('Такого этажа не существует')
            return
        for lv in range(1, floor + 1):
            print(lv)

        return None

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

