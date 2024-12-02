import sys


def solution(x, y):
  if x == y == 0:
    return "Not a moose"
  if x == y:
    return "Even " + str(x * 2)
  else:
    return "Odd " + str(max(x, y) * 2)


x, y = map(int, sys.stdin.readline().split())

print(solution(x, y))
