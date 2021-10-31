"""Zadanie: 1 Ala - Kocia mama.
Napisz funkcję (lub program), który wyświetli poprawnie zdanie "Ala ma x kotów" w zależności od ilości kotów.
 To jest: Ala ma 1 kota, Ala ma 2 koty, Ala ma 10 kotów.
Podpowiedź 1
Odmiana słowa "kot" zależy od reszty z dzielenia liczby kotów przez 10.
Podpowiedź 2
Odmiana słowa "kot" wygląda inaczej dla 12/13/14."""


def ala_cats_mom(number):
    if number == 1:
        x = 'kota'
    elif number % 10 not in [2, 3, 4] or (11 <= number <= 14):
        x = 'kotów'
    else:
        x = 'koty'
    print(f'Ala ma {number} ' + x + '.')


if __name__ == '__main__':
    ala_cats_mom(1)
