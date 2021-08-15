def createLists(oriented = False):
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
    for i in range (len(AdjacentList)):
        AdjacentList[i].sort()
    return AdjacentList


def BFS(startNode):
    global AdjacentLists, n
    BFTree = [startNode]
    viz = [0 for i in range(n)]
    viz[startNode - 1] = 1
    coada = [startNode]
    while coada:
        for vecin in AdjacentLists[coada[0] - 1]:
            if viz[vecin - 1] == 0:
                coada.append(vecin)
                viz[vecin - 1] = 1
                BFTree.append(vecin)
        coada.pop(0)
    return BFTree

def DFS(startNode):
    global AdjacentLists, n, viz
    stack = [startNode]
    DFTree = [startNode]
    viz[startNode - 1] = 1
    while stack:
        ok = 0
        for vecin in AdjacentLists[stack[-1] - 1]:
            if viz[vecin - 1] == 0:
                stack.append(vecin)
                DFTree.append(vecin)
                viz[vecin - 1] = 1
                ok = 1
                break
        if not ok:
            stack.pop()
    return DFTree

# main
oriented = False
AdjacentLists = createLists(oriented)
viz = [0 for i in range(n)]
# BFSTree = BFS(1)
# DFSTree = DFS(1)
node = int(input("Nod: "))