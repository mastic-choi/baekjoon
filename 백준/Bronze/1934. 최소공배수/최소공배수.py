def GCD(a, b):
    while not a%b == 0:
        a, b = b, a%b
    return b
def lcm(a, b):
    return (a*b)/GCD(a, b)
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print(int(lcm(b, a)))
