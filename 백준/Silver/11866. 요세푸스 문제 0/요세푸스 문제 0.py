"""
요세푸스 문제는 원형 큐의 개념을 이용해서 풀어야하며, deque 라이브러리를 활용하여 효율적으로 구현할 수 있다.
"""
import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
person = deque()
person.extend(list(range(1, n+1)))
result = []

while person:

    person.rotate(-k+1)
    result.append(person.popleft())

print('<' + ', '.join(map(str, result)) + '>')