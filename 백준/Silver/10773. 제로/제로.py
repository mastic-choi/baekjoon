import sys

x = []  #stack 선언
K = int(sys.stdin.readline().strip())

for _ in range(K):
  n = int(sys.stdin.readline().strip())
  if n == 0:
    x.pop()
  else:
    x.append(n)
print(sum(x))
