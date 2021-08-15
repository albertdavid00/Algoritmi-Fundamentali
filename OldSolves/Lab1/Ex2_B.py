def BFS(x):
    global matrix, n, m
    startNode = x
    coada = [x]
    viz = [x]
    sol = []
    SOLFINAL = []
    while coada:
        vecini = []
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
            if vecin not in viz:
                if matrix[vecin[0] - 1][vecin[1] - 1] == 1:
                    sol.extend(vecin)
                    break
                viz.append(vecin)
                coada.append(vecin)
        if sol:
            dist = abs(startNode[0] - sol[0]) + abs(startNode[1] - sol[1])
            SOLFINAL.append(dist)
            SOLFINAL.append(sol)
            break
        coada.pop(0)
    return SOLFINAL

f = open("graf2B.in", "r")
n, m = [int(x) for x in f.readline().split()]
matrix = []
for i in range(n):
    line = [int(x) for x in f.readline().split()]
    matrix.append(line)
points = []
for line in f.readlines():
    points.append(tuple([int(x) for x in line.split()]))

for x in points:
    print(x, end=": ")
    print(*(BFS(x)))
