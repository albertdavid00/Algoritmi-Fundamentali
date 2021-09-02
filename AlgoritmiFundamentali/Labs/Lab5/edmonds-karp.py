def getData(oriented=False):
    f = open("retea.in", "r")
    n = int(f.readline())
    s, t = [int(x) - 1 for x in f.readline().split()]
    m = int(f.readline())

    matrix = [[[0, 0] for i in range(n)] for _ in range(n)]

    for i in range(m):
        node1, node2, capacity, flow = [int(x) for x in f.readline().split()]
        matrix[node1 - 1][node2 - 1] = [capacity, flow]

        if not oriented:
            matrix[node2 - 1][node1 - 1][1] = [capacity, flow]

    f.close()
    return matrix, s, t, n, m


def getListAndEdges(oriented: bool = False):
    f = open("retea.in", "r")
    n = int(f.readline())
    s, t = [int(x) - 1 for x in f.readline().split()]
    m = int(f.readline())
    adjacentList = [[] for _ in range(n)]
    edges = []

    for i in range(m):
        node1, node2, capacity, flux = [int(x) for x in f.readline().split()]
        edges.append([node1 - 1, node2 - 1, capacity, flux])
        adjacentList[node1 - 1].append([node2 - 1, capacity, flux])
        if not oriented:
            adjacentList[node2 - 1].append([node1 - 1, capacity, flux])

    f.close()
    return adjacentList, edges


def bfs():
    global matrix, n, visited, parent, s, t, edges

    queue = [s]
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = 1

    while queue:
        node = queue.pop(0)
        for adjacent in adjacentList[node]:  # forward edge
            neighbour = adjacent[0]
            capacity, flux = matrix[node][neighbour][0], matrix[node][neighbour][1]

            if not visited[neighbour] and capacity - flux > 0:
                queue.append(neighbour)
                visited[neighbour] = True
                parent[neighbour] = node

                if neighbour == t:
                    return True

        for neighbour in range(n):
            if matrix[neighbour][node] != [0, 0]:
                if visited[neighbour] == 0 and matrix[neighbour][node][1] > 0:
                    queue.append(neighbour)
                    visited[neighbour] = 1
                    parent[neighbour] = -node
                    if neighbour == t:
                        return True

    return False


def getPath(node):
    global parent
    path = [node]

    while parent[node] != None:
        node = abs(parent[node])
        path.append(node)

    path.reverse()
    return path


def validFlow(matrix):
    global n

    for i in range(n):
        flowIn = sum(list(map(lambda x: x[1], matrix[i])))
        flowOut = 0
        for row in range(n):
            flowOut += matrix[row][i][1]

        if i != s and i != t:
            if flowIn != flowOut:
                return False

        for j in range(n):
            capacity, flow = [x for x in matrix[i][j]]
            if capacity < flow:
                return False

    return True


if __name__ == "__main__":
    oriented = True
    matrix, s, t, n, m = getData(oriented)
    adjacentList, edges = getListAndEdges(oriented)

    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]

    if validFlow(matrix):
        print("Valid flow")
    else:
        print("Invalid flow")

    while bfs():    # find unsaturated path
        # review / update flow
        path = getPath(t)
        capacities = []

        for i in range(len(path) - 1):  # calculate the residual capacities in the path
            node1, node2 = path[i], path[i + 1]

            if parent[node2] >= 0:
                capacity, flow = matrix[node1][node2][0], matrix[node1][node2][1]
                residualCapacity = capacity - flow
                capacities.append(residualCapacity)
            else:
                flow = matrix[node2][node1][1]
                capacities.append(flow)

        minCapacity = min(capacities)

        for i in range(len(path) - 1):  # update the flow in the matrix
            node1, node2 = path[i], path[i + 1]
            capacity, flow = matrix[node1][node2][0], matrix[node1][node2][1]

            if parent[node2] >= 0:
                matrix[node1][node2][1] += minCapacity
            else:
                matrix[node2][node1][1] -= minCapacity
    flow = 0
    for i in range(n):
        if matrix[s][i] != [0, 0]:
            flow += matrix[s][i][1]
    print("Max flow:", flow)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != [0, 0]:
                print(i + 1, j + 1, matrix[i][j][1])
