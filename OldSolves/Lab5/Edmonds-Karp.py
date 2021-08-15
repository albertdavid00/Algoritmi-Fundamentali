import math
from collections import deque


def createMatrix(oriented=False):
    global n, m, s, t, Edges
    f = open("retea.in", "r")
    n = int(f.readline())
    s, t = [int(x) for x in f.readline().split()]
    s = s - 1
    t = t - 1
    m = int(f.readline())
    Edges = []
    matrix = []
    for i in range(n):
        matrix.append([[-1, -1]] * n)
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        Edges.append(tuple(aux))
    for edge in Edges:
        matrix[edge[0] - 1][edge[1] - 1] = [edge[3], edge[2]]  # matrice formata din perechi [flux, capacitate]
        if not oriented:
            matrix[edge[1] - 1][edge[0] - 1] = 1
    return matrix


def BFS_unsat():
    global s, t, tata, viz
    for i in range(n):
        tata[i] = viz[i] = 0
    coada = [s]
    viz[s] = 1
    while coada:
        i = coada.pop()
        for j in range(n):
            if myMatrix[i][j] != [-1, -1]:
                if viz[j] == 0 and myMatrix[i][j][1] - myMatrix[i][j][0] > 0:
                    coada.append(j)
                    viz[j] = 1
                    tata[j] = i
                    if j == t:
                        return True
        for j in range(n):
            if myMatrix[j][i] != [0, 0]:
                if viz[j] == 0 and myMatrix[j][i][0] > 0:
                    coada.append(j)
                    viz[j] = 1
                    tata[j] = -i
                    if j == t:
                        return True
    return False


oriented = True
myMatrix = createMatrix(oriented)
tata = [0 for i in range(n)]
viz = [0 for i in range(n)]
P = []
flux = 0
while BFS_unsat():
    P = []
    cap_rez = []
    node = t
    while node != s:
        P.append(node)
        node = abs(tata[node])
    P.append(s)
    P.reverse()
    for i in range(len(P) - 1):
        if tata[P[i + 1]] >= 0:
            dif = myMatrix[P[i]][P[i + 1]][1] - myMatrix[P[i]][P[i + 1]][0]
            cap_rez.append(dif)
        else:
            cap_rez.append(myMatrix[P[i + 1]][P[i]][0])
    minCap = min(cap_rez)
    for i in range(len(P) - 1):
        if tata[P[i + 1]] >= 0:
            myMatrix[P[i]][P[i + 1]][0] = myMatrix[P[i]][P[i + 1]][0] + minCap
        else:
            myMatrix[P[i + 1]][P[i]][0] = myMatrix[P[i + 1]][P[i]][0] - minCap
    P.clear()
for i in range(n):
    if myMatrix[s][i] != [-1, -1]:
        flux += myMatrix[s][i][0]
print(flux)
for i in range(n):
    for j in range(n):
        if myMatrix[i][j] != [-1, -1]:
            print(i + 1, j + 1, myMatrix[i][j][0])
