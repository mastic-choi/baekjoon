#백준 9375번 / 패션왕 신해빈
import sys

T = int(sys.stdin.readline())  #테스트 케이스
for _ in range(T):
  n = int(sys.stdin.readline())  #가지고 있는 옷의 수
  wears = {}
  for i in range(n):
    name, type = sys.stdin.readline().split()
    if type in wears:
      wears[type].append(name)
    else:
      wears[type] = [name]
  answer = 1
  for j in wears:
    answer *= len(wears[j]) + 1
  print(answer - 1)