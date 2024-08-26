class Vehicle:
    __COLOR_VARIANTS = ('blue', 'red', 'green', 'black', 'white')

    def __init__(self, owner, model, color, power):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = power
        self.__color: str = color

    def get_model(self) -> str:
        return f'Модель: {self.__model}'

    def get_horsepower(self) -> str:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def print_info(self) -> None:
        print(self.get_model(), self.get_horsepower(), self.get_color(), sep='\n')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
