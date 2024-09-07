class WordsFinder:

    def __init__(self, *args: str):
        self.file_names = args

    def get_all_words(self) -> dict:
        all_worlds = {}
        bad_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for f_name in self.file_names:
            with open(f_name, 'r', encoding='utf-8') as file:
                data = file.read()
            for char in bad_chars:
                data = data.replace(char, '').lower()
            all_worlds[f_name] = data.split()
        return all_worlds

    def find(self, word):
        return {k: v.index(word.lower()) + 1 for k, v in self.get_all_words().items() if word.lower() in v}

    def count(self, word):
        return {k: v.count(word.lower()) for k, v in self.get_all_words().items()}


if __name__ == '__main__':

    file_names = ('test_file.txt', 'Rudyard Kipling - If.txt', 'test.txt')

    finder2 = WordsFinder(*file_names)
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
