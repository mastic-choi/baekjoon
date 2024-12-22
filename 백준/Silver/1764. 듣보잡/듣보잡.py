# 백준 1764 / 듣보잡
import sys
def input():
  return sys.stdin.readline().strip()
N, M = map(int, input().split())
name_hear = set() #듣도 못한 사람
name_see = set() #보도 못한 사람
for _ in range(N):
  name_hear.add(input())
for _ in range(M):
  name_see.add(input())
s = name_hear & name_see
x = sorted(list(s))
print(len(x))
for i in x:
  print(i)
