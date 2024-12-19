import sys

k, n = map(int, sys.stdin.readline().split())
lines = []
for _ in range(k):
  x = int(sys.stdin.readline())
  lines.append(x)


def calLines(lines: list, n: int):
  start = 1
  end = max(lines)
  result = 0
  while (start <= end):
    mid = (start + end) // 2
    cnt_line = 0
    for line in lines:
      cnt_line += line // mid
    if cnt_line >= n:
      result = mid
      start = mid + 1
    elif cnt_line < n:
      end = mid - 1
  return result


print(calLines(lines, n))
