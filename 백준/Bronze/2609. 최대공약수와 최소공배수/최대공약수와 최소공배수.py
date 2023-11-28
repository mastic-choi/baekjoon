a, b = map(int, input().split())

def GCD(x, y):
    while x%y!=0:
        x, y = y, x%y
    return y

def LCM(x, y):
    gcd = GCD(x,y)
    return int((x*y)/gcd)
print(GCD(a,b))
print(LCM(a,b))