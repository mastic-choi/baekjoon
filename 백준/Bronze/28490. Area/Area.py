import sys

n = int(sys.stdin.readline().strip())
anwer = []
for i in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  anwer.append(x * y)

print(max(anwer))
