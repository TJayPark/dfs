n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))


def dfs(i,j):
  #validation
  if(i<0 or i>=n or j<0 or j>=m):
    return False

  if(graph[i][j]==0):
    graph[i][j]=1
    #상
    dfs(i-1,j)
    #하
    dfs(i+1,j)
    #좌
    dfs(i,j-1)
    #우
    dfs(i,j+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if(dfs(i,j)==True):
      result+=1

print(result)

