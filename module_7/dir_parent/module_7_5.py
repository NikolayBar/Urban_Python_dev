import os
import time


def scan_dir(path='.'):
    scan_files(path)
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            scan_dir(path + '\\' + i)


def scan_files(path='.'):
    for obj in os.listdir(path):
        if not os.path.isdir(obj):
            f_path = f'{path}\\{obj}'
            _time = os.stat(f_path).st_mtime
            f_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(_time))
            f_size = os.stat(f_path).st_size
            print(f'Файл: {obj}\nПуть: {f_path}, Размер: {f_size} байт, Время изменения: {f_time}, '
                  f'Родительская директория: {path}')


scan_dir()
