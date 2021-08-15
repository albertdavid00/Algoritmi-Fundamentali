import math
# Complexitate: O(N+M)
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


def topologicalSort(node):
    global stack, viz
    viz[node - 1] = 1
    for vecin in AdjacentLists[node - 1]:
        if viz[vecin - 1] == 0:
            topologicalSort(vecin)
    stack.append(node)

oriented = True
AdjacentLists = createLists(oriented)

viz = [0 for i in range(n)]
stack = []

for i in range(1, n+1):
    if viz[i - 1] == 0:
        topologicalSort(i)

stack.reverse()
print(*stack)
