import math
# Complexitate: O(N+M)
# Contine si ex 2 din lab 2
def createLists(oriented=False):
    global n, m
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
    return AdjacentList

# DFS recursiv
def DFS(i):
    global AdjacentLists, n, viz, niv, niv_min, Bridges, CriticalPoints, startNode, count, stack, Biconexe
    viz[i - 1] = 1
    niv_min[i - 1] = niv[i - 1]
    for vecin in AdjacentLists[i - 1]:
        if viz[vecin - 1] == 0:     # (i,vecin) muchie de avansare
            if startNode == i:
                count += 1
            niv[vecin - 1] = niv[i - 1] + 1
            stack.append((i, vecin))
            DFS(vecin)
            # actualizare niv_min[i] - cazul B
            niv_min[i - 1] = min(niv_min[i - 1], niv_min[vecin - 1])
            # test (i, vecin) este muchie critica
            if niv_min[vecin - 1] > niv[i - 1]:
                Bridges.append((i, vecin))
            if niv_min[vecin - 1] >= niv[i - 1]:    # verif punct critic
                CriticalPoints.add(i)
                lista = []
                while stack[-1] != (i, vecin):
                    lista.append(stack[-1])
                    stack.pop()
                lista.append(stack[-1])
                stack.pop()
                Biconexe.append(lista)
        elif niv[vecin - 1] < niv[i - 1] - 1:   # (i,vecin) muchie de intoarcere
            # actualizare niv_min[i] - cazul A
            niv_min[i - 1] = min(niv_min[i - 1], niv[vecin - 1])
            stack.append((i, vecin))


oriented = False
AdjacentLists = createLists(oriented)
Bridges = []
stack = []
Biconexe = []
CriticalPoints = set()
count = 0
viz = [0 for i in range(n)]
niv = [0 for i in range(n)]
niv_min = [math.inf for i in range(n)]
startNode = 1
df = DFS(startNode)
if count > 1:
    CriticalPoints.add(startNode)
elif startNode in CriticalPoints:
    CriticalPoints.remove(startNode)

print("Legaturi critice:")
for bridge in Bridges:
    print(bridge)

print("Puncte critice:")
for node in CriticalPoints:
    print(node)

print("Componente biconexe:")
maxComp = (max(map(lambda x: len(x), Biconexe)))
for comp in Biconexe:
    noduri = set()
    if len(comp) == maxComp:
        for x in comp:
            noduri.add(x[0])
            noduri.add(x[1])
        print(noduri)
        print(comp)