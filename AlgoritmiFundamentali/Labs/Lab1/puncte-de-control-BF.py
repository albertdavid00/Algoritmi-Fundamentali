def createList(f, oriented=False):
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]

    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    return adjacentList


def getControlPoints(f):
    return [int(x) - 1 for x in f.readline().split()]


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))

# BFSearch
def getParentsAndBFTree(startNode, adjacentList):
    n = len(adjacentList)
    if startNode in controlPoints:
        return [startNode], [-1 for _ in range(n)]
    # startNode -= 1  # notation != actual value in list ( ex. if node = 1 then in list it's actually 0)
    queue = [startNode]
    BFTree = [startNode]
    visited = [1 if startNode == node else 0 for node in range(n)]
    parent = [-1 for _ in range(n)]
    while queue:
        currentNode = queue[0]
        for neighbour in adjacentList[currentNode]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = 1
                parent[neighbour] = currentNode
                BFTree.append(neighbour)
                if neighbour in controlPoints:
                    return BFTree, parent
        queue.pop(0)

    print("Impossible to reach control point!")
    exit(1)

def getPath(node, controlPoint, parent):

    path = []
    currentNode = controlPoint

    while currentNode != -1:
        path.append(currentNode)
        currentNode = parent[currentNode]

    return path[::-1]


if __name__ == "__main__":
    # node = int(input("Nod = "))
    node = 2
    node -= 1
    oriented = True

    f = open("graf.in", "r")
    adjacentList = createList(f, oriented)
    controlPoints = getControlPoints(f)

    printList(adjacentList)
    print("Control Points:", list(map(lambda x : x + 1, controlPoints)))
    bfTree, parent = getParentsAndBFTree(node, adjacentList)
    path = getPath(node, bfTree[-1], parent)
    print("Closest control point: {}".format(bfTree[-1] + 1))
    print("Path: ", list(map(lambda x : x + 1, path)))
    print("BF Tree:", list(map(lambda x : x + 1, (bfTree))))