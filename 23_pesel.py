"""Zadanie 3: Sprawdź swój Pesel!
Napisz funkcję (lub program), która sprawdzi czy podany Pesel posiada poprawną sumę kontrolną.
Uwaga
Zadanie nie zakłada pełnego sprawdzania prawidłości podanego Peselu"""


def check_pesel_correctness(pesel):
    pesel_list = [int(number) for number in str(pesel)]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    if len(pesel_list) != 11:
        return False

    control_sum = sum([a*b for a, b in zip(pesel_list[:-1], weights)])

    control_number = 10 - [int(number) for number in str(control_sum)][-1]

    print(control_number)

    if pesel_list[-1] != control_number:
        return False

    return True


if __name__ == '__main__':
    pesel = '02070803628'
    print(check_pesel_correctness(pesel))
