import math
import sys


def is_Prime_number(num):  #소수 판별 알고리즘
  if num == 1:
    return False
  else:
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
    return True


def solution(n, m):
  x = list(range(n, m + 1))
  a = []
  for i in x:
    if is_Prime_number(i):
      a.append(i)
  return a


n, m = map(int, sys.stdin.readline().split())
anwer = solution(n, m)
for i in anwer:
  print(i)
