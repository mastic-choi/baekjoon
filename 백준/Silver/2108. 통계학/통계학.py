import sys
from collections import Counter
'''
def roundNum(num):
  x = num + 0.5
  return round(x)
'''


def calaver(x: list):
  return round(sum(x) / len(x))


def modefinder(numbers):
  c = Counter(numbers)
  order = c.most_common()
  maximum = order[0][1]

  modes = []
  for num in order:
    if num[1] == maximum:
      modes.append(num[0])
  if len(modes) == 1:
    return modes[0]
  else:
    return modes[1]


T = int(sys.stdin.readline().strip())
x = []
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  x.append(N)

x.sort()
print(calaver(x))
print(x[len(x) // 2])
print(modefinder(x))
print(x[-1] - x[0])
