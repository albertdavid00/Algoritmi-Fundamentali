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
    global reprez
    return reprez[node - 1]


def Unite(u, v):
    global reprez
    r1 = Reprez(u)
    r2 = Reprez(v)  # ar mai trebui o verificare pentru height
    for k in range(n):
        if reprez[k] == r2:
            reprez[k] = r1


Edges = []
oriented = False
AdjacentLists = createLists(oriented)
Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
reprez = [i for i in range(n)]

nrmsel = 0
TreeEdges = []
for edge in Edges:
    if Reprez(edge[0]) != Reprez(edge[1]):
        TreeEdges.append(edge)
        Unite(edge[0], edge[1])
        nrmsel += 1
        if nrmsel == n - 1:
            break
