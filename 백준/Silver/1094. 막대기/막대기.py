import sys


X = int(sys.stdin.readline())
stick = 64
countTimes = 0

# X보다 작은 2의 배수를 구한 다음 빼주기
for i in range(10):
    if X == stick:
        countTimes += 1
        break
    if X > stick:
        countTimes += 1
        X = X-stick
    stick = stick//2
print(countTimes)