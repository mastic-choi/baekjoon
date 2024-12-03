import sys

B = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))
J = list(map(int, sys.stdin.readline().split()))



def solution(B, D, J):
  BtoJ = max(abs(B[0] - J[0]), abs(B[1] - J[1]))
  DtoJ = abs(D[0] - J[0]) + abs(D[1] - J[1])
  if BtoJ < DtoJ:
    return "bessie"
  elif BtoJ > DtoJ:
    return "daisy"
  elif BtoJ == DtoJ:
    return "tie"


print(solution(B, D, J))
