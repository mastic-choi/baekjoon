import sys
input = sys.stdin.readline

T = int(input())
list = [0]*(T)
for i in range(T):
    list[i-1] = int(input())
list.sort()
for j in list:
    print(j)