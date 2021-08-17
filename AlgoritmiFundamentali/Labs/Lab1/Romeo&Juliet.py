
def readData(f):
    n, m = [int(x) for x in f.readline().split()]
    matrix = []

    for i in range(n):
        line = f.readline().split('\n')
        if i == 0 and len(line[0]) != m:  # semihardcodat
            line[0] += (' ')
        matrix.append(line[0])

    Romeo, Julieta = None, None
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'R':
                Romeo = (i, j)
            if matrix[i][j] == 'J':
                Julieta = (i, j)

    return n, m, matrix, Romeo, Julieta

def bfSearch(startPoint, matrix):
    queue = [startPoint]
    visited = set()
    visited.add(startPoint)
    parent = dict()
    parent[startPoint] = (-1, -1)
    Julieta = None

    while queue:
        currentPoint = queue[0]
        neighbours = getNeighbours(currentPoint, matrix)

        for neighbour in neighbours:
            i, j = neighbour[0], neighbour[1]
            if matrix[i][j] != "X":
                if neighbour not in visited:
                    if matrix[i][j] == "J":
                        Julieta = (i, j)
                        parent.setdefault(neighbour, currentPoint)
                        break
                    visited.add(neighbour)
                    queue.append(neighbour)
                    parent.setdefault(neighbour, currentPoint)

        if Julieta:
            path = []
            node = Julieta

            while node != (-1, -1):
                path.append(node)
                node = parent[node]

            return  [len(path) // 2 + 1, tuple(map(lambda x : x + 1, path[len(path) // 2]))]
        queue.pop(0)


def getNeighbours(point, matrix):
    n = len(matrix)
    m = len(matrix[0])
    neighbours = []
    okUp, okDown, okRight, okLeft = False, False, False, False

    if point[1] - 1 >= 0:  # left side
        neighbour = (point[0], point[1] - 1)
        neighbours.append(neighbour)
        okLeft = True

    if point[1] + 1 < m:  # right side
        neighbour = (point[0], point[1] + 1)
        neighbours.append(neighbour)
        okRight = True

    if point[0] - 1 >= 0:   # up side
        neighbour = (point[0] - 1, point[1])
        neighbours.append(neighbour)
        okUp = True

    if point[0] + 1 < n:    # down side
        neighbour = (point[0] + 1, point[1])
        neighbours.append(neighbour)
        okDown = True

    if okUp and okLeft:
        neighbour = (point[0] - 1, point[1] - 1)
        neighbours.append(neighbour)

    if okUp and okRight:
        neighbour = (point[0] - 1, point[1] + 1)
        neighbours.append(neighbour)

    if okDown and okLeft:
        neighbour = (point[0] + 1, point[1] - 1)
        neighbours.append(neighbour)

    if okDown and okRight:
        neighbour = (point[0] + 1, point[1] + 1)
        neighbours.append(neighbour)

    return neighbours


if __name__ == "__main__":

    f = open("graf3.in", "r")
    n, m, matrix, Romeo, Julieta = readData(f)
    for line in matrix:
        print(line)
    print(bfSearch(Romeo, matrix))


