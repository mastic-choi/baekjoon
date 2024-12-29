# 백준 2178번 / 미로 탐색
import sys
input = sys.stdin.readline

# 1. 기본 세팅
N, M = map(int, input().split())  
graph = []
visited = [[False] * M for _ in range(N)]  # N x M 크기로 설정
for _ in range(N): 
    number = input().strip()
    x = list(map(int, number))
    graph.append(x)

# 2. BFS 탐색
queue = [(0, 0)]  # 시작점
visited[0][0] = True  # 시작점 방문 처리

dx = [1, -1, 0, 0]  # 이동 방향: 오른쪽, 왼쪽, 아래, 위
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있는지 체크
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and graph[ny][nx] == 1:  # 길이고 방문하지 않았으면
                    queue.append((ny, nx))  # 큐에 추가
                    visited[ny][nx] = True  # 방문 처리
                    graph[ny][nx] = graph[y][x] + 1  # 거리 갱신

bfs()

# 결과 출력: 목표 지점 (N-1, M-1)까지의 거리
print(graph[N-1][M-1])