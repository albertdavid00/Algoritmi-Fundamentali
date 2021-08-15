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


def drum(i, j):
    if i != j:
        drum(i, p[i][j])
    print(j + 1, end=" ")


oriented = True
myMatrix = createMatrix(oriented)
p = [[0] * n for i in range(n)]     # matrice de predecesori
for i in range(n):
    for j in range(n):
        if myMatrix[i][j] == math.inf:
            p[i][j] = 0
        else:
            p[i][j] = i
for k in range(n):
    for i in range(n):
        for j in range(n):
            if myMatrix[i][j] > myMatrix[i][k] + myMatrix[k][j]:
                myMatrix[i][j] = myMatrix[i][k] + myMatrix[k][j]
                p[i][j] = p[k][j]

for line in myMatrix:
    print(line)

drum(0,4)