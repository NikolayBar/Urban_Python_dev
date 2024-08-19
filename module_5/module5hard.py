class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.nickname)

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return f'{self.title}, {self.duration}{"" if not self.adult_mode else ", age 18+"} '


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, name: str, password: str, age: int):
        if name not in self.users:
            obj = User(name, password, age)
            self.users.append(obj)
            self.current_user = obj

        else:
            print(f'Пользователь {name} уже существует')
            return False

    def add(self, *obj):
        if not all(isinstance(x, Video) for x in obj):
            raise TypeError('Требуется объект <class Video>')
        if not any(x in self.videos for x in obj):
            self.videos.extend(obj)

    def log_in(self, name, password):
        if name in self.users:
            index = self.users.index(name)
            if self.users[index].password == hash(password):
                self.current_user = self.users[index]
            else:
                print('Не правильный пароль')
                return
        else:
            print(f'Пользователь {name} не найден.')

    def log_out(self):
        self.current_user = None

    def get_videos(self, string: str):
        f_videos = []
        for obj in self.videos:
            if obj.title == string:
                return obj
            else:
                if string.lower() in obj.title.lower():
                    f_videos.append(obj.title)
        return f_videos

    def watch_video(self, title):
        from time import sleep
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return None

        cur_video = self.get_videos(title)
        if isinstance(cur_video, Video):
            if cur_video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return None
            digs = len(str(cur_video.duration))
            print(f'Play video for {self.current_user}')
            for sec in range(cur_video.time_now + 1, cur_video.duration + 1):
                print(f'{sec: >{digs}d}', end=' ')
                sleep(0.1)
            print('Конец видео')
            return None

    def info_users(self):
        self.__print_info(self.users)

    def info_video(self):
        self.__print_info(self.videos)

    @staticmethod
    def __print_info(objs):
        pos = 1
        for obj in objs:
            print(f'{pos: 2d}. ', obj)
            pos += 1


if __name__ == '__main__':

    ur = UrTube()
    ur.register('qwer', '1234', 34)
    ur.register('asdf', '2345', 25)
    ur.info_users()
    v1 = Video('film1', 30)
    v2 = Video('film2', 20, adult_mode=True)
    ur.add(v1, v2)
    ur.info_video()
    ur.log_out()
    ur.log_in('qwer', '1234')
    print(ur.current_user)




