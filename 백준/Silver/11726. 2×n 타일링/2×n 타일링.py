#백준 11726번 / 2 X n 타일링
import sys

n = int(sys.stdin.readline().strip())
if n == 1:
  print(1)
  exit()
elif n == 2:
  print(2)
  exit()

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, int(n)+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)