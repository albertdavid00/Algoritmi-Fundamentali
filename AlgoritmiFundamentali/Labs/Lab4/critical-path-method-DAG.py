import math
from collections import deque


def createList(oriented: bool = False):
    f = open("activitati.in", "r")
    numOfNodes = int(f.readline())
    time = [int(x) for x in f.readline().split()]
    numOfEdges = int(f.readline())
    adjacentList = [[] for _ in range(numOfNodes)]
    inDegree = [0 for _ in range(numOfNodes)]
    for i in range(numOfEdges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        inDegree[node2 - 1] += 1
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    for i in range(len(adjacentList)):
        adjacentList[i].sort()

    return adjacentList, inDegree, time


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))


def topologicalSort():
    global inDegree, adjacentList
    queue = []
    sortedNodes = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.pop(0)
        sortedNodes.append(node)
        for neighbour in adjacentList[node]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                queue.append(neighbour)

    for degree in inDegree:
        if degree != 0:
            return []

    return sortedNodes

def getPath(root):
    global parent
    path = [root]
    while parent[root] != -1:
        root = parent[root]
        path.append(root)

    path.pop() # remove the startNode which is not in the graph
    return path

if __name__ == "__main__":
    oriented = True
    adjacentList, inDegree, time = createList(oriented)
    n = len(adjacentList)

    startNode = n
    adjacentList.append([])
    time.append(0)

    parent = [-1 for _ in range(n + 1)]
    distance = [-math.inf for _ in range(n + 2)]    # since we need the max distance, we reverse the limit
    distance[startNode] = 0

    for i in range(len(inDegree)):
        if inDegree[i] == 0:
                adjacentList[n].append(i)

    sortedNodes = deque(topologicalSort())
    sortedNodes.appendleft(startNode)

    for node in sortedNodes:
        if adjacentList[node]:  # if node is not a final node (out-degree = 0)
            for neighbour in adjacentList[node]:
                weight = time[node]
                if distance[node] + weight > distance[neighbour]:   # for min dist, reverse the condition (leq)
                    distance[neighbour] = distance[node] + weight
                    parent[neighbour] = node
        else:   # this will happen only with the nodes at the end of the list with out-degree = 0
            distance[node] += time[node]

    maxDistance = max(distance)
    finalNode = distance.index(maxDistance)
    criticalPath = getPath(finalNode)
    criticalPath.reverse()
    print("Minimum time:", maxDistance)
    print("Critical activities:", list(map(lambda x: x+1, criticalPath)))
    for i in range(n):
        if adjacentList[i]:
            print(i+1, ":", distance[i], distance[i] + time[i])
        else:   # the distance for final nodes already includes their time too
            print(i + 1, ":", distance[i] - time[i], distance[i])


