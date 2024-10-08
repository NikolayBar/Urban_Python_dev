from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    TRANS_NUM = 100
    NUM_RANGE = 50, 500
    DELAY = 0.001

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(self.TRANS_NUM):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            x = randint(*self.NUM_RANGE)
            self.balance += x
            print(f'Пополнение: {x}. Баланс: {self.balance}')
            sleep(self.DELAY)

    def take(self):
        for _ in range(self.TRANS_NUM):
            x = randint(*self.NUM_RANGE)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств, Баланс: {self.balance}')
                self.lock.acquire()
            sleep(self.DELAY)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

threads = th1, th2
for obj in threads:
    obj.start()

for obj in threads:
    obj.join()

print(f'Итоговый баланс: {bk.balance}')
