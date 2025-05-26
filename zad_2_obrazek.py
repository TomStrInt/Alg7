from PIL import Image
from collections import deque

def flood_fill_dfs(image, x, y, new_color):
    pixels = image.load()
    width, height = image.size
    old_color = pixels[x, y]

    if old_color == new_color:
        return
    
    def dfs(i, j):
        if not (0 <= i < width and 0 <= j < height) or pixels[i, j] != old_color:
            return
        
        pixels[i, j] = new_color

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4-kierunkowe sąsiedztwo
            dfs(i + di, j + dj)

    dfs(x, y)

def flood_fill_bfs(image, x, y, new_color):
    pixels = image.load()
    width, height = image.size
    old_color = pixels[x, y]

    if old_color == new_color:
        return

    queue = deque([(x, y)])

    while queue:
        i, j = queue.popleft()
        if not (0 <= i < width and 0 <= j < height) or pixels[i, j] != old_color:
            continue

        pixels[i, j] = new_color

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4-kierunkowe sąsiedztwo
            queue.append((i + di, j + dj))

# Przetwarzanie obrazu
image = Image.open("obrazek.jpg").convert("RGB")  # Konwersja na RGB
start_x, start_y = 10, 50  # Punkt startowy !!!
new_color = (255, 10, 0)  # Czerwony !!!

# flood_fill_dfs(image, start_x, start_y, new_color)  # Użyj DFS
flood_fill_bfs(image, start_x, start_y, new_color)  # Użyj BFS

image.save("obrazek_wynik.jpg")  # Zapis zmienionego obrazka
image.show()  # Wyświetlenie 
