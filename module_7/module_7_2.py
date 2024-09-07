def custom_write(file_name, strings):
    num_line = 1
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for line in strings:
            pos = file.tell()
            key = (num_line, pos)
            num_line += 1
            strings_positions[key] = line
            file.write(line + '\n')

    return strings_positions


if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)