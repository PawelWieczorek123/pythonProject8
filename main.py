import timeit
import random




def sito():
    maksiu = 1000000
    tab = [True for x in range(maksiu)]
    tab[0] = False
    tab[1] = False
    wynik = []
    for i in range(2, maksiu):
        if tab[i]:
            for j in range(i * i,maksiu,i):
                tab[j] = False
    for i in range(2,maksiu):
        if tab[i]:
            wynik.append(i)
        return wynik



def pierwsze():
    maksiu = 1000000
    wynik=[]


def czypiersze(liczba):
    if liczba == 1 or liczba == 0:
        return False
    for y in range(2,int(liczba**0.5)+1):
        if liczba%y == 0:
            return False
        return True


liczbypiersze = sito()
def liczbypierwsze():
    for _ in range(1000):
        r = random.randint(1,1000000)
    if r in liczbypierwsze:
        pass



set_liczbypierwsze= set(liczbypiersze)
def szukamyset():
    set_liczbypierwsze=set(liczbypiersze)
    for _ in range(1000000):
        r = random.randint(1,1000000)
    if r in set_liczbypierwsze:
        pass


print(timeit.timeit(stmt= szukamyset,number=1))
print(timeit.timeit(stmt= pierwsze,number=1))

