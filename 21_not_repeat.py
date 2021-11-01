"""Zadanie 1: Nie powtarzaj się!
W każdym języku programowania ważne jest by się nie powtarzać DRY - dlatego też warto starać się korzystać z funkcji.
W związku z tym:
Wylosuj 10 liczb z zakresu od 0 do 10, jeżeli któraś liczba się powtórzy wyświetl napis: Oh no! I repeated myself!
Wskazówka
Do losowania wykorzystaj bibliotekę random."""
import random


def no_repeat():
    numbers_set = set()
    for i in range(0, 10):
        number = random.randint(0, 10)
        print(number, end=', ')
        if number in numbers_set:
            print('Oh no! I repeated myself!', end=', ')
        numbers_set.add(number)


if __name__ == '__main__':
    no_repeat()


