import math
from heapq import heappush, heapify, heappop


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

    return adjacentList, edges


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = [(node + 1, weight) for (node, weight) in adjacentList[i]]
        print(str(i + 1) + ": " + str(resultList))


def printMST(mst):
    print("MSTree:", [(node1 + 1, node2 + 1, weight) for (node1, node2, weight) in mst])
    print("Weight:", sum(list(map(lambda x: x[2], mst))))


def getPath(parent, root):
    path = [root]

    while parent[root] != -1:
        root = parent[root]
        path.append(root)
    return path


if __name__ == "__main__":
    oriented = False
    adjacentList, edges = getListAndEdges(oriented)
    n = len(adjacentList)

    k = 2
    controlPoints = [8, 9]
    startNode = 0

    controlPoints = [x - 1 for x in controlPoints]

    parent = [-1 for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    visited = [0 for _ in range(n)]

    distance[startNode] = 0

    heap = []
    heapify(heap)

    for node in range(n):
        heappush(heap, (distance[node], parent[node], node))

    while heap:
        minElement = heappop(heap)
        dist, par, node = minElement[0], minElement[1], minElement[2]

        for neighbour, weight in adjacentList[node]:
            if distance[node] + weight < distance[neighbour]:
                distance[neighbour] = weight + distance[node]
                parent[neighbour] = node
                heappush(heap, (distance[neighbour], node, neighbour))

    minWeight = min(list(map(lambda x: distance[x], controlPoints)))
    for point in controlPoints:
        if distance[point] == minWeight:
            path = getPath(parent, point)
            path.reverse()
            print([x + 1 for x in path])
            print(minWeight)

    # dijkstraTree = []
    # for i in range(n):
    #     if parent[i] != -1:
    #         dijkstraTree.append((i, parent[i]))
    # dijkstraTree.sort(key=lambda e: e[1])
    # print([(x + 1, y + 1) for x,y in dijkstraTree])
