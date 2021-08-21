import math


def getData(oriented: bool = False):
    f = open("retea2.in", "r")
    nrOfPowerStations, nrOfBuildings, nrOfEdges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nrOfPowerStations + nrOfBuildings)]
    edges = []
    coords = []

    for i in range(nrOfPowerStations + nrOfBuildings):
        x, y = [int(coord) for coord in f.readline().split()]
        coords.append((x, y))

    for i in range(nrOfEdges):
        node1, node2 = [int(x) for x in f.readline().split()]
        distance = getEuclideanDistance(node1 - 1, node2 - 1, coords)
        edges.append((node1 - 1, node2 - 1, distance))
        adjacentList[node1 - 1].append([node2 - 1, distance])

        if not oriented:
            adjacentList[node2 - 1].append([node1 - 1, distance])

    edges.sort(key=lambda e: e[2])
    return adjacentList, edges, nrOfPowerStations, nrOfBuildings


def repres(node):
    global parent
    if parent[node] == -1:
        return node

    parent[node] = repres(parent[node])
    return parent[node]


def unite(fstNode, sndNode):
    global n, parent, height
    rep1 = repres(fstNode)
    rep2 = repres(sndNode)

    height1 = height[rep1]
    height2 = height[rep2]

    if height1 > height2:
        parent[rep2] = rep1
        return

    parent[rep1] = rep2
    if height[rep1] == height[rep2]:
        height[rep2] += 1
    return


def getEuclideanDistance(node1, node2, coords):

    res1 = (coords[node1][0] - coords[node2][0]) ** 2
    res2 = (coords[node1][1] - coords[node2][1]) ** 2
    return math.sqrt(res1 + res2)


def printMST(mst):
    print("MSTree:", [(node1 + 1, node2 + 1, weight) for (node1, node2, weight) in mst])
    print("Weight:", sum(list(map(lambda x: x[2], mst))))

if __name__ == "__main__":
    oriented = False
    adjacentList, edges, n, m = getData(oriented)

    height = [0 for _ in range(len(adjacentList))]
    parent = [-1 for _ in range(len(adjacentList))]
    minimumSpanningTree = []
    countEdgesInMST = 0

    for i in range(n):
        if i != 0:
            parent[i] = 0  # all the power stations are in the same component!
        height[i] = 1

    for edge in edges:
        fstNode, sndNode = edge[0], edge[1]

        if repres(fstNode) != repres(sndNode):
            unite(fstNode, sndNode)
            minimumSpanningTree.append(edge)
            countEdgesInMST += 1

        if countEdgesInMST == m:  # MST will have m edges now
            break

    printMST(minimumSpanningTree)