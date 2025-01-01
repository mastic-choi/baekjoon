#백준 1541번 / 잃어버린 괄호호
import sys

input = sys.stdin.readline


def cal(a: str):
  s = list(a.split('+'))
  sum = 0
  for i in s:
    sum = sum + int(i)
  return sum


#1. 입력받기
mathFormula = input()
#2. '-'가 있는 수식인지 확인
T = False
for i in mathFormula:
  if i == '-':
    T = True
    break
mathFormula = mathFormula.split('-')
#3. 계산하기
if T:
  tmp = cal(mathFormula[0])
  for i in range(1, len(mathFormula)):
    tmp = tmp - cal(mathFormula[i])
else:
  tmp = cal(mathFormula[0])
print(tmp)
