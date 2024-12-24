count = 0
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False 
    if x == 1:
        return False
    return True 

T = int(input())
numlist = list(map(int, input().split()))
for i in numlist:
    if is_prime_number(i):
        count = count+1
print(count)