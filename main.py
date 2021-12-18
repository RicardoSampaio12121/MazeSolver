from collections import deque


def mazeSolver(maze):
    Rows = len(maze)
    Columns = len(maze[0])

    #TODO: Se algum de voçês tiver tempo tentem pôr esta parte do código mais "bonita" -Ricardo

    # Procura a posição inicial
    startPos = (0, 0)
    for r in range(Rows):
        for c in range(Columns):
            if maze[r][c] == 'E':
                startPos = (r, c)
                break
        else:
            continue
        break
    else:
        return None

    # [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 9], [3, 9], [4, 9], [4, 10], [4, 11], [5, 11], [5, 12], [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [13, 13], [14, 13]]
    # Cria a queue e adiciona-lhe a posição inicial
    # Define as operações possiveis, no caso, [0, 1] = coluna para a direita
    # [0, -1] coluna para a esquerda
    # [1, 0] Linha para cima
    # [-1, 0] Linha para baixo
    # Criamos também uma lista para guardar as posições já visitadas
    queue = deque()
    queue.appendleft((startPos[0], startPos[1], 0, [startPos[0] * Columns + startPos[1]]))
    operations = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = []

    for _ in range(Rows):
        temp = []
        for __ in range(Columns):
            temp.append(False)
        visited.append(temp)

    # O programa corre enquanto houver "jogadas"
    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        path = []
        if maze[coord[0]][coord[1]] == "S":
            for i in coord[3]:
                path.append([i // Columns, i % Columns])

            return coord[2], path

        for direction in operations:
            nr = coord[0] + direction[0]
            nc = coord[1] + direction[1]

            # Verifica se a coordenada atual na matriz mais a direção para onde vai é uma parede, já foi visitado ou se está fora da matriz
            if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or maze[nr][nc] == "#" or visited[nr][nc]: continue
            queue.appendleft((nr, nc, coord[2] + 1, coord[3] + [nr * Columns + nc]))


with open("maze2.txt") as f:
    maze = []
    for line in f:
        maze.append([i for i in line.strip("\n")])
    pathLen, pathItems = mazeSolver(maze)

    for cord in pathItems:
        if maze[cord[0]][cord[1]] != "E" and maze[cord[0]][cord[1]] != "S":
            maze[cord[0]][cord[1]] = "A"

    print("Número de operações necessárias:", pathLen)
    print("Coordenadas na matriz:", *pathItems)

    for line in maze:
        print(line)
