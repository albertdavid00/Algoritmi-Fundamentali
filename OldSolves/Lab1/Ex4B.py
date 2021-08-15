def createLists(oriented=False):            # functie pentru crearea listei de adiacenta
    global n, m, controlPoints
    f = open("graf.in", "r")
    n, m = [int(x) for x in f.readline().split()]
    AdjacentList = [[] for i in range(n)]
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        AdjacentList[aux[0] - 1].append(aux[1])
        if not oriented:
            aux.reverse()
            AdjacentList[aux[0] - 1].append((aux[1]))
    for i in range(len(AdjacentList)):
        AdjacentList[i].sort()
   # controlPoints = [int(x) for x in f.readline().split()]  # n am nevoie de astea
    return AdjacentList

def BFS(startNode):
    global AdjacentLists, n, niv, viz, tata
    BFTree = [startNode]
    viz = [0 for i in range(n)]
    niv = [0 for i in range(n)]
    tata = [ [] for i in range(n)]  # fiecare nod are o lista de posibili tati
    tata[startNode - 1].append(0)   # nodul de start nu are tata
    viz[startNode - 1] = 1
    coada = [startNode]
    while coada:
        for vecin in AdjacentLists[coada[0] - 1]:               # avem -1 de la numerotarea nodurilor
            if viz[vecin - 1] == 0:
                coada.append(vecin)
                niv[vecin - 1] = niv[coada[0] - 1] + 1
                viz[vecin - 1] = 1
                tata[vecin - 1].append(coada[0])
                BFTree.append(vecin)
            elif niv[coada[0] - 1] < niv[vecin - 1]:
                tata[vecin - 1].append(coada[0])
        coada.pop(0)
    return BFTree

def SearchPath(node):
    global fNode
    for t in tata[node]:
        if t == 0:
            print(fNode, *minPaths[k])
            return
        else:
            minPaths[k].append(t)
            SearchPath(t - 1)
            minPaths[k].pop()

oriented = False
AdjacentLists = createLists(oriented)
sNode = int(input("Nod start: "))
fNode = int(input("Nod final: "))
BFTree = BFS(sNode)
minPaths = [[]]
k = 0
for x in tata[fNode - 1]:
    node = x - 1
    minPaths[k].append(x)
    SearchPath(node)
    k += 1
    minPaths.append([])
