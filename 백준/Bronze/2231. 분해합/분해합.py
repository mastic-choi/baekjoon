num = int(input())
def find_num(x):
    for i in range(num+1):
        x = list(map(int, str(i)))
        if num == sum(x)+i:
            return i
    return 0

print(find_num(num))

