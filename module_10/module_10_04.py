from threading import Thread
from time import sleep
from random import randint
import queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()
        return

    def guest_arrival(self, *arg):
        l_t = len(self.tables)
        for i, v in enumerate(arg):
            if tables[i % l_t].guest is None:
                tables[i % l_t].guest = v
                print(f'{v.name} сел(-а) за стол номер {tables[i % l_t].number}')
            else:
                print(f'{v.name} в очереди')
                self.queue.put(v)
        return

    def discuss_guests(self):
        while not all(x.guest is None for x in self.tables):
            for i, v in enumerate(self.tables):
                if v.guest is not None and not v.guest.is_alive():
                    print(f'{v.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {tables[i].number} свободен')
                    self.tables[i].guest = None

            for i, v in enumerate(self.tables):
                if v.guest is None and not self.queue.empty():
                    g = self.queue.get()
                    print(f'{g.name}  вышел(-ла) из очереди и сел(-а) за стол номер {v.number}')
                    g.start()
                    self.tables[i].guest = g


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
