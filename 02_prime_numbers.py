"""Napisz program, który sprawdza czy zadaną liczbę poprzedza w kolejności liczba pierwsza.
Ważne
Sprawdzając czy liczba n jest liczbą pierwszą nie trzeba sprawdzać potencjalnych dzielników od 2 do n. Można dramtycznie
 zmniejszyć ilość porównań sprawdzając jedynie od 2 do √(n) (pierwiastek z n).
Przykład:
Postarajmy się znaleźć wszystkie dzielniki liczby 100 i wylistować je w formie tabeli:
2  x  50 = 100
4  x  25 = 100
5  x  20 = 100
10  x  10 = 100 <-- √(100)
20  x  5  = 100
25  x  4  = 100
50  x  2  = 100
Można zaobserwować, że wraz z osiągnięciem √(100) wszystkie dzielniki zostały już znalezione. Ta właściwość ma
zastosowanie dla dowolnej wartości n."""
from math import sqrt, floor


def previous_is_prime_number(number):
    number -= 1
    square_root = int(sqrt(number)) + 1
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False

    for divisor in range(3, square_root, 2):
        if number % divisor == 0:
            return False

    return True


if __name__ == '__main__':
    print(previous_is_prime_number(18))
