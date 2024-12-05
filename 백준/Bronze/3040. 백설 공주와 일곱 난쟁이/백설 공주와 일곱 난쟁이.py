x = []
for i in range(9):
  x.append(int(input()))

for j in x:
  for k in x:
    if j != k:
      if (sum(x) - (j + k)) == 100:
        x.remove(j)
        x.remove(k)
        break

for p in x:
  print(p)
