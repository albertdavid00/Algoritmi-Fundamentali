import math
from heapq import heappush, heapify, heappop


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


Edges = []
oriented = False
AdjacentLists = createLists(oriented)
startNode = 1
viz = [0 for i in range(n)]
d = [math.inf for i in range(n)]
tata = [0 for i in range(n)]
d[startNode - 1] = 0

heap = []
heapify(heap)
heappush(heap, (0, 0, 1))
for i in range(1, n):
    heappush(heap, (math.inf, 0, i + 1))        # weight, parent, node

totalWeight = 0
PrimTree = []
while heap:
    tuplu = heappop(heap)
    node = tuplu[2]
    if viz[node - 1] == 0:
        viz[node - 1] = 1
        totalWeight += tuplu[0]
        PrimTree.append((tuplu[1], tuplu[2], tuplu[0]))
        for adj in AdjacentLists[node - 1]:
            if viz[adj[0] - 1] == 0 and adj[1] < d[adj[0] - 1]:
                d[adj[0] - 1] = adj[1]
                tata[adj[0] - 1] = node
                heappush(heap, (d[adj[0] - 1], node, adj[0]))

# for i in range(0,n):
#     print(tata[i], i + 1)
print("Cost total:", totalWeight)
print("Numar muchii:", n - 1)
PrimTree.pop(0)
for edge in PrimTree:
    print(edge[0], edge[1], "cost:", edge[2])
