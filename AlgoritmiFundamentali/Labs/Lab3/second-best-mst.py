import copy
import math


def getListAndEdges(oriented: bool = False):
    f = open("sndbest.in", "r")
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


def printMST(mst):
    print("MSTree:", [(node1 + 1, node2 + 1, weight) for (node1, node2, weight) in mst])
    print("Weight:", sum(list(map(lambda x: x[2], mst))))


def dfSearch(root):
    global n, visited, adjTree, dfPath, check, parentTree
    if check == True:
        return
    visited[root] = 1
    for neighbour, weight in adjTree[root]:
        if not visited[neighbour]:
            parentTree[neighbour] = root
            dfPath.append((root, neighbour, weight))
            dfSearch(neighbour)

            if check:
                return
            dfPath.pop()

        elif parentTree[root] != neighbour:   # we got the cycle
            dfPath.append((root, neighbour, weight))
            check = True
            return

def getMaxEdge(dfPath, newEdge):

    maxEdge = [-1, -1, -1]
    for edge in dfPath:
        edges = (edge[0], edge[1])
        if edge[2] > maxEdge[2]:
            if newEdge[0] in edges and newEdge[1] in edges:
                continue
            maxEdge = edge

    return maxEdge

if __name__ == "__main__":
    oriented = False
    adjacentList, edges = getListAndEdges(oriented)
    n = len(adjacentList)

    parent = [-1 for _ in range(n)]
    height = [0 for _ in range(n)]

    minimumSpanningTree = []
    countEdgesInMST = 0

    edges.sort(key=lambda e: e[2])
    remainingEdges = copy.deepcopy(edges)
    for edge in edges:
        fstNode, sndNode = edge[0], edge[1]

        if repres(fstNode) != repres(sndNode):
            unite(fstNode, sndNode)
            minimumSpanningTree.append(edge)
            countEdgesInMST += 1
            remainingEdges.remove(edge)

        if countEdgesInMST == n - 1:  # MST has n-1 edges
            break
    print("Best Tree")
    printMST(minimumSpanningTree)

    adjTree = [[] for _ in range(n)]
    for edge in minimumSpanningTree:
        node1, node2, weight = edge[0], edge[1], edge[2]
        adjTree[node1].append((node2, weight))

        if not oriented:
            adjTree[node2].append((node1, weight))



    lastEdgeIndex = edges.index(minimumSpanningTree[-1])
    sndBestList = [None, None, math.inf] # newEdge, edgeToBeRemovedFromMST, weightDifference

    for i in range(len(remainingEdges)):
        parentTree = [-1 for _ in range(n)]
        visited = [0 for _ in range(n)]
        dfPath = []
        check = False
        newEdge = remainingEdges[i]
        node1, node2, weight = newEdge[0], newEdge[1], newEdge[2]
        minimumSpanningTree.append(newEdge)
        adjTree[node1].append([node2, weight])
        if not oriented:
            adjTree[node2].append([node1, weight])

        dfSearch(node1)
        maxEdge = getMaxEdge(dfPath, newEdge)
        weightDifference = newEdge[2] - maxEdge[2]
        minWeightDifference = sndBestList[2]

        if weightDifference < minWeightDifference:
            sndBestList[2] = weightDifference
            sndBestList[0] = newEdge
            sndBestList[1] = maxEdge

        minimumSpanningTree.pop()
        adjTree[node1].pop()
        if not oriented:
            adjTree[node2].pop()

    secondBest = copy.deepcopy(minimumSpanningTree)

    secondBest.append(sndBestList[0])
    secondBest.remove(sndBestList[1])
    print("Second Best Tree:")
    printMST(secondBest)
