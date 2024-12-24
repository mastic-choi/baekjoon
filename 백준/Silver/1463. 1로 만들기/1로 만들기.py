#백준 1463번 / 1로 만들기
import sys

d = [0] * 1000001


def input():
  return sys.stdin.readline().strip()


n = int(input())
for i in range(2, n + 1):
  #1을 빼는 연산
  d[i] = d[i - 1] + 1
  #2로 나누는 연산
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
print(d[n])
