from math import inf
def editDistance(str1, str2, m, n):
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n),  # Remove
                   editDistance(str1, str2, m - 1, n - 1)  # Replace
                   )

def Reprez(node):
    global tata
    while tata[node - 1] != 0:
        node = tata[node - 1];
    return node

def Unite(u, v):
    global tata, height
    ru = Reprez(u)
    rv = Reprez(v)  # ar mai trebui o verificare pentru height
    if height[ru - 1] > height[rv - 1]:
        tata[rv - 1] = ru
        clusters[ru] = clusters[ru] + clusters[rv]
        clusters[rv].clear()
    else:
        tata[ru - 1] = rv
        clusters[rv] = clusters[rv] + clusters[ru]
        clusters[ru].clear()
        if height[ru - 1] == height[rv - 1]:
            height[rv - 1] = height[rv - 1] + 1

words = []
with open("cuvinte.in", "r") as file:
    for line in file:
        words.extend(line.split())
k = int(input("k = "))
Edges = []
n = len(words)
for i in range(n - 1):
    for j in range(i + 1, n):
        distance = editDistance(words[i], words[j], len(words[i]), len(words[j]))
        Edges.append((i, j, distance))

Edges.sort(key=lambda e: e[2])  # sortez lista de muchii
tata = [0 for i in range(n)]  # initializez lista de tati
height = [0 for i in range(n)]  # inaltimile
clusters = [[i] for i in range(n)]

nrmsel = 0
TreeEdges = []

for edge in Edges:
    if Reprez(edge[0]) != Reprez(edge[1]):
        TreeEdges.append(edge)
        Unite(edge[0], edge[1])
        nrmsel += 1
        if nrmsel == n - k:
            break

gradSep = inf
for i in range(n-1):
    for j in range(i+1, n):
        dist = editDistance(words[i], words[j], len(words[i]), len(words[j]))
        if Reprez(i) != Reprez(j) and dist < gradSep:
            gradSep = dist

for cluster in clusters:
    if cluster != []:
        for elem in cluster:
            print(words[elem], end= " ")
        print()
print("Grad separare:", gradSep)