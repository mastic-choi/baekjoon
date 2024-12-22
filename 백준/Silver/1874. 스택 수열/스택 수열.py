#백준 1874 / 스택 수열
import sys
#python으로 제출하면 시간초과, pypy3로 제출하면 시간 정답 처리됨..


def input():
  return int(sys.stdin.readline().rstrip())


N = input()
stack = []
num_list = []  # 내가 만들어야 하는 수열을 입력받는다.
range_list = []  # 임시로 수열을 저장하는 역할
answr = []  #'+' 혹은 '-'를 입력해둔다.
B = True
for _ in range(N):  # 내가 만들어야 하는 수열을 입력받는다.
  num_list.append(input())
count = 1
for i in num_list:
  num = i
  if not ((num in range_list) or (num in stack)):
    for k in range(count, num + 1):  # stack에 pop하기
      range_list.append(k)
      count = count + 1
      answr.append('+')
  if range_list[-1] == num:  #range_list의 마지막 값이 num과 같다면
    stack.append(range_list.pop())
    answr.append('-')
  else:  # range_list의 마지막 값이 num과 다르다면
    B = False
    break
if B:
  for k in answr:
    print(k)
else:
  print('NO')
