def bfSearch(startNode, adjacentList = []):
    if not adjacentList:
        return []
    # startNode -= 1  # notation != actual value in list ( ex. if node = 1 then in list it's actually 0) !!!
    n = len(adjacentList)
    queue = [startNode]
    BFTree = [startNode]
    visited = [1 if startNode == node else 0 for node in range(n)]
    parent = [-1 for _ in range (n)]

    while queue:
        currentNode = queue[0]
        for neighbour in adjacentList[currentNode]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = 1
                BFTree.append(neighbour)
                parent[neighbour] = currentNode
        queue.pop(0)

    return BFTree   # return parent for more info

if __name__ == "__main__":
    bfTree = bfSearch(1)