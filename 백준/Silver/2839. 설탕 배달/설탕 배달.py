import sys
# 5x+3y = N
# minimization = x+y
# 그리디 알고리즘을 사용하여 해결할것


def solution(N):
  for i in range(N // 5, -1, -1):
    p = N - i * 5
    if p % 3 == 0:
      return i + (p // 3)
  else:
    return -1


N = int(sys.stdin.readline().strip())
print(solution(N))
