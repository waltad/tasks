"""Zadanie 1: Numerowanie plików w katalogu
Napisz program, który wyświetli listę plików znajdujących się w zadanym katalogu i doda numer porządkujący na końcu nazwy pliku.
Uwaga
Rozszerzenie pliku musi pozostać niezmienione! Skorzystaj z biblioteki os."""
import os


def numerate_files(filepath):
    for index, file in enumerate(os.listdir(filepath)):
        with open(file, mode='r') as f:
            file_name, extension = f.split('.')
            os.rename(filepath, f, file_name + f'_{index}', extension)


if __name__ == '__main__':
    file_path = 'TEST'
    numerate_files(file_path)
