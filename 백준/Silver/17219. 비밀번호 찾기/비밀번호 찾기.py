#백준 17219 / 비밀번호 찾기
import sys
N, M = map(int, sys.stdin.readline().split())
pwd = {}
for _ in range(N):
  x, y = map(str, sys.stdin.readline().split())
  pwd[x] = y
for _ in range(M):
  print(pwd[sys.stdin.readline().rstrip()])