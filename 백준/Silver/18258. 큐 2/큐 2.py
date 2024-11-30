import sys
from collections import deque

queue = deque([])

def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def pop(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()  # FIFO 원칙에 따라 popleft()로 수정

T = int(sys.stdin.readline())
for _ in range(T):
    N = sys.stdin.readline().strip()
    if N == "front":
        if empty(queue):  # 큐가 비어 있는지 확인
            print(-1)
        else:
            print(queue[0])
    elif N == "back":
        if empty(queue):  # 큐가 비어 있는지 확인
            print(-1)
        else:
            print(queue[-1])
    elif N == "pop":
        print(pop(queue))
    elif N == "size":
        print(len(queue))
    elif N == "empty":
        print(empty(queue))
    else:  # push 명령 처리
        _, b = N.split()
        queue.append(b)