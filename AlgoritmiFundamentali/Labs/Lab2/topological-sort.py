def createList(oriented: bool = False):
    f = open("graf.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]

    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    for i in range(len(adjacentList)):
        adjacentList[i].sort()

    return adjacentList


def printList(adjacentList: list):
    for i in range(len(adjacentList)):
        resultList = list(map(lambda x: x + 1, adjacentList[i]))
        print(str(i + 1) + ": " + str(resultList))

def topologicalSort(root):
    global stack, visited
    # insert node in stack only when all it's neighbours are in stack
    visited[root] = 1
    for neighbour in adjacentList[root]:
        if visited[neighbour] == 0:
            topologicalSort(neighbour)
    stack.append(root)

if __name__ == "__main__":
    oriented = True
    adjacentList = createList(oriented)
    # printList(adjacentList)
    n = len(adjacentList)
    visited = [0 for _ in range(n)]
    stack = []

    for node in range(n):
        if visited[node] == 0:
            topologicalSort(node)

    stack.reverse()
    print([x + 1 for x in stack])