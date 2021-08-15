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


def Reprez(node):
    global tata
    while tata[node - 1] != 0:
        node = tata[node - 1]
    return node


def Unite(u, v):
    global tata, height
    ru = Reprez(u)
    rv = Reprez(v)
    if height[ru - 1] > height[rv - 1]:
        tata[rv - 1] = ru
    else:
        tata[ru - 1] = rv
        if height[ru - 1] == height[rv - 1]:
            height[rv - 1] = height[rv - 1] + 1

def DFS(startNode):
    global adj, n, viz, parent, niv, ciclu
    stack = [startNode]
    DFTree = [startNode]
    viz[startNode - 1] = 1
    niv[startNode - 1] = 1
    while stack:
        ok = 0
        for vecin in adj[stack[-1] - 1]:
            if viz[vecin[0] - 1] == 0:
                parent[vecin[0] - 1] = stack[-1]
                niv[vecin[0] - 1] = niv[stack[-1] - 1] + 1
                stack.append(vecin[0])
                DFTree.append(vecin[0])
                viz[vecin[0] - 1] = 1
                ok = 1
                break
            elif niv[stack[-1] -1] > niv[vecin[0] - 1] + 1: # muchie de intoarcere
                ciclu.append(stack[-1])
                node = stack[-1] - 1
                while parent[node] != vecin[0]:
                    node = parent[node] - 1
                    ciclu.append(node + 1)
                ciclu.append(vecin[0])
        if not ok:
            stack.pop()
    return DFTree

Edges = []
oriented = False
AdjacentLists = createLists(oriented)
Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
tata = [0 for i in range(n)]  # initializez lista de tati
height = [0 for i in range(n)]  # inaltimile
nrmsel = 0
TreeEdges = []
for edge in Edges:
    if Reprez(edge[0]) != Reprez(edge[1]):
        TreeEdges.append(edge)
        Unite(edge[0], edge[1])
        nrmsel += 1
        if nrmsel == n - 1:
            break

total = sum(map(lambda x: int(x[2]), TreeEdges))
print(total)
for edge in TreeEdges:
    print(edge)

# subp. a) si b)
newEdge = (3, 5, 4)
TreeEdges.append(newEdge)
adj = [[] for i in range(n)]
parent = [0 for i in range(n)]
viz = [0 for i in range(n)]
niv = [0 for i in range(n)]
ciclu = []
for edge in TreeEdges:
    node1 = edge[0] - 1
    node2 = edge[1] - 1
    adj[node1].append((edge[1], edge[2]))
    if not oriented:
        adj[node2].append((edge[0], edge[2]))

# for x in adj:
#     x.sort(key = lambda e: e[0])
df = DFS(1)
muchiiCiclu = []
for edge in TreeEdges:
    if edge[0] in ciclu and edge[1] in ciclu:
        muchiiCiclu.append((edge[0], edge[1], edge[2]))
costMax = max(map(lambda x: x[2],muchiiCiclu))
for edge in muchiiCiclu:
    if edge[2] == costMax:
        print("Muchia de cost maxim din ciclul inchis este:", edge[0], edge[1], "cu costul:", edge[2])
        print("Dupa adaugarea muchiei apcm are costul:", total - edge[2] + newEdge[2])