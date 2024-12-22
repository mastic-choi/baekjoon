# 백준 11723번 / 집합
import sys
S = set()


def add(x):
  if x not in S:
    S.add(x)


def remove(x):
  if x in S:
    S.remove(x)


def check(x):
  if x in S:
    print(1)
  else:
    print(0)


def toggle(x):
  if x in S:
    S.remove(x)
  elif x not in S:
    S.add(x)


def all():
  for i in range(1, 21):
    S.add(i)
def input():
  return sys.stdin.readline().rstrip()

def empty():
  S.clear()


N = int(input())
for _ in range(N):
  cmd = input().split()
  if cmd[0] == 'add':
    add(int(cmd[-1]))
  elif cmd[0] == 'remove':
    remove(int(cmd[-1]))
  elif cmd[0] == 'check':
    check(int(cmd[-1]))
  elif cmd[0] == 'toggle':
    toggle(int(cmd[-1]))
  elif cmd[0] == 'all':
    all()
  elif cmd[0] == 'empty':
    empty()
