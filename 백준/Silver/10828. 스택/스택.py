import sys


def push(stack, item):
  stack.append(item)
  return stack


def pop(stack):
  if len(stack) == 0:
    return -1  # pop할 아이탬이 없으면 -1을(를) pop하기
  else:
    popItem = stack[-1]
    del stack[-1]
    return popItem


def size(stack):
  return len(stack)


def empty(stack):
  if len(stack) == 0:
    return 1
  else:
    return 0


def top(stack):
  if len(stack) == 0:
    return -1
  else:
    return stack[-1]


stack = []
T = int(sys.stdin.readline())
for i in range(T):
  N = sys.stdin.readline().strip()
  if N == "top":
    print(top(stack))
  elif N == "pop":
    print(pop(stack))
  elif N == "size":
    print(size(stack))
  elif N == "empty":
    print(empty(stack))
  else:
    a, b = N.split()
    push(stack, int(b))
