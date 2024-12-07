import sys
import math


def round(x):
  #python 내장round 함수는 오사오입(ex. 4.5 -> 4)이기 때문에 함수를 새로 선언
  #0.5를 더한 뒤에 math의 함수 이용해서 버림
  return math.floor(x + 0.5)


x = []
K = int(sys.stdin.readline().strip())

for _ in range(K):  #입력 받기
  n = int(sys.stdin.readline().strip())
  x.append(n)


def calDiff(theList):
  theList.sort()
  n = len(theList)
  q = theList[(round(n * 0.15)):(n - round(n * 0.15))]
  if len(q) == 0:
    return 0
  else:
    av = round(sum(q) / len(q))
    return av


print(calDiff(x))
