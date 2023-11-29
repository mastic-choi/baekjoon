T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    room = []
    for i in range(k+1): #층
        if i == 0:
            room.extend(list(range(1, n+1)))
        else:
            for j in range(n):#호실의 인덱스
                t = sum(room[:j+1])
                room.append(t)
            del room[:n]
    print(room[-1])