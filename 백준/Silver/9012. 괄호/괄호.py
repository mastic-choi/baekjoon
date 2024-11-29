import sys

T = int(sys.stdin.readline())
for i in range(T):
  x = list(sys.stdin.readline().strip())
  stack = []
  for j in x:
    if j == "(":
      stack.append(j)
    elif j == ")":
      if len(stack) == 0:
        print("NO")
        break
      else:
        stack.pop()
  else:
    if len(stack) == 0:
      print("YES")
    else:
      print("NO")

#백준 9012번
