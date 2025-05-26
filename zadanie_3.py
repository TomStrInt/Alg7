#blur srednia

#DFS (4-kierunkowe sąsiedztwo)

def flood_fill_dfs(image, x, y, new_color, directions):
    rows, cols = len(image), len(image[0])
    old_color = image[x][y]

    if old_color == new_color:  
        return

    def dfs(i, j):
        if not (0 <= i < rows and 0 <= j < cols) or image[i][j] != old_color:
            return

        image[i][j] = new_color

        for di, dj in directions:
            dfs(i + di, j + dj)

    dfs(x, y)

def get_average(x, y, im):
        suma = 0
        licznik = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:  # Sprawdzenie granic
                    suma += im[nx][ny]
                    licznik += 1
        return suma // licznik  # Średnia wartość


image = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]
start_x, start_y = 0, 0
average = get_average
new_color = average
print("\n")
print(average)
directions_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Prawo, dół, lewo, góra

flood_fill_dfs(image, start_x, start_y, new_color, directions_4)

print("DFS - Zmieniony obraz:  ")
for row in image:
    print(row)