import sys

T = int(sys.stdin.readline().strip())
a = []

coin = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
for _ in range(T):
  # 동전 던지기 결과 list로 받기
  x = list(sys.stdin.readline().strip())
  a.append(x)
for i in range(T):
  b = [0, 0, 0, 0, 0, 0, 0, 0]
  for j in range(len(a[i])):
    # 던지기 한 결과를 3개씩 slice 하기
    if (j + 2) == len(a[i]):
      break
    else:
      if a[i][j:j + 3] == list(coin[0]):
        b[0] += 1
      elif a[i][j:j + 3] == list(coin[1]):
        b[1] += 1
      elif a[i][j:j + 3] == list(coin[2]):
        b[2] += 1
      elif a[i][j:j + 3] == list(coin[3]):
        b[3] += 1
      elif a[i][j:j + 3] == list(coin[4]):
        b[4] += 1
      elif a[i][j:j + 3] == list(coin[5]):
        b[5] += 1
      elif a[i][j:j + 3] == list(coin[6]):
        b[6] += 1
      elif a[i][j:j + 3] == list(coin[7]):
        b[7] += 1
  print(*b)
