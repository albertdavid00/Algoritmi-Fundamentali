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


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))


def toMatrix(adjacentList: list):
    matrix = []
    for i in range(len(adjacentList)):
        matrix.append([0] * len(adjacentList))
    for i in range(len(adjacentList)):
        for node in adjacentList[i]:
            matrix[i][node] = 1

    return matrix


def printMatrix(matrix):
    for line in matrix:
        print(line)


if __name__ == "__main__":
    oriented = True
    adjacentList = createList(oriented)
    printList(adjacentList)
    matrix = toMatrix(adjacentList)
    printMatrix(matrix)
