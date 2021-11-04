"""Zadanie 3: Sprawdź swój Pesel!
Napisz funkcję (lub program), która sprawdzi czy podany Pesel posiada poprawną sumę kontrolną.

Co oznaczają poszczególne cyfry w numerze PESEL
Każda z 11 cyfr w numerze PESEL ma swoje znaczenie. Można je podzielić następująco:
RRMMDDPPPPK
RR - to 2 ostanie cyfry roku urodzenia,
MM - to miesiąc urodzenia (zapoznaj się z sekcją  "Dlaczego osoby urodzone po 1999 roku mają inne oznaczenie miesiąca
    urodzenia", która znajduje się poniżej),
DD - to dzień urodzenia,
PPPP - to liczba porządkowa oznaczająca płeć. U kobiety ostatnia cyfra tej liczby jest parzysta (0, 2, 4, 6, 8), a u
    mężczyzny - nieparzysta (1, 3, 5, 7, 9),
K - to cyfra kontrolna.
Przykład: PESEL 810203PPP6K należy do kobiety, która urodziła się 3 lutego 1981 roku, a PESEL 761115PPP3K - do mężczyzny,
który urodził się 15 listopada 1976 roku.

W jaki sposób można obliczyć cyfrę kontrolną
W 3 prostych krokach opiszemy poniżej, w jaki sposób można obliczyć cyfrę kontrolną w numerze PESEL. Jako przykład
 posłuży nam numer 0207080362.

Pomnóż każdą cyfrę z numeru PESEL przez odpowiednią wagę: 1-3-7-9-1-3-7-9-1-3.
0 * 1 = 0
2 * 3 = 6
0 * 7 = 0
7 * 9 = 63
0 * 1 = 0
8 * 3 = 24
0 * 7 = 0
3 * 9 = 27
6 * 1 = 6
2 * 3 = 6

Dodaj do siebie otrzymane wyniki. Uwaga, jeśli w trakcie mnożenia otrzymasz liczbę dwucyfrową, należy dodać tylko
 ostatnią cyfrę (na przykład zamiast 63 dodaj 3).
0 + 6 + 0 + 3 + 0 + 4 + 0 + 7 +6 + 6 = 32
Odejmij uzyskany wynik od 10. Uwaga: jeśli w trakcie dodawania otrzymasz liczbę dwucyfrową, należy odjąć tylko ostatnią
 cyfrę (na przykład zamiast 32 odejmij 2). Cyfra, która uzyskasz, to cyfra kontrolna. 10 - 2 = 8
pełny numer PESEL: 02070803628
Uwaga
Zadanie nie zakłada pełnego sprawdzania prawidłości podanego Peselu"""


def check_pesel_correctness(pesel):
    pesel_list = [int(number) for number in str(pesel)]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    if len(pesel_list) != 11:
        return False

    control_sum = sum([a*b for a, b in zip(pesel_list[:-1], weights)])

    # control_number = 10 - [int(number) for number in str(control_sum)][-1]
    control_number = 10 - int(str(control_sum)[-1])

    print(control_number)

    if pesel_list[-1] != control_number:
        return False

    return True


if __name__ == '__main__':
    pesel = '02070803628'
    print(check_pesel_correctness(pesel))
