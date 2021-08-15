import math
def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, Edges

    f = open("grafpond.in", "r")
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

def BFS(startNode, Node2, cost):
    global AdjacentLists, n, niv, viz, parent
    BFTree = [startNode]
    viz = [0 for i in range(n)]
    niv = [0 for i in range(n)]
    parent = [0 for i in range(n)]  # fiecare nod are o lista de posibili tati
    viz[startNode - 1] = 1
    coada = [startNode]
    stop = False
    while coada:
        for vecin in NewAdj[coada[0] - 1]:               # avem -1 de la numerotarea nodurilor
            if viz[vecin[0] - 1] == 0:
                coada.append(vecin[0])
                niv[vecin[0] - 1] = niv[coada[0] - 1] + 1
                viz[vecin[0] - 1] = 1
                parent[vecin[0] - 1] = coada[0]
                BFTree.append(vecin[0])
                if vecin[0] == Node2:
                    stop = True
                    break
        if stop == True:
            break
        coada.pop(0)
    muchii = []
    for adj in NewAdj[Node2 - 1]:
        if adj[0] == parent[Node2 - 1]:
            muchii.append((Node2, parent[Node2], adj[1]))
    while parent[Node2 - 1] != 0:
        Node2 = parent[Node2 - 1]
        for adj in NewAdj[Node2 - 1]:
            if adj[0] == parent[Node2 - 1]:
                muchii.append((Node2, parent[Node2 - 1], adj[1]))
    Max = max(map(lambda x: x[2], muchii))
    for edge in muchii:
        if edge[2] == Max:
            return edge

Edges = []
oriented = False
AdjacentLists = createLists(oriented)
Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
tata = [0 for i in range(n)]  # initializez lista de tati
height = [0 for i in range(n)]  # inaltimile
NewAdj = [[] for i in range(n)]
nrmsel = 0
TreeEdges = []
minDif = math.inf
EdgesPair = []
maxEdge = []
check = False
for edge in Edges:
    if nrmsel < n - 1:
        if Reprez(edge[0]) != Reprez(edge[1]):
            TreeEdges.append(edge)
            Unite(edge[0], edge[1])
            nrmsel += 1
        # if nrmsel == n - 1:
        #     break
    else:
        if check == False:
            for e in TreeEdges:
                NewAdj[e[0] - 1].append((e[1], e[2]))
                if not oriented:
                    NewAdj[e[1] - 1].append((e[0], e[2]))
            check = True
        k = nrmsel - 1
        while k > - 1:
            maxEdge = BFS(edge[0], edge[1], edge[2])
            if minDif > edge[2] - maxEdge[2]:
                minDif = edge[2] - maxEdge[2]
                EdgesPair.clear()
                EdgesPair.append(maxEdge)
                EdgesPair.append(edge)
            k -= 1

print("Best")
total = sum(map(lambda x: int(x[2]), TreeEdges))
print(total)
for edge in TreeEdges:
    print(edge)

print("Second best")
for edge in TreeEdges:
    if (edge[0] == EdgesPair[0][0] or edge[0] == EdgesPair[0][1]) and (edge[1] == EdgesPair[0][0] or edge[1] == EdgesPair[0][1]):
        TreeEdges.remove(edge)
TreeEdges.append(EdgesPair[1])
total = sum(map(lambda x: int(x[2]), TreeEdges))
print(total)
for edge in TreeEdges:
    print(edge)