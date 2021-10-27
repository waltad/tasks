"""Napisz program (lub funkcję), który pozwoli na porównanie stosunku pola do ceny pomiędzy dwoma pizzami.
W celu obliczenia pola okręgu P przy zadanym promieniu r - należy posłużyć się wzorem - Wzór.
Znajdź restaurację w Twojej okolicy, wpisz odpowiednie dane i odpowiedz sobie na zadane w poleceniu pytanie.

Ważne
W celu uzyskania dokładnej wartości liczby pi, możesz skorzystać z biblioteki standardowej math
- nie jest to jednak wymagane."""
from math import pi


def two_pizzas():
    diameter1 = float(input('Podaj średnicę pierwszej pizzy w cm: '))
    price1 = float(input('Podaj cenę pierwszej pizzy: '))
    diameter2 = float(input('Podaj średnicę drugiej pizzy w cm: '))
    price2 = float(input('Podaj cenę drugiej pizzy: '))

    average1 = round(price1/(pi*(diameter1/2)**2), 2)
    average2 = round(price2/(pi*(diameter2/2)**2), 2)

    print(f'Centymetr 1 pizzy kosztyje: {average1} zł.\nCentymetr 2 pizzy kosztyje: {average2} zł.')


if __name__ == '__main__':
    two_pizzas()
