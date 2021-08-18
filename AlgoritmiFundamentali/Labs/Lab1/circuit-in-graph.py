def createList(oriented: bool = False):
    f = open("graf5.in", "r")
    nodes, edges = [int(x) for x in f.readline().split()]
    adjacentList = [[] for _ in range(nodes)]

    for i in range(edges):
        node1, node2 = [int(x) for x in f.readline().split()]
        adjacentList[node1 - 1].append(node2 - 1)
        if not oriented:
            adjacentList[node2 - 1].append(node1 - 1)

    return adjacentList

def dfSearch(root):
    global  n, dfTree, visited, adjacentList, check

    for neighbour in adjacentList[root]:
        if check:
            return

        if not visited[neighbour]:
            visited[neighbour] = 1
            parent[neighbour] = root
            dfTree.append(neighbour)
            dfSearch(neighbour)

        else:
            if foundInPath(root, neighbour, parent):
                check = True
                dfTree.append(neighbour)
                return

def foundInPath(root, neighbour, parent):

    node = root
    while parent[node] != -1:
        if parent[node] == neighbour:
            return True
        node = parent[node]
    return False

def getCycle(dfTree, parent):
    startNode, endNode = dfTree[-1], dfTree[-2]
    node = endNode
    cycle = []
    while node != startNode:
        cycle.append(node)
        node = parent[node]

    cycle.append(startNode)
    cycle.reverse()
    return cycle



# indexare de la 0 a nodurilor
if __name__ == "__main__":

    oriented = True
    adjacentList = createList(oriented)
    n = len(adjacentList)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dfTree = []

    check = False
    for node in range(n):
        if not visited[node]:
            visited[node] = 1
            dfTree = [node]
            dfSearch(node)
            if check:
                print("Exista circuit")
               # print(list(map(lambda x: x+ 1, dfTree)))
                print(list(map(lambda x: x+ 1, getCycle(dfTree, parent))))
                break
    if not check:
        print("Nu exista circuit => Realizabil")


