def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, Edges

    f = open("graf.in", "r")
    n, m = [int(x) for x in f.readline().split()]
    AdjacentList = [[] for i in range(n)]
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        Edges.append((aux[0], aux[1], aux[2]))
        AdjacentList[aux[0] - 1].append((aux[1], aux[2]))
        if not oriented:
            AdjacentList[aux[1] - 1].append((aux[0], aux[2]))
    for i in range(len(AdjacentList)):
        AdjacentList[i].sort()
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

Edges = []
oriented = False
AdjacentLists = createLists(oriented)
Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
tata = [0 for i in range(n)]  # initializez lista de tati
height = [0 for i in range(n)]  # inaltimile
nrmsel = 0
TreeEdges = []
for edge in Edges:
    if Reprez(edge[0]) != Reprez(edge[1]):
        TreeEdges.append(edge)
        Unite(edge[0], edge[1])
        nrmsel += 1
        if nrmsel == n - 1:
            break

total = sum(map(lambda x: int(x[2]), TreeEdges))
print(total)
for edge in TreeEdges:
    print(edge)
