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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
