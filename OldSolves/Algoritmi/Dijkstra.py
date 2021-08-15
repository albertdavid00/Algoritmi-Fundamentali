import math
from heapq import heappush, heapify, heappop

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


Edges = []
oriented = False
AdjacentLists = createLists(oriented)
startNode = 1
viz = [0 for i in range(n)]
d = [math.inf for i in range(n)]
tata = [0 for i in range(n)]
d[startNode - 1] = 0

DijkstraTree = []
totalWeight = 0
heap = []
heapify(heap)
heappush(heap, (0, 0, startNode))
for i in range(1, n):
    heappush(heap, (math.inf, 0, i + 1))        # weight, parent, node
while heap:
    tuplu = heappop(heap)
    node = tuplu[2]
    if viz[node - 1] == 0:
        viz[node - 1] = 1
        totalWeight += tuplu[0]
        DijkstraTree.append((tuplu[1], tuplu[2], tuplu[0]))
        for adj in AdjacentLists[node - 1]:     #luam vecin
            if viz[adj[0] - 1] == 0 and adj[1] + d[node - 1] < d[adj[0] - 1]:
                d[adj[0] - 1] = adj[1] + d[node - 1]
                tata[adj[0] - 1] = node
                heappush(heap, (d[adj[0] - 1], node, adj[0]))
DijkstraTree.pop(0)