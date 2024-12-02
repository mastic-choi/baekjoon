import sys

N, H = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answr = 0
for i in a:
  if H >= i:
    answr += 1
print(answr)
