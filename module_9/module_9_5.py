class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = self.__check_step(step)
        self.pointer = self.start

    @staticmethod
    def __check_step(value):
        if value != 0:
            return value
        else:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer > self.stop or \
                self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        return self.pointer


if __name__ == '__main__':

    data = [(100, 200, 0), (-5, 1), (6, 15, 2), (5, 1, -1), (10, 1)]

    for arg in data:
        try:
            iter2 = Iterator(*arg)
            for i in iter2:
                print(i, end=' ')
            print()
        except StepValueError:
            print('Шаг указан неверно')
