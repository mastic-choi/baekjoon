import sys
input = sys.stdin.readline
n = int(input())
def pec(num : int):
    x = 1
    for i in range(1, num+1):
        x = x * i
    return x
list_result = list(map(int, str(pec(n))))
count = 0
for i in reversed(list_result):
    if not i == 0:
        print(count)
        break
    else :
        count += 1