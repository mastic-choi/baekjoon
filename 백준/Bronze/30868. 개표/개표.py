import sys

T = int(sys.stdin.readline())

def vote(x):
    a, b = x//5, x % 5
    c, d = "++++ "*a, "|"*b
    return c + d

myList = []
for i in range(T):
    n = int(sys.stdin.readline())
    myList.append(vote(n))

for x in myList:
    print(x)