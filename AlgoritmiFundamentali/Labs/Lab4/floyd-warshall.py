import math
from heapq import heappush, heapify, heappop

def createMatrix(oriented=False):
    f = open("grafpond.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    matrix = [[0 for i in range(nodes)] for _ in range(nodes)]
    for i in range(edges):
        node1, node2, weight = [int(x) for x in f.readline().split()]
        matrix[node1 - 1][node2 - 1] = weight
        if not oriented:
            matrix[node2 - 1][node1 - 1] = weight

    f.close()
    return matrix


def getListAndEdges(oriented: bool = False):
    f = open("grafpond.in", "r")
    nrOfNodes, nrOfEdges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nrOfNodes)]
    edges = []

    for i in range(nrOfEdges):
        node1, node2, weight = [int(x) for x in f.readline().split()]
        edges.append((node1 - 1, node2 - 1, weight))
        adjacentList[node1 - 1].append([node2 - 1, weight])

        if not oriented:
            adjacentList[node2 - 1].append([node1 - 1, weight])

    f.close()
    return adjacentList, edges


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = [(node + 1, weight) for (node, weight) in adjacentList[i]]
        print(str(i + 1) + ": " + str(resultList))


def createMatrices(edges):
    global adjacentList, oriented

    n = len(adjacentList)
    distances = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    previous = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]

    for edge in edges:
        node1, node2, weight = edge[0], edge[1], edge[2]
        distances[node1][node2] = weight
        previous[node1][node2] = node1

        if not oriented:
            distances[node2][node1] = weight
            previous[node2][node1] = node2

    return distances, previous


def getPath(node1, node2):
    global previous, path
    if node1 != node2:
        getPath(node1, previous[node1][node2])
    if node2 != None:
        path.append(node2)

    return path

if __name__ == "__main__":
    oriented = True
    adjacentList, edges = getListAndEdges(oriented)
    weight = createMatrix(oriented)
    n = len(adjacentList)
    distances, previous = createMatrices(edges)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    previous[i][j] = previous[k][j]

    nodesInCycles = []
    for i in range(n):
        for j in range(n):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                previous[i][j] = previous[k][j]

            if i == j and distances[i][j] < 0:
                nodesInCycles.append(i)
    k = 0
    for line in distances:
        k += 1
        print(k, line)

    path = []
    while nodesInCycles:
        path.clear()
        node1 = nodesInCycles[0]
        index = -1

        while weight[nodesInCycles[index]][node1] == 0:
            index -= 1

        path = getPath(node1, nodesInCycles[index])
        print("Negative cycle:", path)

        for node in path:
            nodesInCycles.remove(node)
