x = int(input())
d = 1
count = 0
while x >= 0:
    if x - d < 0:
        break
    else :
        x = x - d
        d = d + 1
        count = count + 1

print(count)