def createList(oriented: bool = False):
    f = open("graf.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]

    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    return adjacentList


def bfSearch(startNode, adjacentList = []):
    if not adjacentList:
        return []
    # startNode -= 1  # notation != actual value in list ( ex. if node = 1 then in list it's actually 0) !!!
    n = len(adjacentList)
    queue = [startNode]
    BFTree = [startNode]
    level = [0 for _ in range(n)]
    visited = [1 if startNode == node else 0 for node in range(n)]
    parent = [[-1] if startNode == node else [] for node in range (n)]    # fiecare nod are o lista de posibili tati

    while queue:
        currentNode = queue[0]
        for neighbour in adjacentList[currentNode]:
            if not visited[neighbour]:

                visited[neighbour] = 1
                level[neighbour] = level[currentNode] + 1
                parent[neighbour].append(currentNode)

                queue.append(neighbour)
                BFTree.append(neighbour)

            elif level[currentNode] < level[neighbour]: # there's one more way to reach the neighbour
                parent[neighbour].append(currentNode)
        queue.pop(0)

    return BFTree, parent   # return parent for more info


def searchPath(node):
    global parents, finalNode, minPaths, k, allMinPaths

    for parent in parents[node]:
        if parent == -1:
            print(finalNode, *minPaths[k])
            allMinPaths.append([x for x in minPaths[k]])
            return

        else:
            minPaths[k].append(parent)
            searchPath(parent)
            minPaths[k].pop()


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))

if __name__ == "__main__":
    oriented = False
    adjacentList = createList(oriented)
    # indexare de la 0 a nodurilor
    startNode = 9
    finalNode = 4

    bfTree, parents = bfSearch(startNode, adjacentList)
    # print(parents[1])
    # printList(adjacentList)
    minPaths = [[]]
    k = 0

    # extension for problem 4B
    allMinPaths = []
    optimNodes = set()
    optimNodes.add(startNode)
    optimNodes.add(finalNode)
    # ------ end ----------

    for parent in parents[finalNode]:
        minPaths[k].append(parent)
        searchPath(parent)
        k += 1
        minPaths.append([])

    # ---------- extension --------------
    # print(allMinPaths)
    for node in range(len(adjacentList)):
        ok = True
        for path in allMinPaths:
            if node not in path:
                ok = False
        if ok:
            optimNodes.add(node)
    print(len(optimNodes))
    print(optimNodes)