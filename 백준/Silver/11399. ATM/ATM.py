#백준 11399 / ATM
import sys

def input():
  return sys.stdin.readline().strip()

N = int(input())
timeList = list(map(int, sys.stdin.readline().split()))
sortedTimelist = sorted(timeList)
answr = []
for i in range(N):
  x = sortedTimelist[i]
  answr.append(x*(N-i))
print(sum(answr))
