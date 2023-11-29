A, B, V = map(int, input().split())

if V < A:
    print(1)
else :
    if (V-A)%(A-B) == 0:        
        print((V-A)//(A-B)+1)
    else : 
        print((V-A)//(A-B)+2)
