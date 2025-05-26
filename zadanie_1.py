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
