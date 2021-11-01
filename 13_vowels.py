"""Zadanie 3: Aaaaaa - czyli 6.
Napisz funkcję (lub program), która określi ilość samogłosek występujących w zadanym stringu.
Ważne
Spróbuj w swoim zadaniu wykorzystać Countera.
Podpowiedź
Warto zapisać poszukiwane samogłoski w postaci np. zbioru samogłosek."""
from collections import Counter


def vowels_number(sentence):
    vowels = ['a', 'ą', 'A', 'Ą', 'e', 'ę', 'E', 'Ę', 'i', 'I', 'o', 'ó', 'O', 'Ó', 'u', 'U', 'y', 'Y']
    counter = 0
    for vowel in vowels:
        counter += sentence.count(vowel)
    print(f'There are {counter} vowels in this string.')


def count_vowel(string):
    vowels = {'a', 'ą', 'A', 'Ą', 'e', 'ę', 'E', 'Ę', 'i', 'I', 'o', 'ó', 'O', 'Ó', 'u', 'U', 'y', 'Y'}

    counter = Counter(string)
    sum = 0
    for key, item in counter.items():
        if key in vowels:
            sum += item

    return sum


if __name__ == '__main__':
    text = 'Ważne: Spróbuj w swoim zadaniu wykorzystać Countera. Podpowiedź: Warto zapisać poszukiwane samogłoski w' \
           ' postaci np. zbioru samogłosek.'
    vowels_number(text)

print(count_vowel(text))
