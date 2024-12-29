import sys

def dfs(idx) :
  global visited
  visited[idx] = True
  print(idx, end = ' ')
  for i in range(1, N+1):
    if not visited[i] and graph[idx][i]:
      dfs(i)
  

def bfs():
  global q, visited
  while q:
    cur = q.pop(0)
    visited[cur] = True
    print(cur, end = ' ')
    for i in range(1, N+1):
      if not visited[i] and graph[cur][i]:
        visited[i] = True
        q.append(i)
  
  
    

# 0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 1. graph 정보 입력
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs 
dfs(V)
print()

# 3. bfs
visited = [False] * (N + 1)
q = [V]
bfs()