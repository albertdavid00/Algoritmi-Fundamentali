#  Determinarea de drumuri minime din parcurgerea BF

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
    controlPoints = [int(x) for x in f.readline().split()]
    return AdjacentList


def BFS(startNode):
    global AdjacentLists, n, niv, viz, tata
    BFTree = [startNode]
    viz = [0 for i in range(n)]
    niv = [0 for i in range(n)]
    tata = [0 for i in range(n)]
    viz[startNode - 1] = 1
    coada = [startNode]
    while coada:
        for vecin in AdjacentLists[coada[0] - 1]:
            if viz[vecin - 1] == 0:
                coada.append(vecin)
                niv[vecin - 1] = niv[coada[0] - 1] + 1
                viz[vecin - 1] = 1
                tata[vecin - 1] = coada[0]
                BFTree.append(vecin)

        coada.pop(0)
    return BFTree


oriented = True
AdjacentLists = createLists(oriented)
node = int(input("Nod: "))
BFS(node)
Sol = []
Min = -1
ok = 0
for x in controlPoints:         # parcurg nodurile care sunt puncte de control
    if viz[x-1] == 1:           # si pentru fiecare aflu drumul, daca este minim il adaug in solutie
        ok = 1
        i = x - 1
        lant = [i + 1]
        while tata[i]:
            i = tata[i] - 1
            lant.append(i + 1)
        if Min == -1:
            Min = len(lant)
            Sol.extend(lant)
        elif len(lant) < Min:
            Sol.clear()
            Sol.extend(lant)
if ok == 0:
     print("Nu exista drum")
else:
    print(Sol[0])
    Sol.reverse()
    print(Sol)