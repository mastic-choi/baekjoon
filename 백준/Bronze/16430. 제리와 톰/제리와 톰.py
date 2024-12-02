import sys


def solution(a, b):
  c = b - a
  return c, b


a, b = map(int, sys.stdin.readline().split())

print(*solution(a, b))