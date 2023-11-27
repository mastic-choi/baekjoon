set1 = set()
for i in range(10):
    x = int(input())
    set1.add(x%42)
print(len(set1))