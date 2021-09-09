def f(M):
    m = len(M)
    n = len(M[0])
    visited = [0]*m
    for i in range(m): 
        temp = [0]*n
        visited[i] = temp
    
    def getNeighbours(y, x):
        c = M[y][x]
        neighbours = []
        if (y>0 and not visited[y-1][x] and M[y-1][x] == c):
            neighbours.append([y-1, x])
        if (y < m - 1 and not visited[y+1][x] and M[y+1][x] == c):
            neighbours.append([y+1, x])
        if (x > 0 and not visited[y][x-1] and M[y][x-1] == c):
            neighbours.push([y, x-1])
        if (x < n - 1 and not visited[y][x+1] and M[y][x+1] == c):
            neighbours.append([y, x+1])

        return neighbours

    def getNeighbours(y,x):
        c = M[y][x]
        neighbours = []
        if (y > 0 and not visited[y-1][x] and M[y-1][x] == c):
            neighbours.append([y-1, x])
        if (y < m - 1 and not visited[y+1][x] and M[y+1][x] == c):
            neighbours.append([y+1, x])
        if (x > 0 and not visited[y][x-1] and M[y][x-1] == c):
            neighbours.append([y, x-1])
        if (x < n - 1 and not visited[y][x+1] and M[y][x+1] == c):
            neighbours.append([y, x+1])

        return neighbours
    
    def dfs(y,x):
        stack = [[y, x]]
  
        while (len(stack)):
            [y, x] = stack.pop()
            visited[y][x] = 1
            stack.extend(getNeighbours(y, x))
   
    count = 0
    for i in range(m):
        for j in range(n):
            if (not visited[i][j]):
                count+=1
                dfs(i,j)

    return count

M = [
  "ababc",
  "abbba",
  "aaabb",
  "bcccb",
  "acbbb",
  "aaabb"
]

print(f(M))