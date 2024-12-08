#1966번
import sys
from collections import deque

T = int(sys.stdin.readline().strip())

answer = []

for _ in range(T):
  N, M = map(int, sys.stdin.readline().strip().split())
  #문서의 개수 : N, 중요도 궁금한 문서 index : M
  p = deque(list(map(int, sys.stdin.readline().strip().split())))
  count = 0
  while p:
    best = max(p)
    front = p.popleft() #queue의 front를 뽑았다
    M -= 1 #내 위치를 앞당긴다.
    if front == best: #뽑은수가 가장큰수
      count+=1
      if M < 0:
        print(count)
        break
    else:
      p.append(front)
      if M < 0:
        M = len(p) -1