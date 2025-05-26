#DFS (4-kierunkowe sąsiedztwo)

def flood_fill_dfs(image, x, y, new_color, directions):
    rows, cols = len(image), len(image[0])
    old_color = image[x][y]

    if old_color == new_color:  # Jeśli kolor jest już zmieniony, nie wykonujemy ponownie operacji
        return

    def dfs(i, j):
        if not (0 <= i < rows and 0 <= j < cols) or image[i][j] != old_color:
            return

        image[i][j] = new_color

        for di, dj in directions:
            dfs(i + di, j + dj)

    dfs(x, y)


image = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]
start_x, start_y = 0, 0
new_color = 2
directions_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Prawo, dół, lewo, góra

flood_fill_dfs(image, start_x, start_y, new_color, directions_4)

print("DFS - Zmieniony obraz:  ")
for row in image:
    print(row)


#BFS (8-kierunkowe sąsiedztwo)

from collections import deque

def flood_fill_bfs(image, x, y, new_color, directions):
    rows, cols = len(image), len(image[0])
    old_color = image[x][y]

    if old_color == new_color:
        return

    queue = deque([(x, y)])

    while queue:
        i, j = queue.popleft()
        if not (0 <= i < rows and 0 <= j < cols) or image[i][j] != old_color:
            continue

        image[i][j] = new_color

        for di, dj in directions:
            queue.append((i + di, j + dj))



image = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]
start_x, start_y = 0, 0
new_color = 3
directions_8 = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

flood_fill_bfs(image, start_x, start_y, new_color, directions_8)

print("BFS - Zmieniony obraz:   ")
for row in image:
    print(row)
