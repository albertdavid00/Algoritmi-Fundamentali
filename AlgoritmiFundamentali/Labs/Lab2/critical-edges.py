def createList(oriented: bool = False):
    f = open("graf.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]

    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    for i in range(len(adjacentList)):
        adjacentList[i].sort()

    return adjacentList


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))



def dfSearch(root):
    global dfTree, visited, adjacentList, stackEdges
    global level, min_level, startNode, biconexComponents

    visited[root] = 1
    min_level[root] = level[root]

    for neighbour in adjacentList[root]:
        if not visited[neighbour]:      # muchie ascendenta => este posibil sa fie muchie critica
            visited[neighbour] = 1
            parents[neighbour] = root
            level[neighbour] = level[root] + 1
            dfTree.append(neighbour)
            stackEdges.append((root, neighbour))

            dfSearch(neighbour)

            min_level[root] = min(min_level[root], min_level[neighbour])    # actualizare nivel_minim

            if level[root] <= min_level[neighbour]:  # daca (root,neighbour) e muchie critica
                if root != startNode:
                    vulnerablePoints.add(root)

                index = stackEdges.index((root, neighbour))
                biconexComponents.append(stackEdges[index : ])
                stackEdges = stackEdges[ : index]


                if level[root] < min_level[neighbour]:
                    criticalEdges.append((root, neighbour))

        elif level[neighbour] < level[root] - 1:    # muchie de intoarcere (excludem muchia directa tata-fiu)
            min_level[root] = min(min_level[root], level[neighbour])
            stackEdges.append((root, neighbour))


def checkRootIsCritical(root):
    global vulnerablePoints

    countSons = 0
    for parent in parents:
        if parent == root:
            countSons += 1
    if countSons > 1:
        vulnerablePoints.add(root)

if __name__ == "__main__":
    oriented = False
    adjacentList = createList(oriented)
    n= len(adjacentList)
    startNode = 0
    visited = [0 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    level = [0 for _ in range(n)]
    min_level = [0 for _ in range(n)]
    dfTree = [startNode]

    criticalEdges = []
    vulnerablePoints = set()
    subnetwork = []
    stackEdges = []
    biconexComponents = []

    dfSearch(startNode)
    checkRootIsCritical(startNode)

    if not criticalEdges:
        print("Retea 2 muchie-conexa")
    else:
        print("Legaturi critice:", [(x + 1,y + 1) for (x, y) in criticalEdges])

    if not vulnerablePoints:
        print("Retea biconexa")
    else:
        print("Puncte vulnerabile: ", list(map(lambda x : x + 1, vulnerablePoints)))

    print("Componenete biconexe maximale: ")
    maxLengthForComponent = (max(map(lambda x: len(x), biconexComponents)))
    for component in biconexComponents:
        nodes = set()
        if len(component) == maxLengthForComponent:
            for edge in component:
                nodes.add(edge[0])
                nodes.add(edge[1])
            print(list(map(lambda node : node + 1, nodes)))
            print([(x + 1, y + 1) for (x, y) in component])
