from collections import deque
import sys

x = int(sys.stdin.readline())

queue = deque(range(1, x + 1))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])
