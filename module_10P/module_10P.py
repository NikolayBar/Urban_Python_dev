import requests
from threading import Thread


class Getter(Thread):
    res = []

    def __init__(self, url):
        self.THE_URL = url
        super().__init__()

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []
num_of_genres = 20
url = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
for i in range(num_of_genres):
    thread = Getter(url)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(*Getter.res, sep='\n')

assert len(Getter.res) == num_of_genres - 1, f'{len(Getter.res)} genres returned!'
