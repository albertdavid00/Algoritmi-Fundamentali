
def createMatrix(oriented=False):
    f = open("graf.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    matrix = []
    matrix = [[0 for i in range(nodes)] for _ in range(nodes)]
    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        matrix[node1 - 1][node2 - 1] = 1
        if not oriented:
            matrix[node2 - 1][node1 - 1] = 1

    return matrix


def printMatrix(matrix):
    for line in matrix:
        print(line)


def toAdjacentList(matrix):
    adjacentList = [[] for i in range(len(matrix))]
    index = 0

    for line in matrix:
        for i in range(len(line)):
            if line[i]:
                adjacentList[index].append(i)
        index += 1

    return adjacentList

def printList(adjacentList : list):

    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))


if __name__ == "__main__":
    oriented = False
    myMatrix = createMatrix(oriented)
    printMatrix(myMatrix)
    adjacentList = toAdjacentList(myMatrix)
    printList(adjacentList)

