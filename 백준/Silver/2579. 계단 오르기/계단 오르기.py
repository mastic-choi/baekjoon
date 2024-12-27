#백준 2579 / 계단 오르기
import sys
#다이나믹 프로그램으로 풀기
N = int(sys.stdin.readline())  #계단의 수
dp = [0] * (N + 4)
point = [0] * (N + 4)
for i in range(1, N + 1):
  num = int(sys.stdin.readline())
  point[i] = num
dp[1] = point[1]
dp[2] = point[1] + point[2]
#마지막 계단을 밟았을때, 현재 위치에서 바로 직전 계단을 밟았을 경우와, 현재 위치 바로 직전 계단을 밟지 않았을 경우를 나눠 생각한다.
if N >= 3:
  for j in range(3, N + 1):
    dp[j] = max((dp[j - 3] + point[j] + point[j - 1]), (dp[j - 2] + point[j]))  
print(dp[N])
