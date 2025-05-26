#PERMUTACJA

def permutacja(s):
    # Warunek brzegowy: pusty ciąg – jedyna permutacja to pusty ciąg.
    if len(s) == 0:
        return [""]

    wynik = []
    # Przechodzimy przez każdy znak w ciągu wraz z jego indeksem
    for i, znak in enumerate(s):
        # Wywołujemy rekurencyjnie funkcję dla ciągu bez i-tego znaku
        for p in permutacja(s[:i] + s[i+1:]):
            wynik.append(znak + p)
    return wynik


ciag = input("Podaj ciag znakow:   ")
'''
print("Permutacje ciągu '{}':".format(ciag))
for p in permutacja(ciag):
    print(p)
'''
print("Permutacje ciągu  '{}':".format(ciag), permutacja(ciag))


#ZAPIS BINARNY LICZBY CALKOWITEJ

def zapis_binarny(n):
    if n < 0:
        return '-' + zapis_binarny(-n)
    if n < 2:
        return str(n)
    return zapis_binarny(n // 2) + str(n % 2)


liczba = int(input("Podaj liczbe calkowita (w zapisie dziesietnym):    "))
print("Zapis binarny liczby {}: {}".format(liczba, zapis_binarny(liczba)))


#
