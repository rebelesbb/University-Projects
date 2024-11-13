from random import randint


def birthday(n: int) -> bool:
    birthdayList = []
    isTheSame = False
    for i in range(n):
        bd = randint(1, 365)
        if birthdayList.count(bd) > 0:
            isTheSame = True
        birthdayList.append(bd)
    return isTheSame


def run():
    count = 0
    tests = 1000
    n = 26
    for i in range(1000):
        if birthday(n):
            count += 1
    print(f'Probabilitatea ca doua persoane din {n} sa aiba aceeasi zi de nastere este : {count / tests}')

run()