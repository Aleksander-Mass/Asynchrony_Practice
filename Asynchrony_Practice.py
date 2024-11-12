import asyncio


# Функция для имитации подъема шаров силачом
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):  # Каждый силач поднимает 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


# Функция для запуска турнира
async def start_tournament():
    # Создаем задачи для каждого участника
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Ожидание выполнения всех задач
    await task1
    await task2
    await task3


# Запуск турнира
asyncio.run(start_tournament())

###    Вывод на консоль:
"""
Силач Pasha начал соревнования
Силач Denis начал соревнования
Силач Apollon начал соревнования
Силач Apollon поднял 1 шар
Силач Denis поднял 1 шар
Силач Pasha поднял 1 шар
Силач Apollon поднял 2 шар
Силач Denis поднял 2 шар
Силач Apollon поднял 3 шар
Силач Pasha поднял 2 шар
Силач Denis поднял 3 шар
Силач Apollon поднял 4 шар
Силач Apollon поднял 5 шар
Силач Apollon закончил соревнования
Силач Pasha поднял 3 шар
Силач Denis поднял 4 шар
Силач Denis поднял 5 шар
Силач Denis закончил соревнования
Силач Pasha поднял 4 шар
Силач Pasha поднял 5 шар
Силач Pasha закончил соревнования
"""