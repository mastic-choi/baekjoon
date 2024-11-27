import sys


def push(queue, item):  #stack과 동일하게 구현
  queue.append(item)
  return queue


def pop(queue):
  if len(queue) == 0:
    return -1  # pop할 아이탬이 없으면 -1을(를) pop하기
  else:
    popItem = queue[0]
    del queue[0]
    return popItem


def size(queue):
  return len(queue)


def empty(queue):
  if len(queue) == 0:
    return 1
  else:
    return 0


def front(queue):
  if len(queue) == 0:
    return -1
  else:
    return queue[0]


def back(queue):
  if len(queue) == 0:
    return -1
  else:
    return queue[-1]


queue = []
T = int(sys.stdin.readline())
for i in range(T):
  N = sys.stdin.readline().strip()
  if N == "front":
    print(front(queue))
  elif N == "back":
    print(back(queue))
  elif N == "pop":
    print(pop(queue))
  elif N == "size":
    print(size(queue))
  elif N == "empty":
    print(empty(queue))
  else:
    a, b = N.split()
    push(queue, int(b))
