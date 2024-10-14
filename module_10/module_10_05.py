import multiprocessing
from time import time


def read_info(f_name: str):
    all_data = []
    with open(f_name, 'r', encoding='utf-8') as file:
        while (line:= file.readline()) != '':
            all_data.append(line.strip())
    return all_data

if __name__ == '__main__':

    filenames = [f'.\\Files\\file {number}.txt' for number in range(1, 5)]

    # # Линейный вызов
    # start = time()
    # for name in filenames:
    #     read_info(name)
    # print(f'{time() - start:.4f}')

    # Много процессный
    start = time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    print(f'{time() - start:.4f}')