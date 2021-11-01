"""Zadanie 2: HP - drukarka czy programistyczny czarodziej?
Ten-którego-imię-można-wymawiać potrafił rozmawiać z wężami. Pora by wykorzystał Pythona, by ulżyć sobie w trakcie
 wykonywania karnej pracy.
Napisz program, który będzie wyświetlał zadane zdanie, co trzecie będzie napisane wielkimi literami, a co 4 będzie
 posiadało wykrzyknik na swoim końcu. (Tylko nie opowiadaj kłamstw! ;)
Podpowiedź
Dobrym pomysłem będzie stworzenie dodatkowego stringa - kopii powtarzanego zdania, który w zależności od sytuacji
 otrzyma dodatkowy znak na końcu, bądź też zostanie napisany wielkimi literami."""


def hp(sentence, number):
    string3 = sentence.upper()
    string4 = sentence + '!'
    counter = 1
    while counter <= number:
        if counter % 3 == 0:
            print(string3)
        elif counter % 4 == 0:
            print(string4)
        else:
            print(sentence)

        counter += 1


if __name__ == '__main__':
    text = 'Ten-którego-imię-można-wymawiać potrafił rozmawiać z wężami'
    liczba = 21
    hp(text, liczba)
