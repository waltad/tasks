"""Zadanie 3: Tańczące parabole
Napisz funkcję (lub program), która obliczy miejsca zerowe zadanej funkcji kwadratowej. W tym celu można skorzystać
z przedstawionych tutaj wzorów:
Jeśli masz postać ogólną funkcji kwadratowej: y=ax2+bx+c najczęściej miejsca zerowe oblicza się przez wyznaczenie współczynników a,b,c przy kolejnych potęgach x.

2) Znając wzór na wyróżnik trójmianu kwadratowego (wzór na deltę)
Δ=b2−4⋅a⋅c
obliczasz wartość delty, a następnie wybierasz jedną z trzech możliwości:

jeśli Δ > 0 wówczas mamy dwa miejsca zerowe:
x1=(−b−√Δ)/2⋅a
x2=(−b+√Δ)/2⋅a
jeśli Δ = 0 wówczas mamy jedno miejsce zerowe o wzorze:
x0=−b2⋅a
jeśli Δ < 0 to brak miejsc zerowych
Uwaga
Zakładamy poruszanie się jedynie w przestrzeni liczb rzeczywistych, rozwiązania zespolone nie są wymagane.
Podpowiedź
W celu realizacji zadania najlepiej stworzyć funkcję, która przyjmie 3 argumenty będące współczynnikami równania funkcji
 kwadratowej. Przyda się również biblioteka math do obliczenia pierwiastka."""