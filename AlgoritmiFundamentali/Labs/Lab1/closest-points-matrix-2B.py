def readData(f):
    n, m = [int(x) for x in f.readline().split()]
    matrix = [[int(x) for x in f.readline().split()] for _ in range(n)]
    points = []
    for line in f.readlines():
        points.append(tuple([int(x) - 1 for x in line.split()]))

    # printMatrix(matrix)
    # print(points)
    return n, m, matrix, points


def printMatrix(matrix):
    for line in matrix:
        print(line)


def bfSearch(startPoint, matrix):
    queue = [startPoint]
    visitedPoints = set()
    visitedPoints.add(startPoint)
    closestPoint = None

    while queue:
        currentPoint = queue[0]
        neighbours = getNeighbours(currentPoint, matrix)

        for neighbour in neighbours:
            if neighbour not in visitedPoints:
                visitedPoints.add(neighbour)
                i, j = neighbour[0], neighbour[1]
                if matrix[i][j] == 1:
                    closestPoint = (i, j)
                    break
                queue.append(neighbour)

        if closestPoint:
            dist = abs(startPoint[0] - closestPoint[0]) + abs(startPoint[1] - closestPoint[1])
            return dist, closestPoint

        queue.pop(0)
    return -1, -1


def getNeighbours(point, matrix):
    n = len(matrix)
    m = len(matrix[0])
    neighbours = []

    if point[1] - 1 >= 0:  # left side
        neighbour = (point[0], point[1] - 1)
        neighbours.append(neighbour)

    if point[1] + 1 < m:  # right side
        neighbour = (point[0], point[1] + 1)
        neighbours.append(neighbour)

    if point[0] - 1 >= 0:   # up side
        neighbour = (point[0] - 1, point[1])
        neighbours.append(neighbour)

    if point[0] + 1 < n:    # down side
        neighbour = (point[0] + 1, point[1])
        neighbours.append(neighbour)

    return neighbours


if __name__ == "__main__":
    f = open("graf2.in", "r")
    n, m, matrix, points = readData(f)
    for point in points:
        distance, closestPoint = bfSearch(point, matrix)
        print(distance, tuple(map(lambda x: x + 1, closestPoint)))
