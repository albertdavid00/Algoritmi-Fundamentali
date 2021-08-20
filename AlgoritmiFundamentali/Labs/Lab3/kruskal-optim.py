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


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = [(node + 1, weight) for (node, weight) in adjacentList[i]]
        print(str(i + 1) + ": " + str(resultList))


def reprez(node):
    global parent

    while parent[node] != -1:
        node = parent[node]

    return node



'''
the height grows only if the trees are of the same height
as a result of always attaching the smaller tree to the taller tree
'''
def unite(fstNode, sndNode):
    global n, parent
    rep1 = reprez(fstNode)
    rep2 = reprez(sndNode)

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
    print("Cost:", sum(list(map(lambda x: x[2], mst))))


# Complexity: O(m log n)
if __name__ == "__main__":
    oriented = False
    adjacentList, edges = getListAndEdges(oriented)
    n = len(adjacentList)

    parent = [-1 for _ in range(n)]
    height = [0 for _ in range(n)]

    minimumSpanningTree = []
    countEgdesInMST = 0

    edges.sort(key=lambda e: e[2])

    for edge in edges:
        fstNode, sndNode = edge[0], edge[1]

        if reprez(fstNode) != reprez(sndNode):
            unite(fstNode, sndNode)
            minimumSpanningTree.append(edge)
            countEgdesInMST += 1

        if countEgdesInMST == n - 1:  # MST has n-1 edges
            break

    printMST(minimumSpanningTree)
