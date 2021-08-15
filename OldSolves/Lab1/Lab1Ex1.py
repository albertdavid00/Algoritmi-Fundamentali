def createMatrix(grafType):
    f = open("graf.in","r")
    n,m = [int(x) for x in f.readline().split()]
    lista = []
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        lista.append(tuple(aux))
    for pair in lista:
        matrix[pair[0] - 1][pair[1] - 1] = 1
        if grafType == "neorientat":
            matrix[pair[1] - 1][pair[0] - 1] = 1
    return matrix

def ToList(matrix):
    L = [[] for i in range (len(matrix))]
    k = 0
    for line in matrix:
        for i in range (len(line)):
            if line[i]:
                L[k].append(i+1)
        k += 1
    return L


grafType =input("Introduceti tipul grafului (orientat / neorientat): ")
myMatrix = createMatrix(grafType)
i = 0
for line in myMatrix:
    i += 1
    print(str(i) + ":", end= " ")
    print(*line)
myList = ToList(myMatrix)