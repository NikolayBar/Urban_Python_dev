class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__filename = 'products.txt'

    def get_products(self):
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = file.read()
        return data

    def add(self, *args):
        data = self.get_products()
        with open(self.__filename, 'a', encoding='utf-8') as file:
            for obj in args:
                if obj.name in data:
                    print(f'Продукт {obj.name} же есть в магазине')
                else:
                    file.write(str(obj)+'\n')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    # print(p2)  # __str__

    s1.add(p1, p2, p3)

    # print(s1.get_products())
