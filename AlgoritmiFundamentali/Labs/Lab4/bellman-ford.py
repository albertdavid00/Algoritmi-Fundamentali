import math


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

    # for i in range(len(adjacentList)):
    #     adjacentList[i].sort()

    return adjacentList, edges

if __name__ == "__main__":
    oriented = True
    adjacentList, edges = getListAndEdges(oriented)
    n = len(adjacentList)
    startNode = 0
    visited = [0 for _ in range(n)]
    distance = [math.inf for _ in range(n)]
    parent = [0 for _ in range(n)]
    distance[startNode] = 0

    for node in range(n):
        for edge in edges:
            node1, node2, weight = edge[0], edge[1], edge[2]
            if distance[node1] + weight < distance[node2]:
                distance[node2] = distance[node1] + weight
                parent[node2] = node1

    # detectare circuit negativ
    for edge in edges:
        node1, node2, weight = edge[0], edge[1], edge[2]
        if distance[node1] + weight < distance[node2]:
            distance[node2] = distance[node1] + weight
            parent[node2] = node1
            print("Stop")
            break