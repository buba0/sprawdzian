a = [7,4,15,2,6]
def min(lista):
    if len(lista) == 0:
        return None
    min_wartosc = lista[0]
    for liczba in lista:
        if liczba < min_wartosc:
            min_wartosc = liczba
    return min_wartosc
def max(lista):
    if len(lista) == 0:
        return None
    max_wartosc = lista[0]
    for liczba in lista:
        if liczba > max_wartosc:
            max_wartosc = liczba
    return max_wartosc


parzyste = [liczba for liczba in a if liczba % 2 ==0]
nieparzyste = [liczba for liczba in a if liczba % 2 !=0]
najmniejsza_p = min(parzyste, default=None)
najwieksza_np = max(nieparzyste, default=None)
print(najmniejsza_p)
print(najwieksza_np)
