import sys

x = int(sys.stdin.readline())
shirts = list(map(int, input().split()))
T, P = map(int, sys.stdin.readline().split())


def calShirts(shirts, T):
    answer = 0
    for i in shirts:
        answer += (i + T - 1) // T
    return answer


print(calShirts(shirts, T))
print((x // P), (x % P))
