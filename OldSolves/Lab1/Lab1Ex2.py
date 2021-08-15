# def createLists(graphType):
#     f = open("graf.in","r")
#     n,m = [int(x) for x in f.readline().split()]
#     lista = []
#     AdjacentList = []
#     for i in range(m):
#         aux = [int(x) for x in f.readline().split()]
#         lista.append(tuple(aux))
#         if graphType == "neorientat":
#             aux.reverse()
#             lista.append(tuple(aux))
#     lista.sort(key = lambda e: e[0])
#     nr = 1
#     aux = []
#     for pair in lista:
#         if pair[0] == nr:
#             aux.append(pair[1])
#         else:
#             AdjacentList.append([*aux])
#             aux.clear()
#             aux.append(pair[1])
#             nr = pair[0]
#     if aux:
#         AdjacentList.append([*aux])
#     return AdjacentList
def createLists(graphType):
    global n, m
    f = open("graf.in", "r")
    n, m = [int(x) for x in f.readline().split()]
    AdjacentList = [[] for i in range(n)]
    for i in range(m):
        aux = [int(x) for x in f.readline().split()]
        AdjacentList[aux[0] - 1].append(aux[1])
        if graphType == "neorientat":
            aux.reverse()
            AdjacentList[aux[0] - 1].append((aux[1]))
    return AdjacentList

def toMatrix(myList, graphType):
    mat = []
    for i in range(len(myList)):
        mat.append([0] * len(myList))
    for i in range(len(myList)):
        for x in myList[i]:
            mat[i][x-1] = 1
            if graphType == "neorientat":
                mat[x-1][i] = 1
    return mat

graphType =input("Introduceti tipul grafului (orientat / neorientat): ")
myLists = createLists(graphType)
i = 0
for line in myLists:
    i += 1
    print(str(i) + ":", end= " ")
    print(*line)
myMatrix = toMatrix(myLists, graphType)