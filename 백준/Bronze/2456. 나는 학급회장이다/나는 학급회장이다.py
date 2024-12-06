from re import X

N = int(input())
x = [0, 0, 0]
y = [0, 0, 0]

for i in range(N):
  a, b, c = map(int, input().split())
  x[0] += a**2
  x[1] += b**2
  x[2] += c**2
  y[0] += a
  y[1] += b
  y[2] += c

if (x.count(max(x)) != 1):
  print("0", max(y))

else:
  q = x.index(max(x)) + 1
  print(q, max(y))
