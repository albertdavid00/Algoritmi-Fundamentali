def createList(oriented: bool = False):
    f = open("graf.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]
    inDegree = [0 for _ in range(nodes)]
    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        inDegree[node2 - 1] += 1
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    for i in range(len(adjacentList)):
        adjacentList[i].sort()

    return adjacentList, inDegree


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))


def topologicalSort():
    global inDegree, adjacentList
    queue = []
    sortedNodes = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.pop(0)
        sortedNodes.append(node)
        for neighbour in adjacentList[node]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                queue.append(neighbour)

    for degree in inDegree:
        if degree != 0:
            return []

    return sortedNodes


if __name__ == "__main__":
    oriented = True
    adjacentList, inDegree = createList(oriented)
    # printList(adjacentList)
    sortedNodes = topologicalSort()
    if sortedNodes == []:
        print("No topological sort. There are circuits in graph.")
    else:
        print([x + 1 for x in sortedNodes])
