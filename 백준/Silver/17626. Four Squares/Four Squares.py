#백준 17626번 / Four Squares
import sys
def input():
  return sys.stdin.readline()
n = int(input())
count = 0

DP = [0] * (n + 1)

k = 1
while k**2 <= n: #제곱수는 항상 답을 1로 가진다.
    DP[k**2] = 1
    k += 1

for i in range(1, n + 1):
    if DP[i] != 0:
        continue
    j = 1
    while j*j <= i:
        if DP[i] == 0:
            DP[i] = DP[j*j] + DP[i - j*j]
        else:
            DP[i] = min(DP[i], DP[j*j] + DP[i - j*j])
        j += 1
print(DP[n])