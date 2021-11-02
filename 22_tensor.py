"""Zadanie 2: 3DTensor -> Wektor
Napisz funkcję (lub program), która spłaszczy tensor do listy jednowymiarowej. Tensor - definicja.
Dane do zadania
Zadany tensor:
tensor = [[[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]]]
Podpowiedź
Z pewnością przyda się kilka zagnieżdzonych pętli."""


def flatten_tensor(tensor):
    vector = []

    for matrix in tensor:
        for row in matrix:
            for element in row:
                vector.append(element)
    return vector


if __name__ == '__main__':
    tensor1 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
              [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    print(flatten_tensor(tensor1))
