# 백준 26561번 / Population
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p, t = map(int, input().split())
    x = p + (t//4) - (t//7)
    print(x)