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

if __name__ == "__main__":
    oriented = False
    adjacentList, edges = getListAndEdges(oriented)
    n = len(adjacentList)

    parent = [-1 for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    visited = [0 for _ in range(n)]

    startNode = 0
    distance[startNode] = 0
    minimumSpanningTree = []

    heap = []
    heapify(heap)

    for node in range(n):
        heappush(heap, (distance[node], parent[node], node))

    while heap:
        minElement = heappop(heap)
        dist, par, node = minElement[0], minElement[1], minElement[2]

        if visited[node] == 0:
            visited[node] = 1

            if node != startNode:
                minimumSpanningTree.append((par, node, dist))

            for neighbour, weight in adjacentList[node]:
                if visited[neighbour] == 0 and weight < distance[neighbour]:
                    distance[neighbour] = weight
                    parent[neighbour] = node
                    heappush(heap, (weight, node, neighbour))

        if len(minimumSpanningTree) == n - 1:
            # remove useless iterations
            break

    print("MST Format: (node1, node2, weight)")
    printMST(minimumSpanningTree)