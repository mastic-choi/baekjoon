import sys
input = sys.stdin.readline
n , k = map(int, input().split())
def pec(num):
    x = 1
    for i in range(1, num+1):
        x = x * i
    return x
def binomial(n : int,k : int):
    if k < 0 :
        return 0
    elif k > n :
        return 0
    else :
        return int(pec(n) / (pec(k)*pec(n - k)))
print(binomial(n, k))