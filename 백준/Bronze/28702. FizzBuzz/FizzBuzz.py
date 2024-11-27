import sys


def fizzBuzz(a):
  if a % 3 == 0 and a % 5 == 0:
    return "FizzBuzz"
  elif a % 3 == 0:
    return "Fizz"
  elif a % 5 == 0:
    return "Buzz"
  else:
    return a


for i in range(3, 0, -1):
  X = sys.stdin.readline().strip()
  if X not in ['Fizz', 'Buzz', 'FizzBuzz']:
    n = int(X) + i
print(fizzBuzz(n))
