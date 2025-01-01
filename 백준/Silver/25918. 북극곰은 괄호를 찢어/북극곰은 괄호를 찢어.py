# 백준 25918번 / 북극곰은 괄호를 찢어
# 스택
import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
min_day = 0
total = 0
for c in S:
    if c == '(':
        total += 1
    else:
        total -= 1
    if abs(total) > min_day:
        min_day = abs(total)
if total == 0:
    print(min_day)
else:
    print(-1)