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
oriented = True
AdjacentLists = createLists(oriented)
startNode = 1
viz = [0 for i in range(n)]
d = [math.inf for i in range(n)]
tata = [0 for i in range(n)]
d[startNode - 1] = 0

for i in range(1, n):
    for edge in Edges:
        if d[edge[0] - 1] + edge[2] < d[edge[1] - 1]:
            d[edge[1] - 1] = d[edge[0] - 1] + edge[2]
            tata[edge[1] - 1] = edge[0]

# detectare circuit negativ
for edge in Edges:
    if d[edge[0] - 1] + edge[2] < d[edge[1] - 1]:
        d[edge[1] - 1] = d[edge[0] - 1] + edge[2]
        tata[edge[1] - 1] = edge[0]
        print("Stop")
        break
