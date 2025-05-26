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


#LABIRYNT

def znajdowanie_sciezki(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def dfs(x, y):
        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or visited[x][y]:
            return False
        
        visited[x][y] = True
        path.append((x, y))

        if (x, y) == end:
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if dfs(x + dx, y + dy):
                return True
        
        path.pop()
        return False

    return path if dfs(start[0], start[1]) else None
print("\n")

#przykladowy labirynt
maze = [
    [0, 1, 0, 0],   #0
    [0, 0, 0, 1],   #1
    [1, 1, 0, 0],   #2
    [0, 0, 0, 0]    #3
]
    #0  1  2  3
start = (0, 0)
end = (3, 3)

sciezka = znajdowanie_sciezki(maze, start, end)
print("Znaleziono ścieżkę:", sciezka)

