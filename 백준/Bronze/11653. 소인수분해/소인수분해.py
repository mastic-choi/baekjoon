number = int(input())

d = 2
while number >= d:
    if number % d ==0:
        print(d)
        number = number / d

    else : 
        d = d + 1
