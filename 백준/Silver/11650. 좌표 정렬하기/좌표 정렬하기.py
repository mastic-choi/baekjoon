import sys
input = sys.stdin.readline

T = int(input())
list_1 = [0]*(T)
for i in range(T):
    x, y = map(int, input().split())
    list_1[i] = [x, y]

list_1.sort(key = lambda x : (x[0], x[1]))
for j in range(len(list_1)):
    q = list_1[j]
    print(q[0], q[1])