def BFS(x):
    global matrix, n, m, tata, Julieta
    startNode = Julieta
    coada = [x]
    viz = [x]
    sol = []
    SOL = []
    tata = {
        x: (0, 0)
    }
    while coada:
        vecini = []
        # diagonala stanga-sus
        if coada[0][0] - 2 >= 0 and coada[0][1] - 2 >= 0:  # verificam daca depaseste marginea superioara a matricei
            coords = (coada[0][0] - 1, coada[0][1] - 1)
            vecini.append(coords)
        #diagonala dreapta-sus
        if coada[0][0] - 2 >= 0 and coada[0][1] < m:  # verificam daca depaseste marginea superioara a matricei
            coords = (coada[0][0] - 1, coada[0][1] + 1)
            vecini.append(coords)
        # diagonala stanga-jos
        if coada[0][0] < n and coada[0][1] - 2 >= 0:  # verificam daca depaseste marginea superioara a matricei
            coords = (coada[0][0] + 1, coada[0][1] - 1)
            vecini.append(coords)
        # diagonala dreapta-jos
        if coada[0][0] < n and coada[0][1] < m:  # verificam daca depaseste marginea superioara a matricei
            coords = (coada[0][0] + 1, coada[0][1] + 1)
            vecini.append(coords)
        # ne uitam in sus
        if coada[0][0] - 2 >= 0:  # verificam daca depaseste marginea superioara a matricei
            coords = (coada[0][0] - 1, coada[0][1])
            vecini.append(coords)
        # in jos
        if coada[0][0] < n:
            coords = (coada[0][0] + 1, coada[0][1])
            vecini.append(coords)
        # la dreapta
        if coada[0][1] < m:
            coords = (coada[0][0], coada[0][1] + 1)
            vecini.append(coords)
        # la stanga
        if coada[0][1] - 2 >= 0:
            coords = (coada[0][0], coada[0][1] - 1)
            vecini.append(coords)
        for vecin in vecini:
            if matrix[vecin[0] - 1][vecin[1] - 1] != 'X':
                if vecin not in viz:
                    if matrix[vecin[0] - 1][vecin[1] - 1] == 'J':
                        sol.extend(vecin)
                        tata.setdefault(vecin, coada[0])
                        break
                    viz.append(vecin)
                    coada.append(vecin)
                    tata.setdefault(vecin, coada[0])
        if sol:
            break
        coada.pop(0)
    while startNode != (0,0):
        SOL.append(startNode)
        startNode = tata[startNode]
    SOLFINAL = [len(SOL)//2 + 1, SOL[len(SOL)//2]]
    return SOLFINAL


f = open("graf3B.in", "r")
n, m = [int(x) for x in f.readline().split()]
matrix = []
for i in range(n):
    line = f.readline().split('\n')
    if i == 0 and len(line[0]) != m:  # semihardcodat
        line[0] += (' ')
    matrix.append(line[0])
Romeo = tuple()
Julieta = tuple()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            Romeo += (i + 1, j + 1)
        if matrix[i][j] == 'J':
            Julieta += (i + 1, j + 1)

print(BFS(Romeo))
