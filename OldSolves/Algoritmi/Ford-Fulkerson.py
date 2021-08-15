import math


def createMatrix(oriented=False):
    global n, m
    f = open("grafpond.in", "r")
    n, m = [int(x) for x in f.readline().split()]
    lista = []
    matrix = []
    for i in range(n):
        matrix.append([0 if j == i else math.inf for j in range(n)])
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        lista.append(tuple(aux))
    for edge in lista:
        matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        if not oriented:
            matrix[edge[1] - 1][edge[0] - 1] = 1
    return matrix


oriented = True
myMatrix = createMatrix(oriented)