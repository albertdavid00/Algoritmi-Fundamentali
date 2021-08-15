def createLists(oriented=False):  # functie pentru crearea listei de adiacenta
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
    # controlPoints = [int(x) for x in f.readline().split()]  # n am nevoie de astea
    return AdjacentList


def DFS(startNode):
    global AdjacentLists, n, tata, viz, circuit
    stack = [startNode]
    DFTree = [startNode]
   # viz = [0 for i in range(n)]
    tata = [-1 for i in range(n)]
    tata[startNode - 1] = 0
    viz[startNode - 1] = 1
    while stack:
        ok = 0
        for vecin in AdjacentLists[stack[-1] - 1]:
            if viz[vecin - 1] == 0:
                DFTree.append(vecin)
                viz[vecin - 1] = 1
                tata[vecin - 1] = stack[-1]
                stack.append(vecin)
                ok = 1
                break
            else:
                x = stack[-1] - 1
                circuit = []
                while x >= 0:
                    circuit.append(x + 1)
                    if tata[x] == vecin:
                        circuit.append(vecin)
                        circuit.reverse()
                        return True
                    x = tata[x] - 1
        if not ok:
            stack.pop()
    return DFTree

oriented = True
AdjacentLists = createLists(oriented)
viz = [0 for i in range(n)]
for node in range(1, n + 1):
    if viz[node - 1] == 0:
        check = DFS(node)
        if check == True:
            break
if check == True:
    print(circuit)
else:
    print("Rezolvabil")