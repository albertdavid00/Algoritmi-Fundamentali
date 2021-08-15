import math
from heapq import heappush, heapify, heappop


def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, Edges, durata, grad_min, grad_max

    f = open("activitati.in", "r")
    n = int(f.readline())
    for i in range(n):
        grad_min.append(i+1)
        grad_max.append(i+1)
    durata = [int(x) for x in f.readline().split()]
    durata.append(0)
    durata.reverse()
    durata.append(0)
    durata.reverse()
    m = int(f.readline())
    AdjacentList = [[] for i in range(n + 2)]
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        Edges.append((aux[0], aux[1]))
        AdjacentList[aux[0]].append(aux[1])
        if aux[1] in grad_min:
            grad_min.remove(aux[1])
        if aux[0] in grad_max:
            grad_max.remove(aux[0])
        if not oriented:
            AdjacentList[aux[1]].append(aux[0])
    for i in range(len(AdjacentList)):
        AdjacentList[i].sort()
    return AdjacentList



def topologicalSort(node):
    global stack, viz
    viz[node - 1] = 1
    for vecin in AdjacentLists[node - 1]:
        if viz[vecin - 1] == 0:
            topologicalSort(vecin)
    stack.append(node)


oriented = True
Edges = []
grad_min = []
grad_max = []
AdjacentLists = createLists(oriented)
viz = [0 for i in range(n)]
stack = []
startNode = 0
finNode = n + 1
d = [-math.inf for i in range(n+2)]
tata = [0 for i in range(n+2)]
d[startNode] = 0

for i in range(1, n+1):
    if viz[i - 1] == 0:
        topologicalSort(i)

for x in grad_min:
    AdjacentLists[startNode].append(x)
for x in grad_max:
    AdjacentLists[x].append(finNode)

stack.append(startNode)     # adaug startNode-ul
stack.reverse()
stack.append(finNode)

for node in stack:
    for adj in AdjacentLists[node]:
        if d[node] + durata[node] > d[adj]:
            d[adj] = d[node] + durata[node]
            tata[adj] = node

print("Timp minim:", d[-1])
ActCrit = []    # activitati critice
while tata[finNode] != 0:
    finNode = tata[finNode]
    ActCrit.append(finNode)
ActCrit.reverse()
print("Activitati critice:", ActCrit)
for i in range(1, n + 1):
    print(i, ":", d[i], d[i] + durata[i])
