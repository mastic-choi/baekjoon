#백준 9461번 / 파도반 수열
import sys

T = int(sys.stdin.readline())
# 다이나믹 프로그래밍으로 해결
dp = [0] * 1001
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  for i in range(6, N + 1):
    if dp[i] == 0:
      dp[i] = dp[i - 2] + dp[i - 3]
  print(dp[N])
