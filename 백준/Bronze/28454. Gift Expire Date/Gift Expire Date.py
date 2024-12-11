import datetime as dt
import sys

now_date = sys.stdin.readline().strip()
now_date = dt.datetime.strptime(now_date, '%Y-%m-%d')

n = int(sys.stdin.readline().strip())
answer = 0
for _ in range(n):
  date = sys.stdin.readline().strip()
  date = dt.datetime.strptime(date, '%Y-%m-%d')

  if date >= now_date:
    answer += 1
print(answer)
