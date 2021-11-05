"""Zadanie 2: Wywróćmy świat do góry nogami.
Napisz funkcję (lub program), która wyświetli tekst z dowolnego pliku tekstowego zamieniając przy tym małe litery na
 duże, a duże na małe."""
import os


def swap_case(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        text = text.swapcase()
        print(text)


if __name__ == '__main__':
    home = os.getcwd()
    path = 'text_to_chang'
    file_path = os.path.join(home, path)
    swap_case(file_path)
