def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, Edges, grad
    f = open("colorare.in", "r")
    n, m = [int(x) for x in f.readline().split()]
    AdjacentList = [[] for i in range(n)]
    grad = [0 for i in range(n)]
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        Edges.append((aux[0], aux[1]))
        AdjacentList[aux[0] - 1].append(aux[1])
        grad[aux[0] - 1] += 1
        if not oriented:
            AdjacentList[aux[1] - 1].append(aux[0])
            grad[aux[1] - 1] += 1
    for i in range(len(AdjacentList)):
        AdjacentList[i].sort()
    return AdjacentList


def colorare():
    global culori
    stiva = []
    while coada:
        nod = coada[0]
        coada.pop(0)
        stiva.append(nod)
        for vecin in AdjacentLists[nod]:
            grad[vecin - 1] -= 1
            if grad[vecin - 1] == 5:
                coada.append(vecin - 1)
    while stiva:
        nod = stiva[-1]
        stiva.pop()
        for i in range(1, 6):
            culori[i] = 0
        for vecin in AdjacentLists[nod]:
            culori[color[vecin - 1]] = 1
        for i in range(6):
            if culori[i] == 0:
                color[nod] = i
                break
Edges = []
oriented = False
grad = []
coada = []
culori = [0 for i in range(6)]
AdjacentLists = createLists(oriented)
for i in range(n):
    if grad[i] <= 5:
        coada.append(i)
color = [0 for i in range(n)]
colorare()
for i in range(n):
    print(color[i], end=" ")
