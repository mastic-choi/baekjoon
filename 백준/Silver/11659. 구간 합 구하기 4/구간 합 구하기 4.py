#백준 11659번 / 구간 합 구하기4
import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
sumList = [0] * 100007
n = 1
for k in numList:
  sumList[n] = sumList[n-1] + k
  n += 1
for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  print(sumList[j] - sumList[i-1])
  # 해당 문제는 누적합 알고리즘으로 해결해야함!