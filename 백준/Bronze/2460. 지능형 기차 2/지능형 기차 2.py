# 백준 2460번 / 지능형 기차2
import sys
input = sys.stdin.readline

def solve():
    train = 0
    cnt = []
    for _ in range(10):
        x, y = map(int, input().split())
        train -= x
        train += y
        cnt.append(train)
    print(max(cnt))


if __name__ == '__main__':
    solve()