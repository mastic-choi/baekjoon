#백준 1012번 / 유기농 배추
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

#상하좌우 값 입력 (1,0), (-1,0), (0,1), (0,-1)
dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y, x):
  global visited
  visited[y][x] = True
  for dirIndex in range(4):
    newX = x + dirC[dirIndex]
    newY = y + dirR[dirIndex]
    if graph[newY][newX] and not visited[newY][newX]:  #배추가 있고 방문한적이 없으면
      dfs(newY, newX)


# 0 : 기본 세팅
T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[False] * MAX for _ in range(MAX)]
  visited = [[False] * MAX for _ in range(MAX)]
  # 1 : 그래프 입력 받기
  for _ in range(K):
    x, y = map(int, input().split())
    graph[y + 1][x + 1] = True
  # 2 : DFS
  answer = 0
  for i in range(1, N + 1):
    for j in range(1, M + 1):
      if graph[i][j] and not visited[i][j]:
        dfs(i, j)
        answer += 1
  print(answer)
