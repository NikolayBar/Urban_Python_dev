from threading import Thread
from datetime import datetime
from time import sleep


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово № {word + 1}\n')
    sleep(0.5)
    print(f'Завершилась запись в файл {file_name}')


w_count = (10, 30, 200, 1000)

t_start = datetime.now()

for i in range(len(w_count)):
    f_name = f'example{i + 1}.txt'
    write_words(w_count[i], f_name)

t_end = datetime.now()
print(f'Работа потоков {t_end - t_start}')

t_start = datetime.now()
thr_list = [Thread(target=write_words, args=(w_count[i], f'example{i+5}.txt')) for i in range(4)]

for obj in thr_list:
    obj.start()
for obj in thr_list:
    obj.join()

t_end = datetime.now()
print(f'Работа потоков {t_end - t_start}')