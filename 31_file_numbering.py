"""Zadanie 1: Numerowanie plików w katalogu
Napisz program, który wyświetli listę plików znajdujących się w zadanym katalogu i doda numer porządkujący na końcu nazwy pliku.
Uwaga
Rozszerzenie pliku musi pozostać niezmienione! Skorzystaj z biblioteki os."""
import os


def numerate_files(filepath):
    os.chdir(filepath)
    for index, file in enumerate(os.listdir(filepath)):
        with open(file, mode='r') as f:
            file_name, extension = file.split('.')
            os.rename(file, file_name + f'_{index}.{extension}')


if __name__ == '__main__':
    here_path = os.getcwd()
    directory = "TEST"
    file_path = os.path.join(here_path, directory)
    numerate_files(file_path)
