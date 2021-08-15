import math
from heapq import heappush, heapify, heappop

def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
    global n, m, Edges, startNode, destinatie
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
    startNode = int(f.readline())
    destinatie = [int(x) for x in f.readline().split()]
    destinatie.pop(0)
    return AdjacentList

# Folosesc algoritmul Bellman-Ford

Edges = []
destinatie = []
oriented = True
AdjacentLists = createLists(oriented)
viz = [0 for i in range(n)]
d = [math.inf for i in range(n)]
tata = [0 for i in range(n)]
d[startNode - 1] = 0

for i in range(1, n):
    for edge in Edges:
        if d[edge[0] - 1] + edge[2] < d[edge[1] - 1]:
            d[edge[1] - 1] = d[edge[0] - 1] + edge[2]
            tata[edge[1] - 1] = edge[0]

Max_dist = -math.inf
vf_departat = -1
for i in range(len(d)):
    if i+1 in destinatie:   # nodurile sunt de la 0 in indecsi si de asta scriu i+1, pt ca in destinatie le am retinute de la 1
        if d[i] > Max_dist:
            Max_dist = d[i]
            vf_departat = i + 1
print("Cel mai departat varf destinatie de nodul sursa este: ", vf_departat)
node = vf_departat - 1
drum = []
while tata[node] != 0:
    drum.append(node + 1)
    node = tata[node] - 1
drum.append(node + 1)
drum.reverse()
print(drum)
