from random import seed, randint as rd, uniform as uf, choice as ch


class Team:

    def __init__(self, name: str, team_members: int, tasks: list, time: float):
        self.name = name
        self.team_members = team_members
        self.time = time
        self.tasks = tasks
        self.solved_task = len([x for x in self.tasks if x != 0])
        self.score = sum(self.tasks)

    def __eq__(self, other):
        return self.score == other.score and self.time == other.time

    def __gt__(self, other):
        return self.score > other.score or self.score == other.score and self.time < other.time


class Results:

    def __init__(self, team1: Team, team2: Team):
        self.t1 = team1
        self.t2 = team2

    def squad_list(self):
        """Использование %"""
        for team in (self.t1, self.t2):
            print('В команде %s участников: %s! ' % (team.name, team.team_members))
        total_members = self.t1.team_members + self.t2.team_members
        print('\tИтого сегодня участвовало: %s игроков!' % total_members)

    def tasks_solved(self):
        """Использование format()"""
        for team in (self.t1, self.t2):
            solved_task = len([x for x in team.tasks if x != 0])
            print('\nКоманда {0} решила задач: {1} !'.format(team.name, solved_task))
            print('{0} решили задачи за {1} сек!'.format(team.name, team.time))

    def __get_winner(self):
        a = self.t1
        b = self.t2
        if a > b:
            winner = f' победа команды {self.t1.name}'
        elif a < b:
            winner = f' победа команды {self.t2.name}'
        else:
            winner = 'Ничья!'

        return winner

    def challenge_result(self):
        """Использование f-строк"""
        winner = self.__get_winner()
        print(f'\nКоманды решили {self.t1.solved_task} и {self.t2.solved_task} задач.')
        print(f'Заработали очков: \n{self.t1.name} - {self.t1.score}\n{self.t2.name} - {self.t2.score}')
        print(f'Результат битвы: {winner}!')
        total_task = self.t1.solved_task + self.t2.solved_task
        time_avg = (self.t1.time + self.t2.time) / total_task
        print(f'Сегодня было решено {total_task} задач, в среднем по {time_avg: .1f} секунды на задачу!')


if __name__ == '__main__':
    seed(11)

    team1_num = 5
    team2_num = 6
    team1_tasks = [ch((0, 1, 1, 1)) for _ in range(50)]
    team2_tasks = [ch((0, 1, 1, 1)) for _ in range(50)]
    team1_time = round(uf(1500, 2500), 3)
    team2_time = round(uf(1500, 2500), 3)

    team_1 = Team('"Мастера кода"', team1_num, team1_tasks, team1_time)
    team_2 = Team('"Волшебники данных"', team2_num, team2_tasks, team2_time)

    res = Results(team_1, team_2)

    res.squad_list()
    res.tasks_solved()
    res.challenge_result()
