#백준 5354번 / J박스
import sys
input = sys.stdin.readline

#1. 입력받기
T = int(input())

for _ in range(T):
  x = int(input())
  if x >2:
    print('#'*x)
    for i in range(x-2):
        print('#' + 'J'*(x-2) + '#')
    print('#'*x, '\n')
  else :
    for i in range(x):
        print('#'*x)
    print()
