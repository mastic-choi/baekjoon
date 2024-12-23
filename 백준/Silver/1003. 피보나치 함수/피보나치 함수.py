# 백준 1003번 / 피보나치 함수
import sys
# 점화식 zeroCount[i] = zeroCount[i-1] + zeroCount[i-2]

#다이나믹 프로그램의 경우 꼭 규칙을 찾아서 점화식을 만들자!

T = int(sys.stdin.readline().strip()) #케이스 번호 받기
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  zero, one = 1, 0 #fib(0)의 0의 갯수와 1의 갯수 설정
  for i in range(N):
    zero, one = one, zero + one #피보나치 수열의 0의 갯수와 1의 갯수 계산
  print(zero, one)