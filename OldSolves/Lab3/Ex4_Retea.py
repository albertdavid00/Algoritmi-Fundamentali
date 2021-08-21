import math


def euclid(node1, node2):
    global Coords
    a = (Coords[node1][0] - Coords[node2][0]) ** 2
    b = (Coords[node1][1] - Coords[node2][1]) ** 2
    return math.sqrt(a + b)


def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, e, Coords, Edges
    f = open("retea2.in", "r")
    n, m, e = [int(x) for x in f.readline().split()]
    for i in range(n + m):
        x, y = [int(x) for x in f.readline().split()]
        Coords.append((x, y))
    AdjacentList = [[] for i in range(n + m)]
    for i in range(e):
        aux = [int(x) for x in f.readline().split()]
        dist = euclid(aux[0] - 1, aux[1] - 1)
        Edges.append((aux[0], aux[1], dist))
        AdjacentList[aux[0] - 1].append((aux[1], dist))  # node dist
        if not oriented:
            aux.reverse()
            AdjacentList[aux[0] - 1].append((aux[1], dist))
    for i in range(len(AdjacentList)):
        AdjacentList[i].sort(key=lambda e: e[0])
    return AdjacentList


def Reprez(node):
    global tata
    while tata[node - 1] != 0:
        node = tata[node - 1]
    return node


def Unite(u, v):
    global tata, height
    ru = Reprez(u)
    rv = Reprez(v)
    if height[ru - 1] > height[rv - 1]:
        tata[rv - 1] = ru
    else:
        tata[ru - 1] = rv
        if height[ru - 1] == height[rv - 1]:
            height[rv - 1] = height[rv - 1] + 1


oriented = False
Coords = []
Edges = []
AdjacentLists = createLists(oriented)

Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
tata = [0 for i in range(n + m)]  # initializez lista de tati
height = [0 for i in range(n + m)]  # inaltimile
nrmsel = 0
TreeEdges = []
for i in range(1, n):
    tata[i] = 1
for i in range(n):
    height[i] = 1
for edge in Edges:
    if Reprez(edge[0]) != Reprez(edge[1]):
        TreeEdges.append(edge)
        Unite(edge[0], edge[1])
        nrmsel += 1
        if nrmsel == m:
            break

total = sum(map(lambda x: int(x[2]), TreeEdges))
print(total)
for edge in TreeEdges:
    print(edge)
