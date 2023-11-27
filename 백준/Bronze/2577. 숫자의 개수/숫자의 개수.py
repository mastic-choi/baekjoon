a = int(input())
b = int(input())
c = int(input())
z = list(map(int, str(a*b*c)))
cnt = []
for i in range(10):
    cnt.append(z.count(i))
for j in cnt:
    print(j)