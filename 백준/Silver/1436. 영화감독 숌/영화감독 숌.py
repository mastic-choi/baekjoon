"""
브루트 포스 알고리즘으로 가능한 수를 모두 계산하고 666이 포함되면 count가 되는 식의 문제풀이.
"""

import sys
input = sys.stdin.readline
n = int(input())
num_str = '666'
first = 666
count = 1
while not count == n:
    first += 1
    if num_str in str(first):
        count += 1

print(first)
