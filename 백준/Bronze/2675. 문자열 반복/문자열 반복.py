n = int(input())
list1 = []
for i in range(1, n+1):
    x, myString = input().split()
    z = ""
    for j in myString:
        z = z + j*int(x)
    list1.append(z)
for k in list1:
    print(k)