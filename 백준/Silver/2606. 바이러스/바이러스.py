#백준 2606번 / 바이러스
import sys
#그래프 이론 문제
N = int(sys.stdin.readline())  # 컴퓨터의 수
M = int(sys.stdin.readline())  # 컴퓨터 연결 쌍 수
adj = [0] * (101)  # 인접 리스트
visit = [0] * (101)  # 방문 여부
global answer
answer = 0
for _ in range(M):
  x = list(map(int, sys.stdin.readline().split()))
  if adj[x[0]] == 0:
    adj[x[0]] = [x[1]]
  else:
    adj[x[0]].append(x[1])
  if adj[x[1]] == 0:
    adj[x[1]] = [x[0]]
  else:
    adj[x[1]].append(x[0])


#깊이 우선 탐색 방식으로 풀기
def dfs(c):
  global answer
  visit[c] = 1
  answer += 1
  if adj[c] != 0:
    for i in adj[c]:
      if visit[i] == 0:
        dfs(i)


dfs(1)
answer -= 1
print(answer)
