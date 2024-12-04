import sys
# divide and conquer
# 1. 문장을 받고 괄호랑 괄호를 제외한 str 분류하기
# 2. 괄호를 스택을 받아서 VPS를 여는 괄호의 경우! 스택에 넣고, 닫는 괄호의 경우! 스택에서 꺼내서 VPS를 만든다.
# 3. 괄호를 분류해서 받기! (교차해서 괄호를 받는 경우 어케할까요?)
while True:
  T = list(sys.stdin.readline().rstrip())
  stack = []
  if T[0] == '.':
    break
  for j in T:
    if j == ".":
      if len(stack) == 0:
        print("yes")
        break
      else:
        print("no")
        break
    if j == "(" or j == "[":
      stack.append(j)
    elif j == ")":
      if not stack or stack[-1] != "(":
        print('no')
        break
      stack.pop()
    elif j == "]":
      if not stack or stack[-1] != "[":
        print('no')
        break
      stack.pop()
