#백준 16194 / 카드 구매하기
import sys

n = int(sys.stdin.readline().strip())
price = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
  a = [0] * i
  for k in range(i):
    a[k] = dp[i - (k + 1)] + price[k]
  dp[i] = min(a)
print(dp[n])