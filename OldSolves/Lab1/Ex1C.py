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
    global AdjacentLists, n, niv, viz, tata, ciclu
    BFTree = [startNode]
    niv = [0 for i in range(n)]
    tata[startNode - 1] = 0   # nodul de start nu are tata
    viz[startNode - 1] = 1
    coada = [startNode]
    while coada:
        for vecin in AdjacentLists[coada[0] - 1]:               # avem -1 de la numerotarea nodurilor
            if viz[vecin - 1] == 0:
                coada.append(vecin)
                niv[vecin - 1] = niv[coada[0] - 1] + 1
                viz[vecin - 1] = 1
                tata[vecin - 1] = coada[0]
                BFTree.append(vecin)
            elif niv[coada[0] - 1] <= niv[vecin - 1]:       # asta inseamna ca avem ciclu
                ciclu.append(vecin)
                ciclu.append(coada[0])
                return True
        coada.pop(0)
    return BFTree

ciclu = []
oriented = False
AdjacentLists = createLists(oriented)
viz = [0 for i in range(n)]

tata = [-1 for i in range(n)]  # fiecare nod are o lista de posibili tati
nrCompConexe = 0
for node in range (1, n+1):
    if viz[node - 1] == 0:
        nrCompConexe += 1
        check = BFS(node)
        if check == True:
            break
if check == True:
    list1 = []
    list2 = []
    x = ciclu[0] - 1
    while x >= 0:
        list1.append(x + 1)
        x = tata[x] - 1
    y = ciclu[1] - 1
    while y >= 0:
        list2.append(y + 1)
        y = tata[y] - 1
    cicluGraf = []
    nodComun = -1
    for node in list1:
        if node in list2:
            nodComun = node
            break
    list2.reverse()
    for node in list1:
        cicluGraf.append(node)
        if node == nodComun:
            break
    ok = 0
    for node in list2:
        if ok == 1:
            cicluGraf.append(node)
        if node == nodComun:
            ok = 1
    cicluGraf.append(cicluGraf[0])
    print(cicluGraf)