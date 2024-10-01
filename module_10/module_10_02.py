from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies:
            enemies -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


knights = [Knight('Sir Lancelot', 5),
           Knight("Sir Galahad", 20)]

for obj in knights:
    obj.start()

for obj in knights:
    obj.join()

print('Все битвы закончились!')