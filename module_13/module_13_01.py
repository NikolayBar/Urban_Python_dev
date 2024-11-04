import asyncio
place = 0
tournament_dict = {}

async def start_strongman(name, power, slp=1):
    global place
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(slp / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')
    place += 1
    tournament_dict[place] = name


async def start_tournament(slp_time=1):
    participants = [('Бывалый', 5), ('Трус', 3), ('Балбес', 4)]
    tasks = [asyncio.create_task(start_strongman(*x, slp_time)) for x in participants]

    for task in tasks:
        await task

    for k, v in tournament_dict.items():
        print(f'{k}: {v}')

asyncio.run(start_tournament(1))
