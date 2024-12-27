#백준 11047 / 동전 0
import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N): #코인을 List로 정리
  x = int(sys.stdin.readline())
  coin.append(x)
coin.sort(reverse=True)

answer = 0
for i in coin: 
  if K > 0:
    answer += K // i
    K = K - (K // i) * i
print(answer)