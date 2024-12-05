import sys

x = 0
for i in range(5):
  p = int(sys.stdin.readline().strip())
  x = x + p
print(x)