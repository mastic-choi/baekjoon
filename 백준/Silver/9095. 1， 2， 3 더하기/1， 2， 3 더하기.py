#백준 9095번 / 1, 2, 3 더하기
import sys

dp = [0]*10001
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13

T = int(sys.stdin.readline().strip())
for _ in range(T):
  n = int(sys.stdin.readline().strip())
  if dp[n] != 0:
    print(dp[n])
  else:
    for i in range(4, n+1):
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
    