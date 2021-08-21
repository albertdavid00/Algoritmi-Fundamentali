import math


def levDistance(fstWord, sndWord):
    if not len(fstWord):
        return len(sndWord)

    if not len(sndWord):
        return len(fstWord)

    if fstWord[0] == sndWord[0]:
        return levDistance(fstWord[1:], sndWord[1:])

    return 1 + min(levDistance(fstWord[1:], sndWord),
                   levDistance(fstWord, sndWord[1:]),
                   levDistance(fstWord[1:], sndWord[1:]))


def getWords(file):
    return file.read().replace("\n", " ").split()


def getSortedEdges(words):
    edges = []

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            dist = levDistance(words[i], words[j])
            edges.append((i, j, dist))

    edges.sort(key=lambda e: e[2])
    return edges


def repres(node):
    global parent
    if parent[node] == -1:
        return node

    parent[node] = repres(parent[node])
    return parent[node]


def unite(fstNode, sndNode):
    global n, parent, height, clusters
    rep1 = repres(fstNode)
    rep2 = repres(sndNode)

    height1 = height[rep1]
    height2 = height[rep2]

    if height1 > height2:
        parent[rep2] = rep1
        clusters[rep1] += clusters[rep2]
        clusters[rep2].clear()
        return

    parent[rep1] = rep2
    clusters[rep2] += clusters[rep1]
    clusters[rep1].clear()

    if height[rep1] == height[rep2]:
        height[rep2] += 1
    return


def printMST(mst):
    global words
    print("MSTree:", [(node1, node2, weight) for (node1, node2, weight) in mst])
    print("Weight:", sum(list(map(lambda x: x[2], mst))))


def getSeparationDegree(edges, index):
    for i in range(index + 1, len(edges)):
        fstNode, sndNode = edges[i][0], edges[i][1]

        if repres(fstNode) != repres(sndNode):
            sepDegree = edges[i][2]
            return sepDegree
    return 0


if __name__ == "__main__":
    k = 3
    words = getWords(open("cuvinte.in"))
    edges = getSortedEdges(words)
    n = len(words)

    parent = [-1 for _ in range(n)]
    height = [0 for _ in range(n)]
    clusters = [[i] for i in range(n)]

    minimumSpanningTree = []
    countEgdesInMST = 0

    for edge in edges:
        fstNode, sndNode = edge[0], edge[1]

        if repres(fstNode) != repres(sndNode):
            unite(fstNode, sndNode)
            minimumSpanningTree.append(edge)
            countEgdesInMST += 1

        if countEgdesInMST == n - k:  # we have k clusters
            break

    separationDegree = getSeparationDegree(edges, countEgdesInMST)

    for cluster in clusters:
        if cluster != []:
            for elem in cluster:
                print(words[elem], end=" ")
            print()
    print("Separation Degree:", separationDegree)